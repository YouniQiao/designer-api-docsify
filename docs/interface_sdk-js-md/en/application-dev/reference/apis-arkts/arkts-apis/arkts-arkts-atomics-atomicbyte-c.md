# AtomicByte

Provides an atomic wrapper for safe concurrent access to a byte value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class AtomicByte--><!--Device-unnamed-export class AtomicByte-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## compareAndSwap

```TypeScript
compareAndSwap(expected: byte, val: byte): byte
```

Atomically compares the current value with the expected value and replaces it if equal

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-compareAndSwap(expected: byte, val: byte): byte--><!--Device-AtomicByte-compareAndSwap(expected: byte, val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expected | byte | Yes | the expected current value. |
| val | byte | Yes | the new value to store if the comparison succeeds. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value |

## constructor

```TypeScript
constructor(val: byte)
```

Constructs a new AtomicByte with the provided initial value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-constructor(val: byte)--><!--Device-AtomicByte-constructor(val: byte)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the initial value. |

## exchange

```TypeScript
exchange(val: byte): byte
```

Atomically exchanges the current value with a new value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-exchange(val: byte): byte--><!--Device-AtomicByte-exchange(val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the new value to exchange with. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: byte): byte
```

Atomically adds a value to the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-fetchAdd(val: byte): byte--><!--Device-AtomicByte-fetchAdd(val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the value to add. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: byte): byte
```

Atomically performs a bitwise AND operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-fetchAnd(val: byte): byte--><!--Device-AtomicByte-fetchAnd(val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the value to AND with. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: byte): byte
```

Atomically performs a bitwise OR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-fetchOr(val: byte): byte--><!--Device-AtomicByte-fetchOr(val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the value to OR with. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: byte): byte
```

Atomically subtracts a value from the current value and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-fetchSub(val: byte): byte--><!--Device-AtomicByte-fetchSub(val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the value to subtract. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: byte): byte
```

Atomically performs a bitwise XOR operation and returns the previous value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-fetchXor(val: byte): byte--><!--Device-AtomicByte-fetchXor(val: byte): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the value to XOR with. |

**Return value:**

| Type | Description |
| --- | --- |
| byte | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-static isLockFree(): boolean--><!--Device-AtomicByte-static isLockFree(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): byte
```

Atomically loads the current value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-load(): byte--><!--Device-AtomicByte-load(): byte-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| byte | the current value |

## store

```TypeScript
store(val: byte): void
```

Atomically stores a new value

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicByte-store(val: byte): void--><!--Device-AtomicByte-store(val: byte): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| val | byte | Yes | the new value to store. |

