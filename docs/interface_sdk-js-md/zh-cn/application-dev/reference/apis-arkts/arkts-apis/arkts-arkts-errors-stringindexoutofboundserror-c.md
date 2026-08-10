# StringIndexOutOfBoundsError

Represents error that is thrown when provided string index is out of bounds

**继承/实现关系：** StringIndexOutOfBoundsError extends [RangeError](arkts-arkts-errors-rangeerror-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class StringIndexOutOfBoundsError extends RangeError--><!--Device-unnamed-export class StringIndexOutOfBoundsError extends RangeError-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new StringIndexOutOfBoundsError instance with provided message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)--><!--Device-StringIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

