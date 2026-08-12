# RichEditorController

RichEditor组件的控制器，继承自[RichEditorBaseController](arkts-arkui-richeditorbasecontroller-c.md#RichEditorBaseController)。

> **说明：**
> 
> 当内容的长度超过组件显示区域的高度时，调用插入接口（例如[addTextSpan](#addTextSpan)、
> [addImageSpan](#addImageSpan)、[addBuilderSpan](#addBuilderSpan)
> 、[addSymbolSpan](#addSymbolSpan)），组件会自动滚动内容使得插入内容末尾可见。

## 导入对象

```ts controller: RichEditorController = new RichEditorController();```

**继承/实现关系：** RichEditorController extends [RichEditorBaseController](arkts-arkui-richeditorbasecontroller-c.md#RichEditorBaseController)

**起始版本：** 10

<!--Device-unnamed-declare class RichEditorController extends RichEditorBaseController--><!--Device-unnamed-declare class RichEditorController extends RichEditorBaseController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addBuilderSpan

```TypeScript
addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number
```

在RichEditor中添加用户自定义布局（BuilderSpan）。

> **说明：**
> 
> - RichEditor组件添加占位Span，占位Span调用系统的measure方法计算真实的长宽和位置。
> 
> - 可通过[RichEditorBuilderSpanOptions](arkts-arkui-richeditorbuilderspanoptions-i.md#RichEditorBuilderSpanOptions)设置此builder在RichEditor中的index（一个文字为一个单位）。
> 
> - 此占位Span不可获焦，支持拖拽，支持部分通用属性，占位、删除等能力等同于ImageSpan，长度视为一个文字。
> 
> - 支持通过[bindSelectionMenu](RichEditorAttribute#bindSelectionMenu)设置自定义菜单。
> 
> - 不支持通过[getSpans](#getSpans)，[getSelection](#getSelection)，
> [onSelect](RichEditorAttribute#onSelect)，[aboutToDelete](RichEditorAttribute#aboutToDelete)获取
> builderSpan信息。
> 
> - 不支持通过[updateSpanStyle](#updateSpanStyle)，
> [updateParagraphStyle](#updateParagraphStyle)等方式更新builder。
> 
> - 对此builder节点进行复制或粘贴不生效。
> 
> - builder的布局约束由RichEditor传入，如果builder里最外层组件不设置大小，则会用RichEditor的大小作为maxSize。
> 
> - builder的手势相关事件机制与通用手势事件相同，如果builder中未设置透传，则仅有builder中的子组件响应。
> 
> - 如果组件光标闪烁，插入后光标位置更新为新插入builder的后面。
> 
> - 对[addBuilderSpan](#addBuilderSpan)的节点文本，
> [enableDataDetector](RichEditorAttribute#enableDataDetector)、
> [dataDetectorConfig](RichEditorAttribute#dataDetectorConfig)、
> [enableSelectedDataDetector](RichEditorAttribute#enableSelectedDataDetector)功能不会生效。
> 通用属性仅支持[size](CommonMethod#size)、[padding](CommonMethod#padding)、[margin](CommonMethod#margin)、
> [aspectRatio](arkts-arkui-commonmethod-c.md#aspectRatio)、[borderStyle](CommonMethod#borderStyle)、
> [borderWidth](CommonMethod#borderWidth)、[borderColor](CommonMethod#borderColor)、
> [borderRadius](CommonMethod#borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses))、
> [backgroundColor](CommonMethod#backgroundColor(value: ResourceColor))、
> [backgroundBlurStyle](CommonMethod#backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions))
> 、[opacity](CommonMethod#opacity(value: number | Resource))、
> [blur](CommonMethod#blur(value: number, options?: BlurOptions))、
> [backdropBlur](arkts-arkui-commonmethod-c.md#backdropBlur)、
> [shadow](CommonMethod#shadow(value: ShadowOptions | ShadowStyle))、
> [grayscale](CommonMethod#grayscale(value: number))、
> [brightness](CommonMethod#brightness(value: number))、[saturate](arkts-arkui-commonmethod-c.md#saturate)
> 、[contrast](CommonMethod#contrast(value: number))、
> [invert](CommonMethod#invert(value: number | InvertOptions))、
> [sepia](arkts-arkui-commonmethod-c.md#sepia)、
> [hueRotate](arkts-arkui-commonmethod-c.md#hueRotate)、
> [colorBlend](arkts-arkui-commonmethod-c.md#colorBlend)、
> [linearGradientBlur](arkts-arkui-commonmethod-c.md#linearGradientBlur)、
> [clip](CommonMethod#clip(value: boolean))、[mask](CommonMethod#mask(value: ProgressMask))、
> [foregroundBlurStyle](arkts-arkui-commonmethod-c.md#foregroundBlurStyle)
> 、[accessibilityGroup](CommonMethod#accessibilityGroup(value: boolean))、
> [accessibilityText](CommonMethod#accessibilityText(value: string))、
> [accessibilityDescription](CommonMethod#accessibilityDescription(value: string))、
> [accessibilityLevel](CommonMethod#accessibilityLevel)、
> [sphericalEffect](arkts-arkui-commonmethod-c.md#sphericalEffect)、
> [lightUpEffect](arkts-arkui-commonmethod-c.md#lightUpEffect)、
> [pixelStretchEffect](arkts-arkui-commonmethod-c.md#pixelStretchEffect)。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number--><!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| options | [RichEditorBuilderSpanOptions](arkts-arkui-richeditorbuilderspanoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## addImageSpan

```TypeScript
addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number
```

添加图片内容。如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

该接口为同步接口，在弱网环境下，直接添加网络图片可能会阻塞UI线程造成冻屏问题。不建议直接添加网络图片。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number--><!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 是 |
| options | [RichEditorImageSpanOptions](arkts-arkui-richeditorimagespanoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## addSymbolSpan

```TypeScript
addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number
```

在RichEditor中添加图标小符号（SymbolSpan）。如果组件光标闪烁，插入后光标位置更新为新插入SymbolSpan的后面。

SymbolSpan暂不支持手势、复制操作和拖拽处理。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number--><!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| options | [RichEditorSymbolSpanOptions](arkts-arkui-richeditorsymbolspanoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## addTextSpan

```TypeScript
addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number
```

添加文本内容。如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number--><!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 是 |
| options | [RichEditorTextSpanOptions](arkts-arkui-richeditortextspanoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## deleteSpans

```TypeScript
deleteSpans(value?: RichEditorRange): void
```

删除指定范围内的文本和图片。当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void--><!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | 否 |

## fromStyledString

```TypeScript
fromStyledString(value: StyledString): Array<RichEditorSpan>
```

将属性字符串转换为span信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan>--><!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[RichEditorSpan](arkts-arkui-richeditorspan-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## getParagraphs

```TypeScript
getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>
```

获取指定范围的段落信息。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>--><!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[RichEditorParagraphResult](arkts-arkui-richeditorparagraphresult-i.md)&gt; |

## getSelection

```TypeScript
getSelection(): RichEditorSelection
```

获取选中内容的范围和span信息。未选中时，返回光标所在span信息。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-getSelection(): RichEditorSelection--><!--Device-RichEditorController-getSelection(): RichEditorSelection-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RichEditorSelection](arkts-arkui-richeditorselection-i.md) |

## getSpans

```TypeScript
getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>
```

获取span信息。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>--><!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[RichEditorImageSpanResult](arkts-arkui-richeditorimagespanresult-i.md) \| [RichEditorTextSpanResult](arkts-arkui-richeditortextspanresult-i.md)&gt; |

## toStyledString

```TypeScript
toStyledString(value: RichEditorRange): StyledString
```

将给定范围的组件内容转换成属性字符串，SymbolSpan和BuilderSpan不支持转换。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString--><!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## updateParagraphStyle

```TypeScript
updateParagraphStyle(value: RichEditorParagraphStyleOptions): void
```

更新段落的样式。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void--><!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorParagraphStyleOptions](arkts-arkui-richeditorparagraphstyleoptions-i.md) | 是 |

## updateSpanStyle

```TypeScript
updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void
```

更新文本、图片或SymbolSpan样式。

若只更新了一个Span的部分内容，则会根据更新部分、未更新部分将该Span拆分为多个Span。当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

使用该接口更新文本、图片或SymbolSpan样式时默认不会关闭自定义文本选择菜单。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void--><!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorUpdateTextSpanStyleOptions](arkts-arkui-richeditorupdatetextspanstyleoptions-i.md) \| [RichEditorUpdateImageSpanStyleOptions](arkts-arkui-richeditorupdateimagespanstyleoptions-i.md) \| [RichEditorUpdateSymbolSpanStyleOptions](arkts-arkui-richeditorupdatesymbolspanstyleoptions-i.md) | 是 |
