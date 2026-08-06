# RichEditorController

Implements the **RichEditor** component controller. Inherits from  
[RichEditorBaseController]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.
    **NOTE**  
    
    When the length of the content exceeds the height of the display area of the component, the insertion interface (  
    such as [addTextSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_,  
    [addImageSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_,  
    [addBuilderSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ and  
    [addSymbolSpan]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_) is called. The component automatically scrolls the  
    content to make the end of the inserted content visible.

**Inheritance/Implementation:** RichEditorController extends [RichEditorBaseController](../arkts-apis/arkts-arkui-component/richeditor-richeditorbasecontroller-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class RichEditorController extends RichEditorBaseController--><!--Device-unnamed-declare class RichEditorController extends RichEditorBaseController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addBuilderSpan

```TypeScript
addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number
```

Adds a custom layout (BuilderSpan) to **RichEditor**.
    **NOTE**  
    
    - This API adds a builder span to take up space in the layout. It calls the system **measure** method to  
    calculate the actual length, width, and position.  
    
    - You can use [RichEditorBuilderSpanOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_32\_\_\_ to set the index of the builder  
    in the **RichEditor** component (with one character as the unit).  
    
    - This builder span is unfocusable, draggable, and equipped with certain universal attributes. It behaves  
    similarly to an image span in terms of placeholder and deletion functionality, and it is treated as a single  
    character in length.  
    
    - Custom menus can be set using [bindSelectionMenu]\_\_\_JSDOC\_LINK\_DESC\_USD\_33\_\_\_.  
    
    - The information about the builder span cannot be obtained through  
    [getSpans]\_\_\_JSDOC\_LINK\_DESC\_USD\_34\_\_\_, [getSelection]\_\_\_JSDOC\_LINK\_DESC\_USD\_35\_\_\_,  
    [onSelect]\_\_\_JSDOC\_LINK\_DESC\_USD\_36\_\_\_, or [aboutToDelete]\_\_\_JSDOC\_LINK\_DESC\_USD\_37\_\_\_.  
    
    - The builder span cannot be updated using [updateSpanStyle]\_\_\_JSDOC\_LINK\_DESC\_USD\_38\_\_\_ or  
    [updateParagraphStyle]\_\_\_JSDOC\_LINK\_DESC\_USD\_39\_\_\_.  
    
    - Copying or pasting the builder span does not take effect.  
    
    - The layout constraints of the builder span are passed in from the **RichEditor** component. If the size of the  
    outermost component in the builder span is not set, the size of the **RichEditor** is used as the value of  
    **maxSize**.  
    
    - The gesture event mechanism of the builder span is the same as the universal gesture event mechanism. If  
    transparent transmission is not set in the builder, only the child components in the builder respond.  
    
    - If the caret in the component is blinking, the caret position is updated to be after the inserted image span.

Only the following universal attributes are supported:  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_5\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_6\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_7\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_8\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_9\_\_\_, [opacity]\_\_\_JSDOC\_LINK\_DESC\_USD\_40\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_10\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_11\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_12\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_13\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_14\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_15\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_16\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_17\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_18\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_19\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_20\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_21\_\_\_, \_\_\_MD\_LINK\_DESC\_USD\_22\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_23\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_24\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_25\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_26\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_27\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_28\_\_\_,  
\_\_\_MD\_LINK\_DESC\_USD\_29\_\_\_, \_\_\_MD\_LINK\_DESC\_USD\_30\_\_\_,

\_\_\_MD\_LINK\_DESC\_USD\_31\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number--><!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Custom component. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Builder options. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Index of the added builder span in all spans. |

## addImageSpan

```TypeScript
addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number
```

Adds an image span. If the caret in the component is blinking, the caret position is updated to be after the inserted image span.

This API is a synchronous API. In a weak network environment, directly adding network images may block the UI thread and cause screen freezing. To avoid potential loading issues, do not directly add a network image.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number--><!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| ResourceStr | Yes | Image content. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Image options. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Index of the added image span in all spans. |

## addSymbolSpan

```TypeScript
addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number
```

Adds a symbol span. If the caret in the component is blinking, the caret position is updated to be after the inserted symbol span.

Currently, gestures, copying, and dragging are not supported.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number--><!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions ): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Symbol resource object. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Symbol options. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Index of the added symbol span in all spans. |

## addTextSpan

```TypeScript
addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number
```

Adds a text span. If the caret in the component is blinking, the caret position is updated to be after the inserted text span.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number--><!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Text content.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The Resource type is supported since API version 20.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 20 |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Text options. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Index of the added text span in all spans. |

## deleteSpans

```TypeScript
deleteSpans(value?: RichEditorRange): void
```

Deletes the text and image spans in a specified range.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void--><!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Range of the target spans. If this parameter is left empty, all text and image spans will be deleted. |

## fromStyledString

```TypeScript
fromStyledString(value: StyledString): Array<RichEditorSpan>
```

Converts a styled string into a span.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan>--><!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Styled string before conversion. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RichEditorSpan&gt; | Text and image span information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. |

## getParagraphs

```TypeScript
getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>
```

Obtains the paragraph information within a specified range.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>--><!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Range of the paragraphs to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RichEditorParagraphResult&gt; | Information about the selected paragraphs. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If no component is bound to the controller or the component bound to the controller is released, **undefined** is returned. |

## getSelection

```TypeScript
getSelection(): RichEditorSelection
```

Obtains the range and span information of the selected content. If no text is selected, this API returns the information about the span where the caret is located.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-getSelection(): RichEditorSelection--><!--Device-RichEditorController-getSelection(): RichEditorSelection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Provides information about the selected content. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If no component is bound to the controller or the component bound to the controller is released, **undefined** is returned. |

## getSpans

```TypeScript
getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>
```

Obtains span information.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>--><!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Range of the target span. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RichEditorImageSpanResult \| RichEditorTextSpanResult&gt; | Text and image span information. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If no component is bound to the controller or the component bound to the controller is released, **undefined** is returned. |

## toStyledString

```TypeScript
toStyledString(value: RichEditorRange): StyledString
```

Convert the component content within the given range into a styled string. SymbolSpan and BuilderSpan cannot be converted.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString--><!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Source range. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Styled string after conversion. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. |

## updateParagraphStyle

```TypeScript
updateParagraphStyle(value: RichEditorParagraphStyleOptions): void
```

Updates the paragraph style.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void--><!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the paragraph style. |

## updateSpanStyle

```TypeScript
updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void
```

Updates the text, image, or symbol span style.

If only part of a span is updated, the span is split into multiple spans based on the updated part and the non-updated part.

Calling this API will not close the custom context menu on selection by default.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void--><!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| RichEditorUpdateImageSpanStyleOptions \| RichEditorUpdateSymbolSpanStyleOptions | Yes | Style options of the text, image, or symbol span.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 11 |

