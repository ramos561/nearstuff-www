#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path.cwd()
CSS = ROOT / "assets" / "css" / "main.css"

if not CSS.exists():
    print("[ERRO] Executa este patch na raiz do repositório nearstuff-www.")
    print("Não encontrei assets/css/main.css")
    sys.exit(1)

text = CSS.read_text(encoding="utf-8")

marker = "/* Nearstuff platform CTA visibility */"
rule = """
/* Nearstuff platform CTA visibility
   Temporário: remover esta regra quando web.nearstuff.com estiver público. */
a[href^="https://web.nearstuff.com"] {
  display: none !important;
}
"""

if marker in text:
    start = text.index(marker)
    # Replace an existing final visibility block if this patch is rerun.
    prefix = text[:start].rstrip()
    text = prefix + "\n\n" + rule.strip() + "\n"
else:
    text = text.rstrip() + "\n\n" + rule.strip() + "\n"

CSS.write_text(text, encoding="utf-8")

print("[OK] assets/css/main.css")
print("[OK] Todos os links/CTAs para web.nearstuff.com ficam ocultos.")
print("[OK] A estrutura HTML foi mantida para ser reativada mais tarde.")
print()
print("Para voltar a mostrar os botões no futuro, remove do CSS:")
print('  a[href^="https://web.nearstuff.com"] { display: none !important; }')
