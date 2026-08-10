# AtomicInt

Provides an atomic wrapper for safe concurrent access to an int value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicInt--><!--Device-unnamed-export class AtomicInt-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: int, val: int): int
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-compareAndSwap(expected: int, val: int): int--><!--Device-AtomicInt-compareAndSwap(expected: int, val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | int | 是 | the expected current value. &lt;br&gt;The value should be an integer. |
| val | int | 是 | the new value to store if the comparison succeeds. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value |

## constructor

```TypeScript
constructor(val: int)
```

Constructs a new AtomicInt with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-constructor(val: int)--><!--Device-AtomicInt-constructor(val: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the initial value. &lt;br&gt;The value should be an integer. |

## exchange

```TypeScript
exchange(val: int): int
```

Atomically exchanges the current value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-exchange(val: int): int--><!--Device-AtomicInt-exchange(val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the new value to exchange with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: int): int
```

Atomically adds a value to the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-fetchAdd(val: int): int--><!--Device-AtomicInt-fetchAdd(val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the value to add. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: int): int
```

Atomically performs a bitwise AND operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-fetchAnd(val: int): int--><!--Device-AtomicInt-fetchAnd(val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the value to AND with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: int): int
```

Atomically performs a bitwise OR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-fetchOr(val: int): int--><!--Device-AtomicInt-fetchOr(val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the value to OR with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: int): int
```

Atomically subtracts a value from the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-fetchSub(val: int): int--><!--Device-AtomicInt-fetchSub(val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the value to subtract. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: int): int
```

Atomically performs a bitwise XOR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-fetchXor(val: int): int--><!--Device-AtomicInt-fetchXor(val: int): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the value to XOR with. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-static isLockFree(): boolean--><!--Device-AtomicInt-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): int
```

Atomically loads the current value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-load(): int--><!--Device-AtomicInt-load(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the current value |

## store

```TypeScript
store(val: int): void
```

Atomically stores a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicInt-store(val: int): void--><!--Device-AtomicInt-store(val: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | int | 是 | the new value to store. &lt;br&gt;The value should be an integer. |

