# -*- mode: python -*-
a = Analysis(['F:\\sduty\\python\\pyqt1\\DlgHello.py'],
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
          name='DlgHello.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
