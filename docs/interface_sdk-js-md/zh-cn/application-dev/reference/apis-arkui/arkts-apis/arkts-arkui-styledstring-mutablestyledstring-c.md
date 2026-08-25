# MutableStyledString

继承于[StyledString](arkts-arkui-styledstring-styledstring-c.md)类。

> **以下接口异常入参处理统一说明：**&gt;
> 当start和length越界或者必填传入undefined时，会抛出异常；&gt;
> 当styledKey和styledValue传入异常值或者两者对应关系不匹配时，会抛出异常。

**继承/实现关系：** MutableStyledString extends [StyledString](arkts-arkui-styledstring-styledstring-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## appendStyledString

```TypeScript
appendStyledString(other: StyledString): void
```

在末尾位置追加新的属性字符串。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | 是 |

## clearStyles

```TypeScript
clearStyles(): void
```

清除属性字符串对象的所有样式。被清空样式类型对象属性使用的是对应Text组件属性的设置值，若Text组件未设置值， 则使用对应Text组件属性的默认值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)
```

可变属性字符串的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [ImageAttachment](arkts-arkui-styledstring-imageattachment-c.md) \| [CustomSpan](arkts-arkui-styledstring-customspan-c.md) | 是 |
| styles | Array&lt;[StyleOptions](arkts-arkui-styledstring-styleoptions-i.md)&gt; | 否 |

## insertString

```TypeScript
insertString(start: int, other: string): void
```

插入字符串。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| other | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## insertStyledString

```TypeScript
insertStyledString(start: int, other: StyledString): void
```

在指定位置插入新的属性字符串。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| other | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## removeString

```TypeScript
removeString(start: int, length: int): void
```

移除指定范围的字符串。当属性字符串中包含图片或[CustomSpan](arkts-arkui-styledstring-customspan-c.md)时，同样生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| length | int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## removeStyle

```TypeScript
removeStyle(start: int, length: int, styledKey: StyledStringKey): void
```

清除指定范围内容的指定类型样式。被清空样式类型对象属性使用的是对应Text组件属性的设置值，若Text组件未设置值， 则使用对应Text组件属性的默认值。当属性字符串中包含图片时，同样生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| length | int | 是 |
| styledKey | [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## removeStyles

```TypeScript
removeStyles(start: int, length: int): void
```

清除指定范围内容的所有样式。被清空样式类型对象属性使用的是对应Text组件属性的设置值，若Text组件未设置值， 则使用对应Text组件属性的默认值。当属性字符串中包含图片时，同样生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| length | int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## replaceString

```TypeScript
replaceString(start: int, length: int, other: string): void
```

替换指定范围的字符串。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| length | int | 是 |
| other | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## replaceStyle

```TypeScript
replaceStyle(spanStyle: SpanStyle): void
```

替换指定范围内容为指定类型新样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-styledstring-spanstyle-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## replaceStyledString

```TypeScript
replaceStyledString(start: int, length: int, other: StyledString): void
```

替换指定范围为新的属性字符串。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | int | 是 |
| length | int | 是 |
| other | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setStyle

```TypeScript
setStyle(spanStyle: SpanStyle): void
```

为指定范围内容设置指定类型新样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-styledstring-spanstyle-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
