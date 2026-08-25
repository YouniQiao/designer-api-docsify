# JsonParseError

JSON解析失败时抛出的错误。

**继承/实现关系：** JsonParseError extends [SyntaxError](arkts-arkts-errors-syntaxerror-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| start_offset | int | 否 |
| end_offset | int | 否 |

**返回值：**

| 类型 |
| --- |
| [JsonParseError](arkts-arkts-json-jsonparseerror-c.md) |

## constructor

```TypeScript
public constructor(message?: string, options?: ErrorOptions)
```

用于创建JsonParseError的构造函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | string | 否 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |
