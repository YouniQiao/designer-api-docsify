# MutableStyledString

继承于[StyledString](arkts-arkui-styledstring-styledstring-c.md)类。

> **以下接口异常入参处理统一说明：**
> 
> 当start和length越界或者必填传入undefined时，会抛出异常；
> 
> 当styledKey和styledValue传入异常值或者两者对应关系不匹配时，会抛出异常。

**Inheritance/Implementation:** MutableStyledString extends [StyledString](arkts-arkui-styledstring-styledstring-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class MutableStyledString extends StyledString--><!--Device-unnamed-export declare class MutableStyledString extends StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## appendStyledString

```TypeScript
appendStyledString(other: StyledString): void
```

在末尾位置追加新的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-appendStyledString(other: StyledString): void--><!--Device-MutableStyledString-appendStyledString(other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes | 新的属性字符串对象。 |

## clearStyles

```TypeScript
clearStyles(): void
```

清除属性字符串对象的所有样式。

被清空样式类型对象属性使用的是对应[Text](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-clearStyles(): void--><!--Device-MutableStyledString-clearStyles(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)
```

可变属性字符串的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)--><!--Device-MutableStyledString-constructor(value: string | ImageAttachment | CustomSpan, styles?: Array<StyleOptions>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| ImageAttachment \| CustomSpan | Yes | 属性字符串文本内容。&lt;br/&gt;**说明：** &lt;br/&gt;当value的类型为ImageAttachment或 CustomSpan时，styles参数不生效。&lt;br/&gt;需要设置styles时，通过[setStyle](arkts-arkui-styledstring-mutablestyledstring-c.md#setstyle)等方法实现。 |
| styles | Array&lt;StyleOptions&gt; | No | 属性字符串初始化选项。&lt;br/&gt;**说明：** &lt;br/&gt;start为异常值时，按默认值0处理；&lt;br/&gt;当length为异常值时， length等于属性字符串在start后的实际长度；&lt;br/&gt;当StyledStringKey与StyledStringValue不匹配时，styles不生效。 |

## insertString

```TypeScript
insertString(start: int, other: string): void
```

插入字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-insertString(start: int, other: string): void--><!--Device-MutableStyledString-insertString(start: int, other: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 插入位置的下标。&lt;br/&gt;取值范围：大于等于0。 |
| other | string | Yes | 插入的新文本内容。&lt;br/&gt;**说明：** &lt;br/&gt;插入的字符串使用的是start-1位置字符的样式。若start-1位置字符未设置样式，则使用start位置字符样式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## insertStyledString

```TypeScript
insertStyledString(start: int, other: StyledString): void
```

在指定位置插入新的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-insertStyledString(start: int, other: StyledString): void--><!--Device-MutableStyledString-insertStyledString(start: int, other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 开始插入位置的下标。&lt;br/&gt;取值范围：大于等于0。 |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes | 新的属性字符串对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## removeString

```TypeScript
removeString(start: int, length: int): void
```

移除指定范围的字符串。

当属性字符串中包含图片或[CustomSpan](arkts-arkui-styledstring-customspan-c.md)时，同样生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-removeString(start: int, length: int): void--><!--Device-MutableStyledString-removeString(start: int, length: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 指定范围的下标。&lt;br/&gt;取值范围：大于等于0。 |
| length | int | Yes | 指定范围的长度。&lt;br/&gt;取值范围：大于等于0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## removeStyle

```TypeScript
removeStyle(start: int, length: int, styledKey: StyledStringKey): void
```

清除指定范围内容的指定类型样式。

被清空样式类型对象属性使用的是对应[Text](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

当属性字符串中包含图片时，同样生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-removeStyle(start: int, length: int, styledKey: StyledStringKey): void--><!--Device-MutableStyledString-removeStyle(start: int, length: int, styledKey: StyledStringKey): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 指定范围开始位置的下标。&lt;br/&gt;取值范围：大于等于0。 |
| length | int | Yes | 指定范围的长度。&lt;br/&gt;取值范围：大于等于0。 |
| styledKey | [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md) | Yes | 样式类型枚举值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## removeStyles

```TypeScript
removeStyles(start: int, length: int): void
```

清除指定范围内容的所有样式。

被清空样式类型对象属性使用的是对应[Text](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md)组件属性的设置值，若Text组件未设置值，则使用对应Text组件属性的默认值。

当属性字符串中包含图片时，同样生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-removeStyles(start: int, length: int): void--><!--Device-MutableStyledString-removeStyles(start: int, length: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 指定范围开始位置的下标。&lt;br/&gt;取值范围：大于等于0。 |
| length | int | Yes | 指定范围的长度。&lt;br/&gt;取值范围：大于等于0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## replaceString

```TypeScript
replaceString(start: int, length: int, other: string): void
```

替换指定范围的字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-replaceString(start: int, length: int, other: string): void--><!--Device-MutableStyledString-replaceString(start: int, length: int, other: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 指定范围的下标。&lt;br/&gt;取值范围：大于等于0。 |
| length | int | Yes | 指定范围的长度。&lt;br/&gt;取值范围：大于等于0。 |
| other | string | Yes | 替换的新文本内容。&lt;br/&gt;**说明：** &lt;br/&gt;替换的字符串使用的是start位置字符的样式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## replaceStyle

```TypeScript
replaceStyle(spanStyle: SpanStyle): void
```

替换指定范围内容为指定类型新样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-replaceStyle(spanStyle: SpanStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-styledstring-spanstyle-i.md) | Yes | 样式对象。&lt;br/&gt;**说明：** &lt;br/&gt;默认清空原有样式，替换为新样式。&lt;br/&gt;当SpanStyle的styledKey为IMAGE或 CUSTOM_SPAN时，只有当start的位置当前是image或CustomSpan且长度为1，才会生效，其余情况无效果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## replaceStyledString

```TypeScript
replaceStyledString(start: int, length: int, other: StyledString): void
```

替换指定范围为新的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-replaceStyledString(start: int, length: int, other: StyledString): void--><!--Device-MutableStyledString-replaceStyledString(start: int, length: int, other: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 指定范围开始位置的下标。&lt;br/&gt;取值范围：大于等于0。 |
| length | int | Yes | 指定范围的长度。&lt;br/&gt;取值范围：大于等于0。 |
| other | [StyledString](arkts-arkui-styledstring-c.md) | Yes | 新的属性字符串对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## setStyle

```TypeScript
setStyle(spanStyle: SpanStyle): void
```

为指定范围内容设置指定类型新样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void--><!--Device-MutableStyledString-setStyle(spanStyle: SpanStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanStyle | [SpanStyle](arkts-arkui-styledstring-spanstyle-i.md) | Yes | 样式对象。&lt;br/&gt;默认不清空原有样式，叠加新样式。如果StyledStringValue类型相同，则新样式将覆盖旧样式。&lt;br/&gt;当SpanStyle的 styledKey为IMAGE或CUSTOM_SPAN时，只有当start的位置当前是image或CustomSpan且长度为1，才会生效，其余情况无效果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. |

