# AtomicBoolean

Provides an atomic wrapper for safe concurrent access to a boolean value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class AtomicBoolean--><!--Device-unnamed-export class AtomicBoolean-End-->

**System capability:** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: boolean, val: boolean): boolean
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicBoolean-compareAndSwap(expected: boolean, val: boolean): boolean--><!--Device-AtomicBoolean-compareAndSwap(expected: boolean, val: boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | boolean | Yes | the expected current value. |
| val | boolean | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the previous value |

## constructor

```TypeScript
constructor(val: boolean)
```

Constructs a new AtomicBoolean with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicBoolean-constructor(val: boolean)--><!--Device-AtomicBoolean-constructor(val: boolean)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | boolean | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: boolean): boolean
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicBoolean-exchange(val: boolean): boolean--><!--Device-AtomicBoolean-exchange(val: boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | boolean | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the previous value |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicBoolean-static isLockFree(): boolean--><!--Device-AtomicBoolean-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): boolean
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicBoolean-load(): boolean--><!--Device-AtomicBoolean-load(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | the current value |

## store

```TypeScript
store(val: boolean): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicBoolean-store(val: boolean): void--><!--Device-AtomicBoolean-store(val: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | boolean | Yes | the new value to store. |

