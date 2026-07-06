#!/usr/bin/env python3
"""
Generate locale-specific sidebars with nested HTML lists and CSS left-border indentation.
No Unicode tree characters — pure HTML <ul>/<li> with border-left for visual hierarchy.

Root _sidebar.md: Kit-level only.
Per-kit _sidebars/{kit}.html: Nested HTML lists.
"""
import os, re, sys

DOCS = os.environ.get("DOCS_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs"))

JS_SDK = "interface_sdk-js-md"
C_SDK = "interface_sdk_c-md"
REF_PATH = "application-dev/reference"


def find_readme(kit_dir, api_subdir):
    api_dir = os.path.join(kit_dir, api_subdir)
    if not os.path.isdir(api_dir):
        return None
    for f in sorted(os.listdir(api_dir)):
        if f.endswith('.md') and 'readme' in f.lower():
            return os.path.join(api_dir, f)
    return None


def parse_readme_hierarchy(readme_path):
    """Parse Readme indentation -> list of (indent_level, label, filename or None).

    Matches:
      - [label](file.md)     -> link entry
      - label                -> section header (no link, no brackets)
      - label<!--comment-->  -> section header with comment
    """
    if not os.path.isfile(readme_path):
        return []
    entries = []
    with open(readme_path) as f:
        for line in f:
            # Try link format: - [label](file.md)
            m = re.match(r'^(\s*)-\s*\[([^\]]+)\]\(([^)]+\.md)\)', line)
            if m:
                indent = len(m.group(1))
                label = m.group(2).strip()
                filename = m.group(3).strip()
                if not filename.startswith('http'):
                    entries.append((indent, label, filename))
                continue
            # Try section header format: - label or - label<!--...-->
            m = re.match(r'^(\s*)-\s+([^<\n\[\n]+)', line)
            if m:
                indent = len(m.group(1))
                label = m.group(2).strip()
                # Skip if it looks like random text (must be a grouping header)
                if label and not label.startswith('#') and indent == 0:
                    entries.append((indent, label, None))
    return entries


def build_html_nested(entries, base_path, max_depth=4):
    """Build nested HTML <ul>/<li> from parsed entries.

    Returns (html_string, first_link, total_count).
    """
    if not entries:
        return "", None, 0

    first_link = None
    total_count = 0

    def esc(s):
        return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    def render_nested(items, depth=0):
        nonlocal first_link, total_count
        if not items or depth > max_depth:
            return ""

        cls = f"tree-l{depth + 1}"
        parts = [f'<ul class="{cls}">']
        i = 0
        while i < len(items):
            indent, label, filename = items[i]

            # Gather children
            children = []
            j = i + 1
            while j < len(items) and items[j][0] > indent:
                children.append(items[j])
                j += 1

            has_link = filename is not None
            if has_link:
                path = f"{base_path}/{filename}"
                if first_link is None:
                    first_link = path

            escaped = esc(label)
            if children:
                parts.append(f'<li class="has-children"><details>')
                if has_link:
                    parts.append(f'<summary>{escaped} <a href="#/{path}" class="tree-nav" onclick="event.stopPropagation()" title="Open page">↗</a></summary>')
                else:
                    parts.append(f'<summary>{escaped}</summary>')
                parts.append(render_nested(children, depth + 1))
                parts.append('</details></li>')
            elif has_link:
                parts.append(f'<li><a href="#/{path}">{escaped}</a></li>')
            else:
                parts.append(f'<li>{escaped}</li>')

            total_count += 1
            i = j

        parts.append('</ul>')
        return '\n'.join(parts)

    html = render_nested(entries)
    return html, first_link, total_count


def wrap_section_html(html, label, count):
    escaped = label.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return (
        f'<div class="tree-section">\n'
        f'  <details>\n'
        f'    <summary class="tree-section-label">{escaped} <span class="tree-count">({count})</span></summary>\n'
        f'    {html}\n'
        f'  </details>\n'
        f'</div>'
    )


def collect_kits(sdk_dir, locale):
    ref_dir = os.path.join(DOCS, sdk_dir, locale, REF_PATH)
    if not os.path.isdir(ref_dir):
        return {}
    kits = {}
    for entry in sorted(os.listdir(ref_dir)):
        full = os.path.join(ref_dir, entry)
        if os.path.isdir(full):
            kits[entry.replace("apis-", "")] = full
    return kits


def generate_sidebars(sidebar_locale):
    js_kits = collect_kits(JS_SDK, sidebar_locale)
    c_kits = collect_kits(C_SDK, sidebar_locale)
    all_kits = sorted(set(list(js_kits.keys()) + list(c_kits.keys())))

    sidebar_dir = os.path.join(DOCS, sidebar_locale, "_sidebars")
    os.makedirs(sidebar_dir, exist_ok=True)

    root_lines = []
    total_files = 0

    for kit in all_kits:
        display_label = kit.replace('-', ' ').title()
        section_htmls = []
        kit_file_count = 0
        first_link = None

        # JS API
        if kit in js_kits:
            kit_dir = js_kits[kit]
            readme = find_readme(kit_dir, "arkts-apis")
            if readme:
                base_path = f"{JS_SDK}/{sidebar_locale}/{REF_PATH}/apis-{kit}/arkts-apis"
                entries = parse_readme_hierarchy(readme)
                tree_html, fl, cnt = build_html_nested(entries, base_path)
                if tree_html:
                    section_htmls.append(wrap_section_html(tree_html, "ArkTS API", cnt))
                    kit_file_count += cnt
                    if not first_link:
                        first_link = fl

        # C API
        if kit in c_kits:
            kit_dir = c_kits[kit]
            readme = find_readme(kit_dir, "c-apis")
            if readme:
                base_path = f"{C_SDK}/{sidebar_locale}/{REF_PATH}/apis-{kit}/c-apis"
                entries = parse_readme_hierarchy(readme)
                tree_html, fl, cnt = build_html_nested(entries, base_path)
                if tree_html:
                    section_htmls.append(wrap_section_html(tree_html, "C API", cnt))
                    kit_file_count += cnt
                    if not first_link:
                        first_link = fl

        # Write per-kit HTML
        with open(os.path.join(sidebar_dir, f"{kit}.html"), 'w') as f:
            f.write('\n'.join(section_htmls))

        # Root sidebar link
        if first_link:
            root_lines.append(f"- [{display_label} ({kit_file_count})]({first_link})")
        else:
            root_lines.append(f"- {display_label}")

        total_files += kit_file_count

    # Write root _sidebar.md
    with open(os.path.join(DOCS, sidebar_locale, "_sidebar.md"), 'w') as f:
        f.write('\n'.join(root_lines))

    print(f"  {sidebar_locale}: {len(all_kits)} kits, {total_files} apis")


for locale in ["en", "zh-cn"]:
    generate_sidebars(locale)
print("Done.")
