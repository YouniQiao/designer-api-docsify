# AtomicByte

Provides an atomic wrapper for safe concurrent access to a byte value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicByte--><!--Device-unnamed-export class AtomicByte-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: byte, val: byte): byte
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-compareAndSwap(expected: byte, val: byte): byte--><!--Device-AtomicByte-compareAndSwap(expected: byte, val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | byte | 是 | the expected current value. |
| val | byte | 是 | the new value to store if the comparison succeeds. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value |

## constructor

```TypeScript
constructor(val: byte)
```

Constructs a new AtomicByte with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-constructor(val: byte)--><!--Device-AtomicByte-constructor(val: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the initial value. |

## exchange

```TypeScript
exchange(val: byte): byte
```

Atomically exchanges the current value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-exchange(val: byte): byte--><!--Device-AtomicByte-exchange(val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the new value to exchange with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: byte): byte
```

Atomically adds a value to the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-fetchAdd(val: byte): byte--><!--Device-AtomicByte-fetchAdd(val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: byte): byte
```

Atomically performs a bitwise AND operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-fetchAnd(val: byte): byte--><!--Device-AtomicByte-fetchAnd(val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: byte): byte
```

Atomically performs a bitwise OR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-fetchOr(val: byte): byte--><!--Device-AtomicByte-fetchOr(val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: byte): byte
```

Atomically subtracts a value from the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-fetchSub(val: byte): byte--><!--Device-AtomicByte-fetchSub(val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: byte): byte
```

Atomically performs a bitwise XOR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-fetchXor(val: byte): byte--><!--Device-AtomicByte-fetchXor(val: byte): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-static isLockFree(): boolean--><!--Device-AtomicByte-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): byte
```

Atomically loads the current value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-load(): byte--><!--Device-AtomicByte-load(): byte-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| byte | the current value |

## store

```TypeScript
store(val: byte): void
```

Atomically stores a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicByte-store(val: byte): void--><!--Device-AtomicByte-store(val: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | byte | 是 | the new value to store. |

