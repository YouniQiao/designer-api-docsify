# PromiseFulfilledResult

Represents the result of a fulfilled promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class PromiseFulfilledResult<T>--><!--Device-unnamed-export class PromiseFulfilledResult<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs an empty PromiseFulfilledResult.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseFulfilledResult-constructor()--><!--Device-PromiseFulfilledResult-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(value: T)
```

Constructs a PromiseFulfilledResult with the given value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseFulfilledResult-constructor(value: T)--><!--Device-PromiseFulfilledResult-constructor(value: T)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | the fulfilled value. |

## status

```TypeScript
status: string
```

The status of the promise.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseFulfilledResult-status: string--><!--Device-PromiseFulfilledResult-status: string-End-->

**系统能力：** SystemCapability.Utils.Lang

## value

```TypeScript
value: T
```

The value of the fulfilled promise.

**类型：** T

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseFulfilledResult-value: T--><!--Device-PromiseFulfilledResult-value: T-End-->

**系统能力：** SystemCapability.Utils.Lang

