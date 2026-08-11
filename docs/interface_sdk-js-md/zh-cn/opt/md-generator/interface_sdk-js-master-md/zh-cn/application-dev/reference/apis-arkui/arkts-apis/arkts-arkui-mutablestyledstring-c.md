# MutableStyledString

继承于[StyledString](arkts-arkui-styledstring-c.md)类。

> **以下接口异常入参处理统一说明：**
> 
> 当start和length越界或者必填传入undefined时，会抛出异常；
> 
> 当styledKey和styledValue传入异常值或者两者对应关系不匹配时，会抛出异常。

**继承/实现关系：** MutableStyledString extends [StyledString](arkts-arkui-styledstring-c.md)

**起始版本：** 12

<!--Device-unnamed-declare class MutableStyledString extends StyledString--><!--Device-unnamed-declare class MutableStyledString extends StyledString-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## appendStyledString

```TypeScript
appendStyledString(other: StyledString): void
```

在末尾位置追加新的属性字符串。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-appendStyledString(other: StyledString): void--><!--Device-MutableStyledString-appendStyledString(other: StyledString): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-c.md) | 是 |

## clearStyles

```TypeScript
clearStyles(): void
```

清除属性字符串对象的所有样式。

被清空样式类型对象属性使用的是对应[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-clearStyles(): void--><!--Device-MutableStyledString-clearStyles(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## insertString

```TypeScript
insertString(start: number, other: string): void
```

插入字符串。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-insertString(start: number, other: string): void--><!--Device-MutableStyledString-insertString(start: number, other: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| other | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## insertStyledString

```TypeScript
insertStyledString(start: number, other: StyledString): void
```

在指定位置插入新的属性字符串。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-insertStyledString(start: number, other: StyledString): void--><!--Device-MutableStyledString-insertStyledString(start: number, other: StyledString): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| other | [StyledString](arkts-arkui-styledstring-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## removeString

```TypeScript
removeString(start: number, length: number): void
```

移除指定范围的字符串。

当属性字符串中包含图片或[CustomSpan](arkts-arkui-customspan-c.md)时，同样生效。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-removeString(start: number, length: number): void--><!--Device-MutableStyledString-removeString(start: number, length: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| length | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## removeStyle

```TypeScript
removeStyle(start: number, length: number, styledKey: StyledStringKey): void
```

清除指定范围内容的指定类型样式。

被清空样式类型对象属性使用的是对应[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

当属性字符串中包含图片时，同样生效。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-removeStyle(start: number, length: number, styledKey: StyledStringKey): void--><!--Device-MutableStyledString-removeStyle(start: number, length: number, styledKey: StyledStringKey): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| length | number | 是 |
| styledKey | [StyledStringKey](arkts-arkui-styledstringkey-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## removeStyles

```TypeScript
removeStyles(start: number, length: number): void
```

清除指定范围内容的所有样式。

被清空样式类型对象属性使用的是对应[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

当属性字符串中包含图片时，同样生效。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-removeStyles(start: number, length: number): void--><!--Device-MutableStyledString-removeStyles(start: number, length: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| length | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## replaceString

```TypeScript
replaceString(start: number, length: number, other: string): void
```

替换指定范围的字符串。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-replaceString(start: number, length: number, other: string): void--><!--Device-MutableStyledString-replaceString(start: number, length: number, other: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| length | number | 是 |
| other | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## replaceStyle

```TypeScript
replaceStyle(spanStyle: SpanStyle): void
```

替换指定范围内容为指定类型新样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-spanstyle-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## replaceStyledString

```TypeScript
replaceStyledString(start: number, length: number, other: StyledString): void
```

替换指定范围为新的属性字符串。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-replaceStyledString(start: number, length: number, other: StyledString): void--><!--Device-MutableStyledString-replaceStyledString(start: number, length: number, other: StyledString): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| length | number | 是 |
| other | [StyledString](arkts-arkui-styledstring-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## setStyle

```TypeScript
setStyle(spanStyle: SpanStyle): void
```

为指定范围内容设置指定类型新样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-spanstyle-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
