# -*- mode: python -*-

block_cipher = None


a = Analysis(['Poster_File_Compare_v1.0.py'],
             pathex=['c:\\Test1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Poster_File_Compare_v1.0',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
