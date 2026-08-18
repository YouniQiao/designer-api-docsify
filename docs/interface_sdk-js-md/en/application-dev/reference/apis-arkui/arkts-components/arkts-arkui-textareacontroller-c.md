# TextAreaController

The controller for the **TextArea** component inherits from TextContentControllerBase. The APIs involved are as follows:<!--Del--> system API getText and other APIs like<!--DelEnd--> getTextContentRect, getTextContentLineCount, getCaretOffset, addText, deleteText, getSelection, clearPreviewText, setStyledPlaceholder, and deleteBackward.

## Objects to Import ```ts controller: TextAreaController = new TextAreaController(); ```

**Inheritance/Implementation:** TextAreaController extends TextContentControllerBase

**Since:** 8

<!--Device-unnamed-declare class TextAreaController--><!--Device-unnamed-declare class TextAreaController-End-->

**System capability:** 
- API version 10 and later: SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## caretPosition

```TypeScript
caretPosition(value: number): void
```

Sets the position of the caret.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-caretPosition(value: number): void--><!--Device-TextAreaController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Length from the start of the string to the position where the caret is located.<br>Values less than 0 are treated as **0**. Values greater than the string length are treated as the string length. |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TextAreaController** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-constructor()--><!--Device-TextAreaController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-TextAreaController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number | Yes | Start position of the text selection range. The start position of text in the text box is 0.<br>Values less than 0 are treated as **0**. Values greater than the maximum text length are treated as the maximum text length.<br> |
| selectionEnd | number | Yes | End position of the text selection range.<br>Values less than 0 are treated as **0**. Values greater than the maximum text length are treated as the maximum text length.<br> |
| options | SelectionOptions | No | Configuration options for text selection.<br>Default value: **MenuPolicy.DEFAULT**<br><br>**Since:** 12 |

## stopEditing

```TypeScript
stopEditing(): void
```

Exits the editing state.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-stopEditing(): void--><!--Device-TextAreaController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

