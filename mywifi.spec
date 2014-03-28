# -*- mode: python -*-
a = Analysis(['F:\\sduty\\python\\mywifi\\mywifi.py'],
             pathex=['F:\\sduty\\python\\pyinsexe'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mywifi.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='F:\\sduty\\python\\mywifi\\img\\wx.ico')
