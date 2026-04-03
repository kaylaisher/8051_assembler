# 8051 Assembler

A two-pass assembler for the Intel 8051 (MCS-51) microcontroller, written in Python. It reads 8051 assembly source files, translates each instruction into machine code, and outputs the result as a sequence of hexadecimal bytes.

## Supported Instructions

| Instruction | Addressing Modes |
|---|---|
| **MOV** | direct↔direct, @Ri←#imm, Rn←direct |
| **SUBB** | A←@Ri, A←Rn |
| **XRL** | direct↔#imm, direct↔A, A↔direct |
| **INC** | @Ri, Rn |
| **JZ** | relative offset |
| **LCALL** | addr16 |
| **RET** | (implied) |

## Folder Structure

```
8051_assembler/
├── assembler.py        # Main entry point (two-pass engine)
├── main.py             # Machine code generation (Pass 2)
├── location.py         # Address calculation (Pass 1)
├── Address.py          # Instruction sizes & shared data
├── util.py             # Utility functions
├── test_file/          # Input assembly source files
│   └── Test04.txt
├── out/                # Machine code output files
│   └── Test04-out.txt
└── log/                # Debug log files
    └── Test04-log.txt
```

## How It Works

### Two-Pass Architecture

The assembler reads the source file **twice** to handle forward references (e.g., a `JZ` or `LCALL` referencing a label defined later in the source).

```
Assembly Source (.txt)
        │
        ▼
┌─────────────────────────────────┐
│  Pass 1: assembler.py           │
│  → Calls location.py methods    │
│  → Reads sizes from Address.py  │
│  → Builds Data.addr_data        │
└─────────────────────────────────┘
        │
        ▼  Data.addr_data (address table)
┌─────────────────────────────────┐
│  Pass 2: assembler.py           │
│  → Calls main.py methods        │
│  → Uses util.py conversions     │
│  → Resolves labels via table    │
└─────────────────────────────────┘
        │
        ▼
  Machine Code Output (.txt)
```

**Pass 1 – Address Calculation:** Scans every line, identifies each instruction or label, determines how many bytes it occupies, and records the address information (current address, next address) into a shared data structure (`Data.addr_data`). After this pass, the address of every label is known.

**Pass 2 – Code Generation:** Scans the file again, converts each instruction into machine code bytes using the opcode tables and addressing-mode rules, and writes the hex output to the output file. Instructions like `JZ` and `LCALL` resolve label references using the address table built in Pass 1.

---

## Module Descriptions

### `assembler.py` — Main Entry Point

The main program file that orchestrates the assembly process. It opens the source file, parses each line, and dispatches to the appropriate handler.

**Line Parsing:** Each line is split by commas and whitespace using `re.split(r'[, ]+', line)`. Trailing newlines are stripped. The result is a list like `["MOV", "30H", "40H"]`.

**Dispatch Logic (both passes):**
- If the first token contains `:` → it's a **label**
- Otherwise, match the mnemonic (`MOV`, `SUBB`, `XRL`, etc.) and inspect operand patterns (e.g., `"H"` for direct addressing, `"@"` for register-indirect, `"#"` for immediate) to select the correct addressing mode handler

### `Address.py` — Instruction Sizes & Shared Data

Serves two purposes:

1. **Instruction size classes** — defines the byte count for each instruction/addressing-mode combination:

| Class | Attribute | Size (bytes) | Example |
|---|---|---|---|
| `MOVaddr` | `direct_direct_addr` | 3 | `MOV 30H, 40H` |
| `MOVaddr` | `reg_imm_addr` | 2 | `MOV @R0, #55H` |
| `MOVaddr` | `Rn_direct_addr` | 2 | `MOV R7, 30H` |
| `SUBBaddr` | `A_Ri_addr` | 1 | `SUBB A, @R0` |
| `SUBBaddr` | `A_Rn_addr` | 1 | `SUBB A, R3` |
| `XRLaddr` | `direct_imm_addr` | 3 | `XRL 30H, #40H` |
| `XRLaddr` | `direct_A_addr` | 2 | `XRL 30H, A` |
| `XRLaddr` | `A_direct_addr` | 2 | `XRL A, 30H` |
| `INCaddr` | `Ri_addr` | 1 | `INC @R0` |
| `INCaddr` | `Rn_addr` | 1 | `INC R3` |
| `JZaddr` | `jz_addr` | 2 | `JZ label` |
| `LCALLaddr` | `lcall_addr` | 3 | `LCALL label` |
| `RETaddr` | `ret_addr` | 1 | `RET` |

2. **`Data` class (shared state)** — class-level variables that persist across both passes:

| Attribute | Type | Description |
|---|---|---|
| `addr_data` | `list[list]` | Stores `[line_index, tokens, current_addr, next_addr]` for every line |
| `addr_detail` | `list` | Temp storage for the current line before appending to `addr_data` |
| `addr_index` | `int` | Current line number (incremented after each line in Pass 1) |
| `current_addr_cnt` | `int` | Starting byte address of the current instruction (PC) |
| `next_addr_cnt` | `int` | Byte address after the current instruction (PC + size) |

### `location.py` — Address Calculation (Pass 1)

The `Location` class contains one static method per instruction/addressing-mode variant. Every method follows the same pattern:

1. Set `current_addr_cnt = next_addr_cnt` (save current PC)
2. Add the instruction's byte size to `next_addr_cnt` (advance the PC)
3. Build `addr_detail = [line_index, tokens, current_addr, next_addr]`
4. Append `addr_detail` to `Data.addr_data`
5. Write debug info to the log file

For **labels**, the byte size added is `0` — labels don't produce machine code, but their address is recorded so `JZ` and `LCALL` can reference it.

<details>
<summary>Full method list</summary>

| Method | Triggered By | Bytes Added |
|---|---|---|
| `label_location()` | Line contains `:` (e.g. `XADD:`) | 0 |
| `MOVdirect_direct_location()` | `MOV <direct>, <direct>` | 3 |
| `MOVreg_imm_location()` | `MOV @Ri, #imm` | 2 |
| `MOVRn_direct_location()` | `MOV Rn, <direct>` | 2 |
| `SUBBA_Ri_location()` | `SUBB A, @Ri` | 1 |
| `SUBBA_Rn_location()` | `SUBB A, Rn` | 1 |
| `XRLdirect_imm_location()` | `XRL <direct>, #imm` | 3 |
| `XRLdirect_A_location()` | `XRL <direct>, A` | 2 |
| `XRLA_direct_location()` | `XRL A, <direct>` | 2 |
| `lcall_location()` | `LCALL <label>` | 3 |
| `INCRi_location()` | `INC @Ri` | 1 |
| `INCRn_location()` | `INC Rn` | 1 |
| `jz_location()` | `JZ <label>` | 2 |
| `ret_location()` | `RET` | 1 |

</details>

### `main.py` — Machine Code Generation (Pass 2)

One class per instruction mnemonic, with methods for each addressing mode. Each method encodes the instruction into hex bytes and writes them to the output file.

| Class.Method | Binary Opcode | Output Bytes | Description |
|---|---|---|---|
| `MOV.direct_direct()` | `10000101` | `85 src dest` | Opcode + source addr + dest addr |
| `MOV.reg_imm()` | `0111011i` | `7E/7F imm` | Ri bit encoded in opcode |
| `MOV.Rn_direct()` | `10101nnn` | `A8–AF direct` | Register number in low 3 bits |
| `SUBB.A_Ri()` | `1001011i` | `96/97` | Single-byte; Ri bit in opcode |
| `SUBB.A_Rn()` | `10011nnn` | `98–9F` | Register number in low 3 bits |
| `XRL.direct_imm()` | `01100011` | `63 direct imm` | Opcode + direct + immediate |
| `XRL.direct_A()` | `01100010` | `62 direct` | Opcode + direct address |
| `XRL.A_direct()` | `01100101` | `65 direct` | Opcode + direct address |
| `LCALL.lcall()` | `00010010` | `12 addrHi addrLo` | Opcode + 16-bit label address |
| `INC.Ri()` | `0000011i` | `06/07` | Single-byte; Ri bit in opcode |
| `INC.Rn()` | `00001nnn` | `08–0F` | Register number in low 3 bits |
| `JZ.jz()` | `01100000` | `60 offset` | Opcode + signed relative offset |
| `RET.ret()` | `00100010` | `22` | Single-byte instruction |

#### Special Cases

**LCALL** looks up the target label's absolute address by searching `Data.addr_data` for a matching label entry, retrieves the address, splits it into high byte and low byte, and writes three bytes: `opcode + addrHi + addrLo`.

**JZ** uses relative addressing. It looks up both the label's absolute address and the current instruction's next address (PC after fetch), then computes `offset = label_addr − next_addr`. Negative offsets (backward jumps) are converted to two's complement: `((|offset| XOR 0xFF) + 1)`.

### `util.py` — Utility Functions

| Function | Example | Description |
|---|---|---|
| `bin_to_hex(str)` | `"10000101"` → `"85"` | Binary string to hex |
| `check_format(raw)` | `"30H"` → `"30"`, `"@R0"` → `"0"`, `"#0B3H"` → `"B3"` | Strips addressing notation (`@`, `#`, `H`, `R`) |
| `dec_to_3bit_bin(n)` | `5` → `"101"` | Decimal to 3-bit binary (for register encoding) |
| `dec_to_16bit_bin(n)` | `255` → `"0000000011111111"` | Decimal to 16-bit binary |
| `check_size(output)` | `"5"` → `"05"` | Ensures exactly 2 uppercase hex digits |
| `offset(label, current)` | `(3, 10)` → `"F9"` | Signed offset; negatives become two's complement hex |

---

## Worked Example

Given this assembly source:

```asm
    MOV   30H, 40H
    LCALL XADD
    XRL   30H, #40H
XADD:
    SUBB  A, R3
    RET
```

### Pass 1 — Address Table

| Line | Instruction | Current Addr | Next Addr | Bytes |
|---|---|---|---|---|
| 0 | `MOV 30H, 40H` | 0 | 3 | 3 |
| 1 | `LCALL XADD` | 3 | 6 | 3 |
| 2 | `XRL 30H, #40H` | 6 | 9 | 3 |
| 3 | `XADD:` | 9 | 9 | 0 |
| 4 | `SUBB A, R3` | 9 | 10 | 1 |
| 5 | `RET` | 10 | 11 | 1 |

### Pass 2 — Machine Code Output

```
85 40 30 12 00 09 63 30 40 9B 22
```

Breakdown:
- `85 40 30` — `MOV 30H, 40H` (opcode `85` + source `40` + dest `30`)
- `12 00 09` — `LCALL XADD` (opcode `12` + address `0009H` where the `XADD` label is)
- `63 30 40` — `XRL 30H, #40H` (opcode `63` + direct `30` + immediate `40`)
- `9B` — `SUBB A, R3` (opcode `10011` + register `011` = `9B`)
- `22` — `RET`

---

## Log Files

The assembler writes detailed debug logs to `log/`. Each entry includes the line index, parsed instruction tokens, current address, next address, and (in Pass 2) the generated machine code bytes. Useful for verifying correctness and debugging.

## Limitations & Future Work

- Only a subset of the 8051 instruction set is implemented
- Addressing mode detection relies on simple string matching (e.g., checking for `"H"` or `"@"`), which may not cover all edge cases
- No error handling for invalid instructions or malformed input
- File paths are hardcoded to `Test04`; could accept command-line arguments
- The `Data` class uses mutable class-level variables as global state, preventing concurrent use
