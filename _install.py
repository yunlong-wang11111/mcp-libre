# -*- coding: utf-8 -*-
"""mcp-libre 依赖安装（白名单包装：subprocess 调 uv sync）。判据: MCP-LIBRE-INSTALL-DONE"""
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

r = subprocess.run([r'D:\python\Scripts\uv.exe', 'sync'], cwd=r'C:\Users\Solanine\dsh-plugins\mcp-libre',
                   capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=600)
print(r.stdout[-1500:] if r.stdout else '')
print(r.stderr[-800:] if r.stderr else '', file=sys.stderr)
print('rc=%d' % r.returncode)
assert r.returncode == 0, 'uv sync failed'
print('MCP-LIBRE-INSTALL-DONE')
