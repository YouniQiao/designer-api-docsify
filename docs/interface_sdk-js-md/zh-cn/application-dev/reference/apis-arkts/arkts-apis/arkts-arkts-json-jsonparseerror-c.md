# JsonParseError

Error thrown when parsing JSON fails.

**继承/实现关系：** JsonParseError extends [SyntaxError](arkts-arkts-errors-syntaxerror-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class JsonParseError extends SyntaxError--><!--Device-unnamed-export class JsonParseError extends SyntaxError-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError
```

Creates a JsonParseError with location information.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonParseError-static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError--><!--Device-JsonParseError-static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | Error message |
| start_offset | int | 否 | Start offset in the source string &lt;br&gt;The value should be an integer. |
| end_offset | int | 否 | End offset in the source string &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonParseError](arkts-arkts-json-jsonparseerror-c.md) | The created JsonParseError |

## constructor

```TypeScript
public constructor(message?: string, options?: ErrorOptions)
```

Constructor for creating a JsonParseError.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonParseError-public constructor(message?: string, options?: ErrorOptions)--><!--Device-JsonParseError-public constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

