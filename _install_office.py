# -*- coding: utf-8 -*-
"""python-office-mcp 安装（白名单包装）：uv tool install（走镜像 git）。
判据: OFFICE-MCP-INSTALL-DONE"""
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

REPO = 'https://gh-proxy.com/https://github.com/rcarmo/python-office-mcp-server.git'
r = subprocess.run([r'D:\python\Scripts\uv.exe', 'tool', 'install', '--force',
                    'git+' + REPO],
                   capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=900)
print((r.stdout or '')[-1200:])
print((r.stderr or '')[-600:], file=sys.stderr)
print('rc=%d' % r.returncode)
assert r.returncode == 0, 'uv tool install failed'
# 验证命令存在
v = subprocess.run(['where', 'office-mcp-server'], capture_output=True, text=True)
print('exe:', (v.stdout or '').strip()[:120])
print('OFFICE-MCP-INSTALL-DONE')
