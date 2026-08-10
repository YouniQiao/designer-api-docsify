# IllegalArgumentError

Represents an error thrown when a method is passed an illegal argument.

**继承/实现关系：** IllegalArgumentError extends [Error](arkts-arkts-error-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class IllegalArgumentError extends Error--><!--Device-unnamed-export class IllegalArgumentError extends Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an IllegalArgumentError instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IllegalArgumentError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IllegalArgumentError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | The error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options, usually containing the error stack information. |

