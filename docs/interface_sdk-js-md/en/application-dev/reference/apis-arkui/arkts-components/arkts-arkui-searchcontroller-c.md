# SearchController

The controller for the **Search** component inherits from  
[TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md). The APIs involved are as follows:&lt;!--Del--&gt; system API  
[getText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c-sys.md/arkts-arkui-common-textcontentcontrollerbase-c-sys.md#gettext) and other APIs like&lt;!--DelEnd--&gt;  
[getTextContentRect](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#gettextcontentrect),  
[getTextContentLineCount](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#gettextcontentlinecount),  
[getCaretOffset](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#getcaretoffset), [addText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#addtext),  
[deleteText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#deletetext),  
[getSelection](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#getselection),  
[clearPreviewText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#clearpreviewtext),  
[setStyledPlaceholder](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#setstyledplaceholder), and  
[deleteBackward](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#deletebackward).

## Objects to Import

```ts controller: SearchController = new SearchController();```

**Inheritance/Implementation:** SearchController extends [TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class SearchController extends TextContentControllerBase--><!--Device-unnamed-declare class SearchController extends TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

Sets the position of the caret.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchController-caretPosition(value: number): void--><!--Device-SearchController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Length from the start of the character string to the position where the caret is located. &lt;br&gt;Values less than 0 are treated as **0**. Values greater than the string length are treated as the string length. |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **SearchController** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchController-constructor()--><!--Device-SearchController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SearchController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-SearchController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number | Yes | Start position of the text selection range. The start position of text in the text box is 0.&lt;br&gt;A value less than 0 is handled as **0**. A value greater than the maximum text length is handled as the maximum text length.&lt;br&gt; |
| selectionEnd | number | Yes | End position of the text selection range.&lt;br&gt;A value less than 0 is handled as **0**. A value greater than the maximum text length is handled as the maximum text length.&lt;br&gt; |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | No | Configuration options for text selection.&lt;br&gt;Default value: **MenuPolicy.DEFAULT |

## stopEditing

```TypeScript
stopEditing(): void
```

Exits the editing state.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchController-stopEditing(): void--><!--Device-SearchController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

