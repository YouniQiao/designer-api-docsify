# RichEditorController

Provides Controller for RichEditor.

**Inheritance/Implementation:** RichEditorController extends [RichEditorBaseController](arkts-arkui-richeditor-richeditorbasecontroller-c.md#richeditorbasecontroller)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class RichEditorController--><!--Device-unnamed-export declare class RichEditorController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addBuilderSpan

```TypeScript
addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): int | undefined
```

Add a builder span.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): int | undefined--><!--Device-RichEditorController-addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | CustomBuilder | Yes | Indicates the custom builder node |
| options | [RichEditorBuilderSpanOptions](arkts-arkui-richeditor-richeditorbuilderspanoptions-i.md) | No | span option. |

**Return value:**

| Type | Description |
| --- | --- |
| int | span index |

## addImageSpan

```TypeScript
addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): int | undefined
```

Add a image span.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): int | undefined--><!--Device-RichEditorController-addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | image value. |
| options | [RichEditorImageSpanOptions](arkts-arkui-richeditor-richeditorimagespanoptions-i.md) | No | image span info. |

**Return value:**

| Type | Description |
| --- | --- |
| int | span index |

## addSymbolSpan

```TypeScript
addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions): int | undefined
```

Add a symbol span.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions): int | undefined--><!--Device-RichEditorController-addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | symbol span value |
| options | [RichEditorSymbolSpanOptions](arkts-arkui-richeditor-richeditorsymbolspanoptions-i.md) | No | symbol span option. |

**Return value:**

| Type | Description |
| --- | --- |
| int | symbol span index |

## addTextSpan

```TypeScript
addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): int | undefined
```

Add a text span.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): int | undefined--><!--Device-RichEditorController-addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | text value. |
| options | [RichEditorTextSpanOptions](arkts-arkui-richeditor-richeditortextspanoptions-i.md) | No | span info. |

**Return value:**

| Type | Description |
| --- | --- |
| int | span index |

## deleteSpans

```TypeScript
deleteSpans(value?: RichEditorRange): void
```

Delete span.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void--><!--Device-RichEditorController-deleteSpans(value?: RichEditorRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | No | range for deleting. |

## fromStyledString

```TypeScript
fromStyledString(value: StyledString): Array<RichEditorSpan> | undefined
```

Convert StyledString to spans in rich editor. return a empty Array&lt;RichEditorSpan&gt; if convert failed

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan> | undefined--><!--Device-RichEditorController-fromStyledString(value: StyledString): Array<RichEditorSpan> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes | StyledString. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[RichEditorSpan](arkts-arkui-richeditorspan-t.md)&gt; | return convert value |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. |

## getParagraphs

```TypeScript
getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult> | undefined
```

Get span content.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult> | undefined--><!--Device-RichEditorController-getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | No | range for getting span info. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[RichEditorParagraphResult](arkts-arkui-richeditor-richeditorparagraphresult-i.md)&gt; |  |

## getSelection

```TypeScript
getSelection(): RichEditorSelection | undefined
```

Called when the content is selected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-getSelection(): RichEditorSelection | undefined--><!--Device-RichEditorController-getSelection(): RichEditorSelection | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RichEditorSelection](arkts-arkui-richeditor-richeditorselection-i.md) |  |

## getSpans

```TypeScript
getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult> | undefined
```

Get span content.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult> | undefined--><!--Device-RichEditorController-getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | No | range for getting span info. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[RichEditorImageSpanResult](arkts-arkui-richeditor-richeditorimagespanresult-i.md) \| [RichEditorTextSpanResult](arkts-arkui-richeditor-richeditortextspanresult-i.md)&gt; |  |

## toStyledString

```TypeScript
toStyledString(value: RichEditorRange): StyledString | undefined
```

Convert spans to StyledString in rich editor. return a empty StyledString if convert failed

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString | undefined--><!--Device-RichEditorController-toStyledString(value: RichEditorRange): StyledString | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | Yes | range of spans in rich editor |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledString](arkts-arkui-styledstring-styledstring-c.md) |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. |

## updateParagraphStyle

```TypeScript
updateParagraphStyle(value: RichEditorParagraphStyleOptions): void
```

Modify span style.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void--><!--Device-RichEditorController-updateParagraphStyle(value: RichEditorParagraphStyleOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorParagraphStyleOptions](arkts-arkui-richeditor-richeditorparagraphstyleoptions-i.md) | Yes |  |

## updateSpanStyle

```TypeScript
updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions |
        RichEditorUpdateSymbolSpanStyleOptions): void
```

Modify span style.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions |        RichEditorUpdateSymbolSpanStyleOptions): void--><!--Device-RichEditorController-updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions |        RichEditorUpdateSymbolSpanStyleOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorUpdateTextSpanStyleOptions](arkts-arkui-richeditor-richeditorupdatetextspanstyleoptions-i.md) \| [RichEditorUpdateImageSpanStyleOptions](arkts-arkui-richeditor-richeditorupdateimagespanstyleoptions-i.md) \| [RichEditorUpdateSymbolSpanStyleOptions](arkts-arkui-richeditor-richeditorupdatesymbolspanstyleoptions-i.md) | Yes |  |

