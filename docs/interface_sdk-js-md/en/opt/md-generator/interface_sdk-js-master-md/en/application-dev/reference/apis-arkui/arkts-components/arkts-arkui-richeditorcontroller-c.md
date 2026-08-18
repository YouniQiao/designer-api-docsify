# RichEditorController

Implements the **RichEditor** component controller. Inherits from [RichEditorBaseController](arkts-arkui-richeditorbasecontroller-c.md#richeditorbasecontroller). > **NOTE：**> > When the length of the content exceeds the height of the display area of the component, the insertion interface ( > such as [addTextSpan](#addtextspan), > [addImageSpan](#addimagespan), > [addBuilderSpan](#addbuilderspan) and > [addSymbolSpan](#addsymbolspan)) is called. The component automatically scrolls the > content to make the end of the inserted content visible.

**Inheritance/Implementation:** RichEditorController extends [RichEditorBaseController](arkts-arkui-richeditorbasecontroller-c.md#richeditorbasecontroller)

**Since:** 10

<!--Device-unnamed-declare class RichEditorController--><!--Device-unnamed-declare class RichEditorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addBuilderSpan

```TypeScript
addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number
```

Adds a custom layout (BuilderSpan) to **RichEditor**. > **NOTE：**> > - This API adds a builder span to take up space in the layout. It calls the system **measure** method to > calculate the actual length, width, and position. > > - You can use [RichEditorBuilderSpanOptions](arkts-arkui-richeditorbuilderspanoptions-i.md#richeditorbuilderspanoptions) to set the index of the builder > in the **RichEditor** component (with one character as the unit). > > - This builder span is unfocusable, draggable, and equipped with certain universal attributes. It behaves > similarly to an image span in terms of placeholder and deletion functionality, and it is treated as a single > character in length. > > - Custom menus can be set using bindSelectionMenu. > > - The information about the builder span cannot be obtained through > [getSpans](#getspans), [getSelection](#getselection), > onSelect, or aboutToDelete. > > - The builder span cannot be updated using [updateSpanStyle](#updatespanstyle) or > [updateParagraphStyle](#updateparagraphstyle). > > - Copying or pasting the builder span does not take effect. > > - The layout constraints of the builder span are passed in from the **RichEditor** component. If the size of the > outermost component in the builder span is not set, the size of the **RichEditor** is used as the value of > **maxSize**. > > - The gesture event mechanism of the builder span is the same as the universal gesture event mechanism. If > transparent transmission is not set in the builder, only the child components in the builder respond. > > - If the caret in the component is blinking, the caret position is updated to be after the inserted image span. Only the following universal attributes are supported: [size](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#size), [padding](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#padding), [margin](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#margin), [aspectRatio](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-layout-constraints.md#aspectratio), [borderStyle](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md#borderstyle), [borderWidth](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md#borderwidth), [borderColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md#bordercolor), [borderRadius](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md#borderradius), [backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor), [backgroundBlurStyle](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundblurstyle9) , opacity, [blur](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#blur), [backdropBlur](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backdropblur), [shadow](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#shadow), [grayscale](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#grayscale), [brightness](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#brightness), [saturate](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#saturate), [contrast](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#contrast), [invert](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#invert), [sepia](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#sepia), [hueRotate](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#huerotate), [colorBlend](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#colorblend), [linearGradientBlur](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#lineargradientblur12) , [clip](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-sharp-clipping.md#clip12), [mask](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-sharp-clipping.md#mask12), [foregroundBlurStyle](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle) , [accessibilityGroup](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitygroup) , [accessibilityText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitytext) , [accessibilityDescription](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitydescription) , [accessibilityLevel](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-accessibility.md#accessibilitylevel) , [sphericalEffect](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#sphericaleffect12) , [lightUpEffect](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#lightupeffect12), [pixelStretchEffect](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-image-effect.md#pixelstretcheffect12) .

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number--><!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [RichEditorBuilderSpanOptions](arkts-arkui-richeditorbuilderspanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## addImageSpan

```TypeScript
addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number
```

Adds an image span. If the caret in the component is blinking, the caret position is updated to be after the inserted image span. This API is a synchronous API. In a weak network environment, directly adding network images may block the UI thread and cause screen freezing. To avoid potential loading issues, do not directly add a network image.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number--><!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | PixelMap \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| options | [RichEditorImageSpanOptions](arkts-arkui-richeditorimagespanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## addSymbolSpan

```TypeScript
addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number
```

Adds a symbol span. If the caret in the component is blinking, the caret position is updated to be after the inserted symbol span. Currently, gestures, copying, and dragging are not supported.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number--><!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| options | [RichEditorSymbolSpanOptions](arkts-arkui-richeditorsymbolspanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## addTextSpan

```TypeScript
addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number
```

Adds a text span. If the caret in the component is blinking, the caret position is updated to be after the inserted text span.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number--><!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes |
| options | [RichEditorTextSpanOptions](arkts-arkui-richeditortextspanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## deleteSpans

```TypeScript
deleteSpans(value?: RichEditorRange): void
```

Deletes the text and image spans in a specified range.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void--><!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | No |

## fromStyledString

```TypeScript
fromStyledString(value: StyledString): Array<RichEditorSpan>
```

Converts a styled string into a span.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan>--><!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RichEditorSpan](arkts-arkui-richeditorspan-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getParagraphs

```TypeScript
getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>
```

Obtains the paragraph information within a specified range.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>--><!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RichEditorParagraphResult](arkts-arkui-richeditorparagraphresult-i.md)&gt; |

## getSelection

```TypeScript
getSelection(): RichEditorSelection
```

Obtains the range and span information of the selected content. If no text is selected, this API returns the information about the span where the caret is located.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-getSelection(): RichEditorSelection--><!--Device-RichEditorController-getSelection(): RichEditorSelection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RichEditorSelection](arkts-arkui-richeditorselection-i.md) |

## getSpans

```TypeScript
getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>
```

Obtains span information.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>--><!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RichEditorImageSpanResult](arkts-arkui-richeditorimagespanresult-i.md) \| [RichEditorTextSpanResult](arkts-arkui-richeditortextspanresult-i.md)&gt; |

## toStyledString

```TypeScript
toStyledString(value: RichEditorRange): StyledString
```

Convert the component content within the given range into a styled string. SymbolSpan and BuilderSpan cannot be converted.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString--><!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditorrange-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## updateParagraphStyle

```TypeScript
updateParagraphStyle(value: RichEditorParagraphStyleOptions): void
```

Updates the paragraph style.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void--><!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorParagraphStyleOptions](arkts-arkui-richeditorparagraphstyleoptions-i.md) | Yes |

## updateSpanStyle

```TypeScript
updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void
```

Updates the text, image, or symbol span style. If only part of a span is updated, the span is split into multiple spans based on the updated part and the non- updated part. Calling this API will not close the custom context menu on selection by default.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void--><!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorUpdateTextSpanStyleOptions](arkts-arkui-richeditorupdatetextspanstyleoptions-i.md) \| [RichEditorUpdateImageSpanStyleOptions](arkts-arkui-richeditorupdateimagespanstyleoptions-i.md) \| [RichEditorUpdateSymbolSpanStyleOptions](arkts-arkui-richeditorupdatesymbolspanstyleoptions-i.md) | Yes |
