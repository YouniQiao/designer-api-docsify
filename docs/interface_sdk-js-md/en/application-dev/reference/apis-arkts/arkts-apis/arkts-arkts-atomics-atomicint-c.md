# AtomicInt

Provides an atomic wrapper for safe concurrent access to an int value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export class AtomicInt--><!--Device-unnamed-export class AtomicInt-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## compareAndSwap

```TypeScript
compareAndSwap(expected: int, val: int): int
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-compareAndSwap(expected: int, val: int): int--><!--Device-AtomicInt-compareAndSwap(expected: int, val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | int | Yes | the expected current value. <br>The value should be an integer. |
| val | int | Yes | the new value to store if the comparison succeeds. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value |

## constructor

```TypeScript
constructor(val: int)
```

Constructs a new AtomicInt with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-constructor(val: int)--><!--Device-AtomicInt-constructor(val: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the initial value. <br>The value should be an integer. |

## exchange

```TypeScript
exchange(val: int): int
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-exchange(val: int): int--><!--Device-AtomicInt-exchange(val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the new value to exchange with. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: int): int
```

Atomically adds a value to the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-fetchAdd(val: int): int--><!--Device-AtomicInt-fetchAdd(val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the value to add. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: int): int
```

Atomically performs a bitwise AND operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-fetchAnd(val: int): int--><!--Device-AtomicInt-fetchAnd(val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the value to AND with. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: int): int
```

Atomically performs a bitwise OR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-fetchOr(val: int): int--><!--Device-AtomicInt-fetchOr(val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the value to OR with. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: int): int
```

Atomically subtracts a value from the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-fetchSub(val: int): int--><!--Device-AtomicInt-fetchSub(val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the value to subtract. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: int): int
```

Atomically performs a bitwise XOR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-fetchXor(val: int): int--><!--Device-AtomicInt-fetchXor(val: int): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the value to XOR with. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-static isLockFree(): boolean--><!--Device-AtomicInt-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): int
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-load(): int--><!--Device-AtomicInt-load(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | the current value |

## store

```TypeScript
store(val: int): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicInt-store(val: int): void--><!--Device-AtomicInt-store(val: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | int | Yes | the new value to store. <br>The value should be an integer. |

