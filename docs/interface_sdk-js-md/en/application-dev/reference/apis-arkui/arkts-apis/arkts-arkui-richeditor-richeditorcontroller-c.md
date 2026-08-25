# RichEditorController

Provides Controller for RichEditor.

**Inheritance/Implementation:** RichEditorController extends [RichEditorBaseController](arkts-arkui-richeditor-richeditorbasecontroller-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addBuilderSpan

```TypeScript
addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): int | undefined
```

Add a builder span.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [RichEditorBuilderSpanOptions](arkts-arkui-richeditor-richeditorbuilderspanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int \| undefined |

## addImageSpan

```TypeScript
addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): int | undefined
```

Add a image span.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes |
| options | [RichEditorImageSpanOptions](arkts-arkui-richeditor-richeditorimagespanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int \| undefined |

## addSymbolSpan

```TypeScript
addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions): int | undefined
```

Add a symbol span.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| options | [RichEditorSymbolSpanOptions](arkts-arkui-richeditor-richeditorsymbolspanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int \| undefined |

## addTextSpan

```TypeScript
addTextSpan(content: ResourceStr, options?: RichEditorTextSpanOptions): int | undefined
```

Add a text span.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes |
| options | [RichEditorTextSpanOptions](arkts-arkui-richeditor-richeditortextspanoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| int \| undefined |

## deleteSpans

```TypeScript
deleteSpans(value?: RichEditorRange): void
```

Delete span.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | No |

## fromStyledString

```TypeScript
fromStyledString(value: StyledString): Array<RichEditorSpan> | undefined
```

Convert StyledString to spans in rich editor. return a empty Array&lt;RichEditorSpan&gt; if convert failed

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RichEditorSpan](arkts-arkui-richeditorspan-t.md)&gt; \| undefined |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getParagraphs

```TypeScript
getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult> | undefined
```

Get span content.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RichEditorParagraphResult](arkts-arkui-richeditor-richeditorparagraphresult-i.md)&gt; \| undefined |

## getSelection

```TypeScript
getSelection(): RichEditorSelection | undefined
```

Called when the content is selected.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RichEditorSelection](arkts-arkui-richeditor-richeditorselection-i.md) \| undefined |

## getSpans

```TypeScript
getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult> | undefined
```

Get span content.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[RichEditorImageSpanResult](arkts-arkui-richeditor-richeditorimagespanresult-i.md) \| [RichEditorTextSpanResult](arkts-arkui-richeditor-richeditortextspanresult-i.md)&gt; \| undefined |

## toStyledString

```TypeScript
toStyledString(value: RichEditorRange): StyledString | undefined
```

Convert spans to StyledString in rich editor. return a empty StyledString if convert failed

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StyledString](arkts-arkui-styledstring-styledstring-c.md) \| undefined |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## updateParagraphStyle

```TypeScript
updateParagraphStyle(value: RichEditorParagraphStyleOptions): void
```

Modify span style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorParagraphStyleOptions](arkts-arkui-richeditor-richeditorparagraphstyleoptions-i.md) | Yes |

## updateSpanStyle

```TypeScript
updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions |
        RichEditorUpdateSymbolSpanStyleOptions): void
```

Modify span style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RichEditorUpdateTextSpanStyleOptions](arkts-arkui-richeditor-richeditorupdatetextspanstyleoptions-i.md) \| [RichEditorUpdateImageSpanStyleOptions](arkts-arkui-richeditor-richeditorupdateimagespanstyleoptions-i.md) \| [RichEditorUpdateSymbolSpanStyleOptions](arkts-arkui-richeditor-richeditorupdatesymbolspanstyleoptions-i.md) | Yes |
