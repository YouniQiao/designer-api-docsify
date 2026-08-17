# AtomicShort

Provides an atomic wrapper for safe concurrent access to a short value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class AtomicShort--><!--Device-unnamed-export class AtomicShort-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: short, val: short): short
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-compareAndSwap(expected: short, val: short): short--><!--Device-AtomicShort-compareAndSwap(expected: short, val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | short | Yes | the expected current value. |
| val | short | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value |

## constructor

```TypeScript
constructor(val: short)
```

Constructs a new AtomicShort with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-constructor(val: short)--><!--Device-AtomicShort-constructor(val: short)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: short): short
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-exchange(val: short): short--><!--Device-AtomicShort-exchange(val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: short): short
```

Atomically adds a value to the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-fetchAdd(val: short): short--><!--Device-AtomicShort-fetchAdd(val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: short): short
```

Atomically performs a bitwise AND operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-fetchAnd(val: short): short--><!--Device-AtomicShort-fetchAnd(val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: short): short
```

Atomically performs a bitwise OR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-fetchOr(val: short): short--><!--Device-AtomicShort-fetchOr(val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: short): short
```

Atomically subtracts a value from the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-fetchSub(val: short): short--><!--Device-AtomicShort-fetchSub(val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: short): short
```

Atomically performs a bitwise XOR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-fetchXor(val: short): short--><!--Device-AtomicShort-fetchXor(val: short): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| short | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-static isLockFree(): boolean--><!--Device-AtomicShort-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): short
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-load(): short--><!--Device-AtomicShort-load(): short-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| short | the current value |

## store

```TypeScript
store(val: short): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicShort-store(val: short): void--><!--Device-AtomicShort-store(val: short): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | short | Yes | the new value to store. |

