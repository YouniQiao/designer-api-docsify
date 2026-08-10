# PromiseRejectedResult

Represents the result of a rejected promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class PromiseRejectedResult--><!--Device-unnamed-export class PromiseRejectedResult-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

Constructs a PromiseRejectedResult with a default error.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseRejectedResult-constructor()--><!--Device-PromiseRejectedResult-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(reason: Error)
```

Constructs a PromiseRejectedResult with the given reason.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseRejectedResult-constructor(reason: Error)--><!--Device-PromiseRejectedResult-constructor(reason: Error)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | Error | 是 | the rejection reason. |

## reason

```TypeScript
reason: Error
```

The reason the promise was rejected.

**类型：** Error

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseRejectedResult-reason: Error--><!--Device-PromiseRejectedResult-reason: Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## status

```TypeScript
status: string
```

The status of the promise.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseRejectedResult-status: string--><!--Device-PromiseRejectedResult-status: string-End-->

**系统能力：** SystemCapability.Utils.Lang

