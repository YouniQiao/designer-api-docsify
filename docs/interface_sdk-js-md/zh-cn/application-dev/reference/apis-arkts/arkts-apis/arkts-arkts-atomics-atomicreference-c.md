# AtomicReference

Provides an atomic reference wrapper for safe concurrent access to a reference value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicReference<T>--><!--Device-unnamed-export class AtomicReference<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: T, ref: T): T
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicReference-compareAndSwap(expected: T, ref: T): T--><!--Device-AtomicReference-compareAndSwap(expected: T, ref: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | T | 是 | the expected current value. |
| ref | T | 是 | the new reference value to store if the comparison succeeds. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | the previous reference value |

## constructor

```TypeScript
constructor(ref: T)
```

Constructs a new AtomicReference with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicReference-constructor(ref: T)--><!--Device-AtomicReference-constructor(ref: T)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ref | T | 是 | the initial reference value. |

## exchange

```TypeScript
exchange(ref: T): T
```

Atomically exchanges the current reference value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicReference-exchange(ref: T): T--><!--Device-AtomicReference-exchange(ref: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ref | T | 是 | the new reference value to exchange with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | the previous reference value |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicReference-static isLockFree(): boolean--><!--Device-AtomicReference-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): T
```

Atomically loads the current reference value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicReference-load(): T--><!--Device-AtomicReference-load(): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | the current reference value |

## store

```TypeScript
store(ref: T): void
```

Atomically stores a new reference value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicReference-store(ref: T): void--><!--Device-AtomicReference-store(ref: T): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ref | T | 是 | the new reference value to store. |

