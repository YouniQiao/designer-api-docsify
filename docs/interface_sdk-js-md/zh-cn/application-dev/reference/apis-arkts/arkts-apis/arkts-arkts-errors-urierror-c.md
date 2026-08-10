# URIError

Represents an error that occurs when a global URI handling function was used in a wrong way

**继承/实现关系：** URIError extends [Error](arkts-arkts-error-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class URIError extends Error--><!--Device-unnamed-export class URIError extends Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): URIError
```

Constructs a new URIError instance with provided message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-URIError-static $_invoke(message?: string, options?: ErrorOptions): URIError--><!--Device-URIError-static $_invoke(message?: string, options?: ErrorOptions): URIError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [URIError](arkts-arkts-errors-urierror-c.md) | Newly created URIError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new URIError instance with provided message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-URIError-constructor(message?: string, options?: ErrorOptions)--><!--Device-URIError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

