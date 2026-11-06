# 给 mcp-libre venv（uv 建，无 pip 模块）补装 pyserial——用 uv pip 定向装。
import subprocess, sys
r = subprocess.run(["uv", "pip", "install", "--python", sys.executable, "pyserial>=3.5"],
                   capture_output=True, text=True, timeout=300)
print(r.stdout[-800:])
print(r.stderr[-300:] if r.returncode else "")
import serial
print("PYSERIAL_OK", serial.VERSION)
