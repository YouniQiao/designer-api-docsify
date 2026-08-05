# AtomicLong

Provides an atomic wrapper for safe concurrent access to a long value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class AtomicLong--><!--Device-unnamed-export class AtomicLong-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: long, val: long): long
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-compareAndSwap(expected: long, val: long): long--><!--Device-AtomicLong-compareAndSwap(expected: long, val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | long | Yes | the expected current value. |
| val | long | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value |

## constructor

```TypeScript
constructor(val: long)
```

Constructs a new AtomicLong with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-constructor(val: long)--><!--Device-AtomicLong-constructor(val: long)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: long): long
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-exchange(val: long): long--><!--Device-AtomicLong-exchange(val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: long): long
```

Atomically adds a value to the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-fetchAdd(val: long): long--><!--Device-AtomicLong-fetchAdd(val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: long): long
```

Atomically performs a bitwise AND operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-fetchAnd(val: long): long--><!--Device-AtomicLong-fetchAnd(val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: long): long
```

Atomically performs a bitwise OR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-fetchOr(val: long): long--><!--Device-AtomicLong-fetchOr(val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: long): long
```

Atomically subtracts a value from the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-fetchSub(val: long): long--><!--Device-AtomicLong-fetchSub(val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: long): long
```

Atomically performs a bitwise XOR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-fetchXor(val: long): long--><!--Device-AtomicLong-fetchXor(val: long): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| long | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-static isLockFree(): boolean--><!--Device-AtomicLong-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): long
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-load(): long--><!--Device-AtomicLong-load(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | the current value |

## store

```TypeScript
store(val: long): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicLong-store(val: long): void--><!--Device-AtomicLong-store(val: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | long | Yes | the new value to store. |

