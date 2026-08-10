# AtomicFloat

Provides an atomic wrapper for safe concurrent access to a float value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicFloat--><!--Device-unnamed-export class AtomicFloat-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: float, val: float): float
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-compareAndSwap(expected: float, val: float): float--><!--Device-AtomicFloat-compareAndSwap(expected: float, val: float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | float | 是 | the expected current value. |
| val | float | 是 | the new value to store if the comparison succeeds. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the previous value |

## constructor

```TypeScript
constructor(val: float)
```

Constructs a new AtomicFloat with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-constructor(val: float)--><!--Device-AtomicFloat-constructor(val: float)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | the initial value. |

## exchange

```TypeScript
exchange(val: float): float
```

Atomically exchanges the current value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-exchange(val: float): float--><!--Device-AtomicFloat-exchange(val: float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | the new value to exchange with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the previous value |

## fetchAdd

```TypeScript
fetchAdd(val: float): float
```

Atomically adds a value to the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-fetchAdd(val: float): float--><!--Device-AtomicFloat-fetchAdd(val: float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | the value to add. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the previous value before the addition |

## fetchSub

```TypeScript
fetchSub(val: float): float
```

Atomically subtracts a value from the current value and returns the previous value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-fetchSub(val: float): float--><!--Device-AtomicFloat-fetchSub(val: float): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | the value to subtract. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the previous value before the subtraction |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-static isLockFree(): boolean--><!--Device-AtomicFloat-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): float
```

Atomically loads the current value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-load(): float--><!--Device-AtomicFloat-load(): float-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| float | the current value |

## store

```TypeScript
store(val: float): void
```

Atomically stores a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicFloat-store(val: float): void--><!--Device-AtomicFloat-store(val: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | float | 是 | the new value to store. |

