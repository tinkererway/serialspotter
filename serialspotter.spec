# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path


a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\amal\\Documents\\kivy_workspace\\serialspotter'],
    binaries=[],
    datas=[('serialspotter.kv','.'),('SpaceMono-Regular.ttf','font'),('icon_serialspotter.png','icon')],
    hiddenimports=['kivymd'],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='serialspotter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
	*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='serialspotter',
)
