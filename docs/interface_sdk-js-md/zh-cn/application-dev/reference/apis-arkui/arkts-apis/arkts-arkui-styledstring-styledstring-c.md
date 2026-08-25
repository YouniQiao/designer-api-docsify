# StyledString

属性字符串

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)
```

属性字符串的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [ImageAttachment](arkts-arkui-styledstring-imageattachment-c.md) \| [CustomSpan](arkts-arkui-styledstring-customspan-c.md) | 是 |
| styles | Array&lt;[StyleOptions](arkts-arkui-styledstring-styleoptions-i.md)&gt; | 否 |

## equals

```TypeScript
equals(other: StyledString): boolean
```

判断两个属性字符串是否相等。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## fromHtml

```TypeScript
static fromHtml(html: string): Promise<StyledString | undefined>
```

将HTML格式字符串转换成属性字符串，使用Promise异步回调。当前支持转换的HTML标签范围：\<p>、\&lt;span&gt;、\&lt;img&gt;、\、\&lt;strong&gt;、\&lt;b&gt;、\&lt;a&gt;、\&lt;i&gt;、\&lt;em&gt;、\&lt;s&gt;、\&lt;u&gt;、\&lt;del&gt;、\&lt;sup&gt;、\&lt;sub&gt;、\&lt;cite&gt;、\&lt;dfn&gt;、\&lt;small&gt;、\&lt;h1&gt;、\&lt;h2&gt;、\&lt;h3&gt;、\&lt;h4&gt;、\&lt;h5&gt;、\

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| html | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-styledstring-c.md) \| undefined & gt; |

**错误码：**

| 错误码ID |
| --- |
| [170001](../errorcode-styled-string.md#170001-转换错误) |

## getString

```TypeScript
getString(): string
```

获取字符串信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getStyles

```TypeScript
getStyles(start: int, length: int, styledKey?: StyledStringKey): Array<SpanStyle> | undefined
```

获取指定范围属性字符串的样式集合。不能超出属性字符串的长度。该接口仅返回开发者设置的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| [length](#length) | int | 是 |
| styledKey | [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[SpanStyle](arkts-arkui-styledstring-spanstyle-i.md)&gt; \| undefined |

## subStyledString

```TypeScript
subStyledString(start: int, length?: int): StyledString | undefined
```

获取属性字符串的子属性字符串。不能超出属性字符串的长度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| [length](#length) | int | 否 |

**返回值：**

| 类型 |
| --- |
| [StyledString](arkts-arkui-styledstring-styledstring-c.md) \| undefined |

## toHtml

```TypeScript
static toHtml(styledString: StyledString): string
```

将属性字符串转换成HTML格式字符串。支持转换的属性字符串[StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md)包括：StyledStringKey.FONT、 StyledStringKey.DECORATION、StyledStringKey.LETTER_SPACING、StyledStringKey.TEXT_SHADOW、StyledStringKey.LINE_HEIGHT 、StyledStringKey.IMAGE。使用方法参考 示例12（fromHtml和toHtml互相转换）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## length

```TypeScript
get length(): int
```

获取属性字符串内容长度。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
