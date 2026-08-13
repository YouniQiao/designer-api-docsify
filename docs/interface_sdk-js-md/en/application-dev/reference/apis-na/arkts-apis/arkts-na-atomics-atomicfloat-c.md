# AtomicFloat

Provides an atomic wrapper for safe concurrent access to a float value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class AtomicFloat--><!--Device-unnamed-export class AtomicFloat-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: float, val: float): float
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-compareAndSwap(expected: float, val: float): float--><!--Device-AtomicFloat-compareAndSwap(expected: float, val: float): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | float | Yes | the expected current value. |
| val | float | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| float | the previous value |

## constructor

```TypeScript
constructor(val: float)
```

Constructs a new AtomicFloat with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-constructor(val: float)--><!--Device-AtomicFloat-constructor(val: float)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | float | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: float): float
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-exchange(val: float): float--><!--Device-AtomicFloat-exchange(val: float): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | float | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| float | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: float): float
```

Atomically adds a value to the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-fetchAdd(val: float): float--><!--Device-AtomicFloat-fetchAdd(val: float): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | float | Yes | the value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| float | the previous value before the addition |

## fetchSub

```TypeScript
fetchSub(val: float): float
```

Atomically subtracts a value from the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-fetchSub(val: float): float--><!--Device-AtomicFloat-fetchSub(val: float): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | float | Yes | the value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| float | the previous value before the subtraction |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-static isLockFree(): boolean--><!--Device-AtomicFloat-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): float
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-load(): float--><!--Device-AtomicFloat-load(): float-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| float | the current value |

## store

```TypeScript
store(val: float): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicFloat-store(val: float): void--><!--Device-AtomicFloat-store(val: float): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | float | Yes | the new value to store. |

