# RichEditor

**RichEditor** is a component that supports interactive text editing and mixture of text and imagery. > **NOTE** > > This component is supported since API version 10. Updates will be marked with a superscript to indicate their > earliest API version.

## RichEditor

```TypeScript
RichEditor(value: RichEditorOptions)
```

Called when create RichEditor.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorInterface-(value: RichEditorOptions): RichEditorAttribute--><!--Device-RichEditorInterface-(value: RichEditorOptions): RichEditorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorOptions](arkts-arkui-richeditoroptions-i.md) | Yes | Options for initializing the component. |

## RichEditor

```TypeScript
RichEditor(options: RichEditorStyledStringOptions)
```

Called when create RichEditor.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorInterface-(options: RichEditorStyledStringOptions): RichEditorAttribute--><!--Device-RichEditorInterface-(options: RichEditorStyledStringOptions): RichEditorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) | Yes | Options for initializing the component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CopyEvent](arkts-arkui-copyevent-i.md) | User copy event. |
| [CutEvent](arkts-arkui-cutevent-i.md) | Defines a custom cut event. |
| [KeyboardOptions](arkts-arkui-keyboardoptions-i.md) | Sets whether to support keyboard avoidance. |
| [LeadingMarginPlaceholder](arkts-arkui-leadingmarginplaceholder-i.md) | Describes the leading margin placeholder, which dictates the distance between the left edges of the paragraph and the component. |
| [PasteEvent](arkts-arkui-pasteevent-i.md) | Defines a custom paste event. |
| [PlaceholderStyle](arkts-arkui-placeholderstyle-i.md) | Style of the placeholder text. |
| [RichEditorBuilderSpanOptions](arkts-arkui-richeditorbuilderspanoptions-i.md) | Sets the offset and style of the builder. |
| [RichEditorChangeValue](arkts-arkui-richeditorchangevalue-i.md) | Image and text change information. |
| [RichEditorDeleteValue](arkts-arkui-richeditordeletevalue-i.md) | Provides information about the delete operation and the deleted content. |
| [RichEditorGesture](arkts-arkui-richeditorgesture-i.md) | User gesture event. |
| [RichEditorImageSpan](arkts-arkui-richeditorimagespan-i.md) | Image span information. |
| [RichEditorImageSpanOptions](arkts-arkui-richeditorimagespanoptions-i.md) | Sets the offset and style of an image span. |
| [RichEditorImageSpanResult](arkts-arkui-richeditorimagespanresult-i.md) | Provides the image information returned by the backend. |
| [RichEditorImageSpanStyle](arkts-arkui-richeditorimagespanstyle-i.md) | Sets the image span style. |
| [RichEditorImageSpanStyleResult](arkts-arkui-richeditorimagespanstyleresult-i.md) | Provides the image span style information returned by the backend. |
| [RichEditorInsertValue](arkts-arkui-richeditorinsertvalue-i.md) | Information about the text to be inserted. |
| [RichEditorLayoutStyle](arkts-arkui-richeditorlayoutstyle-i.md) | Image layout information. |
| [RichEditorOptions](arkts-arkui-richeditoroptions-i.md) | Defines the options for initializing the **RichEditor** component. |
| [RichEditorParagraphResult](arkts-arkui-richeditorparagraphresult-i.md) | Describes the returned paragraph information. |
| [RichEditorParagraphStyle](arkts-arkui-richeditorparagraphstyle-i.md) | Describes the paragraph style. |
| [RichEditorParagraphStyleOptions](arkts-arkui-richeditorparagraphstyleoptions-i.md) | Defines the paragraph style options. Inherits [RichEditorRange](arkts-arkui-richeditorrange-i.md). &gt; **NOTE：**&gt; &gt; Applicable scope of the API: spans involved in the specified range. |
| [RichEditorRange](arkts-arkui-richeditorrange-i.md) | Defines the range of the **RichEditor**. |
| [RichEditorSelection](arkts-arkui-richeditorselection-i.md) | Provides information about the selected content. |
| [RichEditorSpanPosition](arkts-arkui-richeditorspanposition-i.md) | Provides the span position information. |
| [RichEditorSpanStyleOptions](arkts-arkui-richeditorspanstyleoptions-i.md) | Defines the text span style options. Inherits [RichEditorRange](arkts-arkui-richeditorrange-i.md). |
| [RichEditorStyledStringOptions](arkts-arkui-richeditorstyledstringoptions-i.md) | Defines the options for initializing the **RichEditor** component. |
| [RichEditorSymbolSpanOptions](arkts-arkui-richeditorsymbolspanoptions-i.md) | Sets the offset and style of the **SymbolSpan** component. |
| [RichEditorSymbolSpanStyle](arkts-arkui-richeditorsymbolspanstyle-i.md) | Sets the symbol span style. |
| [RichEditorSymbolSpanStyleResult](arkts-arkui-richeditorsymbolspanstyleresult-i.md) | Provides the symbol span style information returned by the backend. |
| [RichEditorTextSpan](arkts-arkui-richeditortextspan-i.md) | Provides the text span information. |
| [RichEditorTextSpanOptions](arkts-arkui-richeditortextspanoptions-i.md) | Describes the options for adding a text span. |
| [RichEditorTextSpanResult](arkts-arkui-richeditortextspanresult-i.md) | Provides the text span information. |
| [RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md) | Provides the text style information. |
| [RichEditorTextStyleResult](arkts-arkui-richeditortextstyleresult-i.md) | Provides the text span style information returned by the backend. While **fontWeight** in **RichEditorTextStyle** sets the font weight, **fontWeight** in **RichEditorTextStyleResult** returns the set font weight after conversion to digits. Conversion relationship between fontWeight in RichEditorSymbolSpanStyle and RichEditorSymbolSpanStyleResult, the conversion relationship is the same as that of fontWeight in RichEditorTextStyle and RichEditorTextStyleResult. |
| [RichEditorUpdateImageSpanStyleOptions](arkts-arkui-richeditorupdateimagespanstyleoptions-i.md) | Image style options. Inherits [RichEditorSpanStyleOptions](arkts-arkui-richeditorspanstyleoptions-i.md). |
| [RichEditorUpdateSymbolSpanStyleOptions](arkts-arkui-richeditorupdatesymbolspanstyleoptions-i.md) | Defines the symbol span style options. Inherits [RichEditorSpanStyleOptions](arkts-arkui-richeditorspanstyleoptions-i.md). |
| [RichEditorUpdateTextSpanStyleOptions](arkts-arkui-richeditorupdatetextspanstyleoptions-i.md) | Defines the text span style options. Inherits [RichEditorSpanStyleOptions](arkts-arkui-richeditorspanstyleoptions-i.md). |
| [RichEditorUrlStyle](arkts-arkui-richeditorurlstyle-i.md) | URL information. |
| [SelectionMenuOptions](arkts-arkui-selectionmenuoptions-i.md) | Sets menu options. |

### Types

| Name | Description |
| --- | --- |
| [MenuCallback](arkts-arkui-menucallback-t.md) | Represents the callback invoked when the custom context menu on selection is shown or hidden. |
| [MenuOnAppearCallback](arkts-arkui-menuonappearcallback-t.md) | Represents the callback invoked when the custom context menu on selection appears. |
| [OnHoverCallback](arkts-arkui-onhovercallback-t.md) | Represents the callback invoked on mouse hover. |
| [PasteEventCallback](arkts-arkui-pasteeventcallback-t.md) | Represents the callback invoked when the paste is about to be completed. |
| [RichEditorSpan](arkts-arkui-richeditorspan-t.md) | Provides the span information of the **RichEditor** component. |
| [SubmitCallback](arkts-arkui-submitcallback-t.md) | Represents the callback invoked when the Enter key on the soft keyboard is pressed. |

### Enums

| Name | Description |
| --- | --- |
| [RichEditorDeleteDirection](arkts-arkui-richeditordeletedirection-e.md) | Deletion direction. |
| [RichEditorResponseType](arkts-arkui-richeditorresponsetype-e.md) | Response type of the menu. |
| [RichEditorSpanType](arkts-arkui-richeditorspantype-e.md) | Provides the span type information. |
| [UndoStyle](arkts-arkui-undostyle-e.md) | Enumerates the options for whether to retain the original style during undo/redo operations. |

