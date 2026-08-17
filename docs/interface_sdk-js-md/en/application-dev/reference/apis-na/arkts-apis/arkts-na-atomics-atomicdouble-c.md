# AtomicDouble

Provides an atomic wrapper for safe concurrent access to a double value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class AtomicDouble--><!--Device-unnamed-export class AtomicDouble-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: double, val: double): double
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-compareAndSwap(expected: double, val: double): double--><!--Device-AtomicDouble-compareAndSwap(expected: double, val: double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | double | Yes | the expected current value. |
| val | double | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the previous value |

## constructor

```TypeScript
constructor(val: double)
```

Constructs a new AtomicDouble with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-constructor(val: double)--><!--Device-AtomicDouble-constructor(val: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | double | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: double): double
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-exchange(val: double): double--><!--Device-AtomicDouble-exchange(val: double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | double | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: double): double
```

Atomically adds a value to the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-fetchAdd(val: double): double--><!--Device-AtomicDouble-fetchAdd(val: double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | double | Yes | the value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the previous value before the addition |

## fetchSub

```TypeScript
fetchSub(val: double): double
```

Atomically subtracts a value from the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-fetchSub(val: double): double--><!--Device-AtomicDouble-fetchSub(val: double): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | double | Yes | the value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| double | the previous value before the subtraction |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-static isLockFree(): boolean--><!--Device-AtomicDouble-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): double
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-load(): double--><!--Device-AtomicDouble-load(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | the current value |

## store

```TypeScript
store(val: double): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicDouble-store(val: double): void--><!--Device-AtomicDouble-store(val: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | double | Yes | the new value to store. |

