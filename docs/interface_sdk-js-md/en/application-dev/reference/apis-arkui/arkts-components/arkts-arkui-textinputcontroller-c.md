# TextInputController

The controller for the **TextInput** component inherits from  
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

```ts controller: TextInputController = new TextInputController();```

**Inheritance/Implementation:** TextInputController extends [TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class TextInputController extends TextContentControllerBase--><!--Device-unnamed-declare class TextInputController extends TextContentControllerBase-End-->

**System capability:** 
- API version 10 and later: SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

Sets the position of the caret. If the value is less than 0, the value **0** is used. If the value exceeds the text length, the caret is placed at the end of the text.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-caretPosition(value: number): void--><!--Device-TextInputController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Length from the start of the string to the position where the caret is located. |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TextInputController** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-constructor()--><!--Device-TextInputController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

Sets the text selection area, which will be highlighted.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-TextInputController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number | Yes | Start position of the text selection range. The start position of text in the text box is 0. |
| selectionEnd | number | Yes | End position of the text selection range. If **selectionEnd** is less than 0, it is handled as **0**. If **selectionEnd** exceeds the text length, it is clamped to the text length. |
| options | [SelectionOptions](../arkts-apis/arkts-arkui-common-selectionoptions-i.md) | No | Configuration options for text selection.&lt;br&gt;Default value: **MenuPolicy.DEFAULT**&lt;br&gt;This parameter can be used in atomic services since API version 12.<br>**Since:** 12 |

## stopEditing

```TypeScript
stopEditing(): void
```

Exits the editing state.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-stopEditing(): void--><!--Device-TextInputController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

