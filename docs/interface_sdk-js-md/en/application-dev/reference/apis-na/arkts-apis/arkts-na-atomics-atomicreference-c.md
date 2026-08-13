# AtomicReference

Provides an atomic reference wrapper for safe concurrent access to a reference value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class AtomicReference--><!--Device-unnamed-export class AtomicReference-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: T, ref: T): T
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicReference-compareAndSwap(expected: T, ref: T): T--><!--Device-AtomicReference-compareAndSwap(expected: T, ref: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | T | Yes | the expected current value. |
| ref | T | Yes | the new reference value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| T | the previous reference value |

## constructor

```TypeScript
constructor(ref: T)
```

Constructs a new AtomicReference with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicReference-constructor(ref: T)--><!--Device-AtomicReference-constructor(ref: T)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ref | T | Yes | the initial reference value. |

## exchange

```TypeScript
exchange(ref: T): T
```

Atomically exchanges the current reference value with a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicReference-exchange(ref: T): T--><!--Device-AtomicReference-exchange(ref: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ref | T | Yes | the new reference value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| T | the previous reference value |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicReference-static isLockFree(): boolean--><!--Device-AtomicReference-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): T
```

Atomically loads the current reference value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicReference-load(): T--><!--Device-AtomicReference-load(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | the current reference value |

## store

```TypeScript
store(ref: T): void
```

Atomically stores a new reference value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicReference-store(ref: T): void--><!--Device-AtomicReference-store(ref: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ref | T | Yes | the new reference value to store. |

