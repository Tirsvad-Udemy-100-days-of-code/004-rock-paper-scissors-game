[English](Install) · [Dansk](Install-da) · **Bahasa Melayu**

# Pemasangan

## Keperluan

- Python 3.13 atau lebih baharu
- Tiada kebergantungan semasa larian; `pytest`, `ruff` dan `mypy` dipasang untuk pembangunan

## Langkah

Cipta dan aktifkan persekitaran maya dalam `.venv`:

```bash
python -m venv .venv
```

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux / Git Bash
source .venv/bin/activate
```

Pasang projek dalam mod boleh sunting bersama alat pembangunan:

```bash
python -m pip install -e ".[dev]"
```

Keluar daripada persekitaran dengan `deactivate`. Seterusnya: [Main](Play-ms).
