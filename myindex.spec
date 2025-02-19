# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\myindex.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\__pycache__\\*', '__pycache__'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\assets\\*', 'assets'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\components\\*', 'components'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\app.py', '.'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\df_cat_despesa.csv', '.'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\df_cat_receita.csv', '.'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\df_despesas.csv', '.'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\df_receitas.csv', '.'), ('C:\\Users\\griso\\OneDrive\\Documentos\\Faculdade\\Finanças Pessoais_Python\\globals.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='myindex',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
