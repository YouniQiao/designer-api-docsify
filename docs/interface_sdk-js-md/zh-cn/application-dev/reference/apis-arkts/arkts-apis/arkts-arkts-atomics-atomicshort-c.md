# AtomicShort

Provides an atomic wrapper for safe concurrent access to a short value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicShort--><!--Device-unnamed-export class AtomicShort-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: short, val: short): short
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-compareAndSwap(expected: short, val: short): short--><!--Device-AtomicShort-compareAndSwap(expected: short, val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | short | 是 | the expected current value. |
| val | short | 是 | the new value to store if the comparison succeeds. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value |

## constructor

```TypeScript
constructor(val: short)
```

Constructs a new AtomicShort with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-constructor(val: short)--><!--Device-AtomicShort-constructor(val: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the initial value. |

## exchange

```TypeScript
exchange(val: short): short
```

Atomically exchanges the current value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-exchange(val: short): short--><!--Device-AtomicShort-exchange(val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the new value to exchange with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: short): short
```

Atomically adds a value to the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-fetchAdd(val: short): short--><!--Device-AtomicShort-fetchAdd(val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value before the addition |

## fetchAnd

```TypeScript
fetchAnd(val: short): short
```

Atomically performs a bitwise AND operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-fetchAnd(val: short): short--><!--Device-AtomicShort-fetchAnd(val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the value to AND with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value before the operation |

## fetchOr

```TypeScript
fetchOr(val: short): short
```

Atomically performs a bitwise OR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-fetchOr(val: short): short--><!--Device-AtomicShort-fetchOr(val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the value to OR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value before the operation |

## fetchSub

```TypeScript
fetchSub(val: short): short
```

Atomically subtracts a value from the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-fetchSub(val: short): short--><!--Device-AtomicShort-fetchSub(val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value before the subtraction |

## fetchXor

```TypeScript
fetchXor(val: short): short
```

Atomically performs a bitwise XOR operation and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-fetchXor(val: short): short--><!--Device-AtomicShort-fetchXor(val: short): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the value to XOR with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the previous value before the operation |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-static isLockFree(): boolean--><!--Device-AtomicShort-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): short
```

Atomically loads the current value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-load(): short--><!--Device-AtomicShort-load(): short-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| short | the current value |

## store

```TypeScript
store(val: short): void
```

Atomically stores a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicShort-store(val: short): void--><!--Device-AtomicShort-store(val: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | short | 是 | the new value to store. |

