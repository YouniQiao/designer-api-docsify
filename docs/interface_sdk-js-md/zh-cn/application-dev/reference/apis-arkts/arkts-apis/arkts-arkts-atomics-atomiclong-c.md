# AtomicLong

Provides an atomic wrapper for safe concurrent access to a long value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicLong--><!--Device-unnamed-export class AtomicLong-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: long, val: long): long
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-compareAndSwap(expected: long, val: long): long--><!--Device-AtomicLong-compareAndSwap(expected: long, val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | long | 是 | the expected current value. |
| val | long | 是 | the new value to store if the comparison succeeds. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value |

## constructor

```TypeScript
constructor(val: long)
```

Constructs a new AtomicLong with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-constructor(val: long)--><!--Device-AtomicLong-constructor(val: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the initial value. |

## exchange

```TypeScript
exchange(val: long): long
```

Atomically exchanges the current value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-exchange(val: long): long--><!--Device-AtomicLong-exchange(val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the new value to exchange with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: long): long
```

Atomically adds a value to the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-fetchAdd(val: long): long--><!--Device-AtomicLong-fetchAdd(val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: long): long
```

Atomically performs a bitwise AND operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-fetchAnd(val: long): long--><!--Device-AtomicLong-fetchAnd(val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: long): long
```

Atomically performs a bitwise OR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-fetchOr(val: long): long--><!--Device-AtomicLong-fetchOr(val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: long): long
```

Atomically subtracts a value from the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-fetchSub(val: long): long--><!--Device-AtomicLong-fetchSub(val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: long): long
```

Atomically performs a bitwise XOR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-fetchXor(val: long): long--><!--Device-AtomicLong-fetchXor(val: long): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-static isLockFree(): boolean--><!--Device-AtomicLong-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): long
```

Atomically loads the current value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-load(): long--><!--Device-AtomicLong-load(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the current value |

## store

```TypeScript
store(val: long): void
```

Atomically stores a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicLong-store(val: long): void--><!--Device-AtomicLong-store(val: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | long | 是 | the new value to store. |

