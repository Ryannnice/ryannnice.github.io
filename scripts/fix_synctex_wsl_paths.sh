#!/usr/bin/env bash
set -euo pipefail

synctex_gz="${1:-}"

if [[ -z "$synctex_gz" || ! -f "$synctex_gz" ]]; then
  exit 0
fi

tmp_file="$(mktemp)"
trap 'rm -f "$tmp_file"' EXIT

gzip -dc "$synctex_gz" | perl -pe '
  if (/^Input:(\d+):(?:\/\/wsl\.localhost\/[^\\\/]+\\|\\\\wsl\.localhost\\[^\\]+\\)(.*)$/) {
    my ($index, $rest) = ($1, $2);
    $rest =~ s{\\}{/}g;
    $_ = "Input:$index:/$rest\n";
  }
' | gzip -c > "$tmp_file"

mv "$tmp_file" "$synctex_gz"
