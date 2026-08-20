# JsonParseError

JSON解析失败时抛出的错误。

**继承/实现关系：** JsonParseError extends [SyntaxError](arkts-arkts-errors-syntaxerror-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class JsonParseError--><!--Device-unnamed-export class JsonParseError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError
```

创建带位置信息的JsonParseError。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonParseError-static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError--><!--Device-JsonParseError-static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 错误信息。 |
| start_offset | int | 否 | 在源字符串中的起始偏移量。 <br>取值约束：应为整数。 |
| end_offset | int | 否 | 在源字符串中的结束偏移量。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonParseError](arkts-arkts-json-jsonparseerror-c.md) | 创建得到的JsonParseError。 |

## constructor

```TypeScript
public constructor(message?: string, options?: ErrorOptions)
```

用于创建JsonParseError的构造函数。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonParseError-public constructor(message?: string, options?: ErrorOptions)--><!--Device-JsonParseError-public constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误信息。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

