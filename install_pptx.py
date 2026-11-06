# 一次性安装脚本：把 python-pptx 装进 mcp-libre 的 venv（供 read_impress_layout 工具用）。
# 用本 venv 的 python 跑：.venv/Scripts/python.exe install_pptx.py
import subprocess, sys
try:
    import pptx  # noqa: F401
    print("PPTX_ALREADY_INSTALLED", pptx.__version__)
    sys.exit(0)
except ImportError:
    pass
r = subprocess.run([sys.executable, "-m", "pip", "install", "python-pptx>=1.0.2"],
                   capture_output=True, text=True, timeout=300)
print(r.stdout[-2000:])
print(r.stderr[-500:] if r.returncode else "")
import pptx
print("PPTX_INSTALL_OK", pptx.__version__)
