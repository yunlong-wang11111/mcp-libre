# -*- coding: utf-8 -*-
"""mcp-libre 冒烟：造一个 docx → 用 libremcp 的转换能力转 PDF → 断言产物。
判据: MCP-LIBRE-SMOKE-DONE"""
import os
import sys

sys.path.insert(0, r'C:\Users\Solanine\dsh-plugins\mcp-libre\src')
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

OUT = r'D:\temp\mcp_libre_smoke'
os.makedirs(OUT, exist_ok=True)

# ① 造一个小 docx（纯 stdlib zipfile 造最小 Word 文档）
docx = os.path.join(OUT, 'smoke.docx')
import zipfile
with zipfile.ZipFile(docx, 'w') as z:
    z.writestr('[Content_Types].xml',
               '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
               '<Default Extension="xml" ContentType="application/xml"/>'
               '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
    z.writestr('_rels/.rels',
               '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
               '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
    z.writestr('word/document.xml',
               '<?xml version="1.0"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
               '<w:body><w:p><w:r><w:t>mcp-libre smoke test 2026</w:t></w:r></w:p></w:body></w:document>')
print('docx 造好: %d bytes' % os.path.getsize(docx))

# ② 用 libremcp 的底层转换（与 MCP 工具同一条 _run_libreoffice_command 通路）
import libremcp as L
r = L._run_libreoffice_command(['--headless', '--convert-to', 'pdf', '--outdir', OUT, docx], timeout=60)
pdf = os.path.join(OUT, 'smoke.pdf')
assert os.path.exists(pdf) and os.path.getsize(pdf) > 1000, 'PDF 未生成: rc=%s out=%s err=%s' % (
    r.returncode, (r.stdout or '')[:120], (r.stderr or '')[:120])
print('PDF 生成: %d bytes' % os.path.getsize(pdf))
print('MCP-LIBRE-SMOKE-DONE')
