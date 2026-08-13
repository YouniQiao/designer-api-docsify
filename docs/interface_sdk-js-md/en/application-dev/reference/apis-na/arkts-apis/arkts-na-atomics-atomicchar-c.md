# AtomicChar

Provides an atomic wrapper for safe concurrent access to a char value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class AtomicChar--><!--Device-unnamed-export class AtomicChar-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: char, val: char): char
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicChar-compareAndSwap(expected: char, val: char): char--><!--Device-AtomicChar-compareAndSwap(expected: char, val: char): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | char | Yes | the expected current value. |
| val | char | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the previous value |

## constructor

```TypeScript
constructor(val: char)
```

Constructs a new AtomicChar with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicChar-constructor(val: char)--><!--Device-AtomicChar-constructor(val: char)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | char | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: char): char
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicChar-exchange(val: char): char--><!--Device-AtomicChar-exchange(val: char): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | char | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| char | the previous value |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicChar-static isLockFree(): boolean--><!--Device-AtomicChar-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): char
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicChar-load(): char--><!--Device-AtomicChar-load(): char-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| char | the current value |

## store

```TypeScript
store(val: char): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicChar-store(val: char): void--><!--Device-AtomicChar-store(val: char): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | char | Yes | the new value to store. |

