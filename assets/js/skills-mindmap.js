const maps = document.querySelectorAll('.skills-mindmap');

// Keep the complete HTML outline available until the diagram is ready.
async function renderMap(container) {
  const data = JSON.parse(container.querySelector('.skills-mindmap__data').textContent);
  const language = container.dataset.language;
  const viewport = container.querySelector('.skills-mindmap__viewport');
  const canvas = container.querySelector('.skills-mindmap__canvas');
  const toolbar = container.querySelector('.skills-mindmap__toolbar');
  const outline = container.querySelector('.skills-mindmap__outline');
  const zoomLabel = container.querySelector('.skills-mindmap__zoom');
  const zoomOut = container.querySelector('[data-map-action="out"]');
  const zoomIn = container.querySelector('[data-map-action="in"]');

  const lines = ['mindmap'];
  const nodes = [];
  const edges = new Map();
  function addNode(node, depth, branch = 'root', parentIndex) {
    const index = nodes.length;
    const label = node[language].replace(/&/g, '&amp;').replace(/"/g, '&quot;');
    lines.push(`${'  '.repeat(depth)}${node.id}["${label}"]`);
    const metadata = { id: node.id, depth: depth - 1, branch, leaf: !node.children };
    nodes.push(metadata);
    if (parentIndex !== undefined) edges.set(`edge_${parentIndex}_${index}`, metadata);
    node.children?.forEach(child => addNode(child, depth + 1, depth === 1 ? child.id : branch, index));
  }
  addNode(data, 1);

  const [{ default: mermaid }, { default: tidyTreeLayouts }] = await Promise.all([
    import('https://cdn.jsdelivr.net/npm/mermaid@12.3.0/dist/mermaid.esm.min.mjs'),
    import('https://cdn.jsdelivr.net/npm/@mermaid-js/layout-tidy-tree@1.0.1/dist/mermaid-layout-tidy-tree.esm.min.mjs'),
    document.fonts.ready
  ]);
  mermaid.registerLayoutLoaders(tidyTreeLayouts);
  mermaid.initialize({
    startOnLoad: false,
    layout: 'tidy-tree',
    securityLevel: 'strict',
    theme: 'base',
    htmlLabels: false,
    themeVariables: {
      fontFamily: getComputedStyle(container).fontFamily,
      fontSize: '18px'
    },
    // Mindmap labels use the shared Markdown renderer's wrapping width.
    flowchart: { wrappingWidth: 200 },
    mindmap: { useMaxWidth: false, padding: 20, maxNodeWidth: 280 }
  });
  const diagramId = `skills-map-${language}`;
  const { svg } = await mermaid.render(diagramId, lines.join('\n'));
  canvas.innerHTML = svg;
  const diagram = canvas.querySelector('svg');
  diagram.querySelectorAll('.mindmap-node').forEach((node, index) => {
    node.dataset.skill = nodes[index].id;
    node.dataset.depth = nodes[index].depth;
    node.dataset.branch = nodes[index].branch;
  });
  diagram.querySelectorAll('.edgePaths path').forEach(path => {
    const target = edges.get(path.dataset.id);
    if (!target) return;
    path.dataset.branch = target.branch;
    path.dataset.depth = target.depth;
    const thickness = target.leaf ? 1.4 : Math.max(2.25, 6.5 - target.depth * 1.5);
    path.style.setProperty('--skills-branch-width', `${thickness}px`);
  });
  const bounds = diagram.viewBox.baseVal;
  const padding = 24;
  const width = bounds.width + padding * 2;
  const height = bounds.height + padding * 2;
  diagram.setAttribute('viewBox', `${bounds.x - padding} ${bounds.y - padding} ${width} ${height}`);
  diagram.removeAttribute('width');
  diagram.removeAttribute('height');
  diagram.removeAttribute('style');
  diagram.setAttribute('role', 'img');

  const title = document.createElementNS('http://www.w3.org/2000/svg', 'title');
  title.id = `${diagramId}-title`;
  title.textContent = data[language];
  const description = document.createElementNS('http://www.w3.org/2000/svg', 'desc');
  description.id = `${diagramId}-description`;
  description.textContent = language === 'zh'
    ? '研究与工程能力、工具与软件、英语。完整文字清单位于图下方。'
    : 'Research and engineering, tools and software, and English proficiency. A complete text outline follows the map.';
  diagram.prepend(title, description);
  diagram.setAttribute('aria-labelledby', title.id);
  diagram.setAttribute('aria-describedby', description.id);

  toolbar.hidden = false;
  viewport.hidden = false;
  outline.open = false;
  let zoom = 1;
  const minZoom = 0.2;
  const maxZoom = 1.5;

  function setZoom(value, focus = 'center') {
    const viewportBox = viewport.getBoundingClientRect();
    const oldBox = canvas.getBoundingClientRect();
    const centerX = (viewportBox.left + viewport.clientWidth / 2 - oldBox.left) / zoom;
    const centerY = (viewportBox.top + viewport.clientHeight / 2 - oldBox.top) / zoom;
    zoom = Math.max(minZoom, Math.min(maxZoom, value));
    canvas.style.width = `${width * zoom}px`;
    canvas.style.height = `${height * zoom}px`;
    zoomLabel.textContent = `${Math.round(zoom * 100)}%`;
    zoomOut.disabled = zoom <= minZoom;
    zoomIn.disabled = zoom >= maxZoom;

    if (focus === 'root') {
      const rootBox = diagram.querySelector('.section-root').getBoundingClientRect();
      viewport.scrollLeft += rootBox.left + rootBox.width / 2 - viewportBox.left - viewport.clientWidth / 2;
      viewport.scrollTop += rootBox.top + rootBox.height / 2 - viewportBox.top - viewport.clientHeight / 2;
    } else if (focus === 'fit') {
      viewport.scrollLeft = (viewport.scrollWidth - viewport.clientWidth) / 2;
      viewport.scrollTop = (viewport.scrollHeight - viewport.clientHeight) / 2;
    } else {
      const nextBox = canvas.getBoundingClientRect();
      viewport.scrollLeft += nextBox.left + centerX * zoom - viewportBox.left - viewport.clientWidth / 2;
      viewport.scrollTop += nextBox.top + centerY * zoom - viewportBox.top - viewport.clientHeight / 2;
    }
  }

  toolbar.addEventListener('click', event => {
    const branch = event.target.closest('[data-focus-branch]')?.dataset.focusBranch;
    if (branch) {
      setZoom(0.85);
      const boxes = Array.from(diagram.querySelectorAll(`.mindmap-node[data-branch="${branch}"]`), node => node.getBoundingClientRect());
      const viewportBox = viewport.getBoundingClientRect();
      const centerX = (Math.min(...boxes.map(box => box.left)) + Math.max(...boxes.map(box => box.right))) / 2;
      const centerY = (Math.min(...boxes.map(box => box.top)) + Math.max(...boxes.map(box => box.bottom))) / 2;
      viewport.scrollLeft += centerX - viewportBox.left - viewport.clientWidth / 2;
      viewport.scrollTop += centerY - viewportBox.top - viewport.clientHeight / 2;
      return;
    }
    const action = event.target.closest('[data-map-action]')?.dataset.mapAction;
    if (action === 'out') setZoom(zoom - 0.15);
    if (action === 'in') setZoom(zoom + 0.15);
    if (action === 'reset') setZoom(1, 'root');
    if (action === 'fit') {
      setZoom(Math.min((viewport.clientWidth - 24) / width, (viewport.clientHeight - 24) / height), 'fit');
    }
  });

  // Touch keeps native scrolling; mouse users can also drag the map.
  let drag;
  viewport.addEventListener('pointerdown', event => {
    if (event.pointerType !== 'mouse' || event.button !== 0) return;
    drag = { x: event.clientX, y: event.clientY, left: viewport.scrollLeft, top: viewport.scrollTop };
    viewport.setPointerCapture(event.pointerId);
    viewport.classList.add('is-dragging');
    event.preventDefault();
    viewport.focus({ preventScroll: true });
  });
  viewport.addEventListener('pointermove', event => {
    if (!drag) return;
    viewport.scrollLeft = drag.left + drag.x - event.clientX;
    viewport.scrollTop = drag.top + drag.y - event.clientY;
  });
  function endDrag() {
    drag = undefined;
    viewport.classList.remove('is-dragging');
  }
  viewport.addEventListener('pointerup', endDrag);
  viewport.addEventListener('pointercancel', endDrag);
  viewport.addEventListener('lostpointercapture', endDrag);

  setZoom(0.85, 'root');
  container.dataset.ready = 'true';
}

function loadMap(container) {
  renderMap(container).catch(error => {
    console.error('Could not render the skills map.', error);
  });
}

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      observer.unobserve(entry.target);
      loadMap(entry.target);
    });
  }, { rootMargin: '300px' });
  maps.forEach(map => observer.observe(map));
} else {
  maps.forEach(loadMap);
}
