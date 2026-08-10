# AtomicBoolean

Provides an atomic wrapper for safe concurrent access to a boolean value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AtomicBoolean--><!--Device-unnamed-export class AtomicBoolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareAndSwap

```TypeScript
compareAndSwap(expected: boolean, val: boolean): boolean
```

Atomically compares the current value with the expected value and replaces it if equal

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicBoolean-compareAndSwap(expected: boolean, val: boolean): boolean--><!--Device-AtomicBoolean-compareAndSwap(expected: boolean, val: boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| expected | boolean | 是 | the expected current value. |
| val | boolean | 是 | the new value to store if the comparison succeeds. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | the previous value |

## constructor

```TypeScript
constructor(val: boolean)
```

Constructs a new AtomicBoolean with the provided initial value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicBoolean-constructor(val: boolean)--><!--Device-AtomicBoolean-constructor(val: boolean)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | boolean | 是 | the initial value. |

## exchange

```TypeScript
exchange(val: boolean): boolean
```

Atomically exchanges the current value with a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicBoolean-exchange(val: boolean): boolean--><!--Device-AtomicBoolean-exchange(val: boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | boolean | 是 | the new value to exchange with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | the previous value |

## isLockFree

```TypeScript
static isLockFree(): boolean
```

Checks whether atomic operations on this type are lock-free

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicBoolean-static isLockFree(): boolean--><!--Device-AtomicBoolean-static isLockFree(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if atomic operations are lock-free, false otherwise |

## load

```TypeScript
load(): boolean
```

Atomically loads the current value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicBoolean-load(): boolean--><!--Device-AtomicBoolean-load(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | the current value |

## store

```TypeScript
store(val: boolean): void
```

Atomically stores a new value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AtomicBoolean-store(val: boolean): void--><!--Device-AtomicBoolean-store(val: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | boolean | 是 | the new value to store. |

