[English](Architecture) · [Dansk](Architecture-da) · **Bahasa Melayu**

# Seni bina

Kod dalam `src/rock_paper_scissors/` mengikut seni bina berlapis (bersih): peraturan tidak bergantung pada konsol atau penjana nombor rawak.

| Lapisan | Pakej | Mengandungi |
| --- | --- | --- |
| Domain | `domain` | `Choice`, `RoundResult` dan `determine_result`, peraturan permainan |
| Aplikasi | `application` | Kes guna `PlayRound` dan port `ComputerChoiceSource` |
| Infrastruktur | `infrastructure` | `RandomChoiceSource`, yang melaksanakan port, dan `bootstrap.main`, akar gubahan |
| Pembentangan | `presentation` | `PlayRoundCommand`, seni ASCII, tajuk dan penghurai input |

Import menuju ke dalam: `domain` tidak mengimport apa-apa daripada lapisan lain, `application` mengimport `domain`, `presentation` mengimport `application` dan `domain`, dan hanya `infrastructure` mengimport semua lapisan.

## Ujian

Ujian dalam `tests/` mencerminkan lapisan:

- `tests/unit`: peraturan, kes guna (dengan komputer palsu) dan pembantu pembentangan
- `tests/integration`: sumber pilihan rawak
- `tests/e2e`: satu pusingan penuh melalui `bootstrap.main`, dan larian sebenar `python -m rock_paper_scissors`

```bash
python -m pytest
```

## Alat

`ruff` memformat dan menyemak kod, dan `mypy --strict` menyemak jenis; kedua-duanya ditetapkan dalam `pyproject.toml`.

Kembali ke [Utama](Home-ms).
