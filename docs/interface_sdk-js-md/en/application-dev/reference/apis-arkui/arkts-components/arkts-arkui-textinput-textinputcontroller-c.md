# TextInputController

Provides the method of switching the cursor position.

**Inheritance/Implementation:** TextInputController extends TextContentControllerBase

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class TextInputController--><!--Device-unnamed-export declare class TextInputController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: int): void
```

Called when the position of the insertion cursor is set.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is less than 0, the value 0 is used. <br>If the value exceeds the text length, the caret is placed at the end of the text. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-caretPosition(value: int): void--><!--Device-TextInputController-caretPosition(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes |  |

## constructor

```TypeScript
constructor()
```

constructor. A constructor used to create a TextInputController object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-constructor()--><!--Device-TextInputController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

Text selection is achieved by specifying the start and end positions of the text.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If selectionStart or selectionEnd is set to undefined, the value 0 will be used. <br>If selectionMenuHidden is set to true or a 2-in-1 device is used, calling setTextSelection does not display the context menu even when options is set to MenuPolicy.SHOW. <br>If the selected text contains an emoji, the emoji is selected when its start position is within the text selection range. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-TextInputController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The start position of the selected text.The start position of text in the text box is 0. |
| selectionEnd | int | Yes | The end position of the selected text. |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | No | Indicates the options of the text selection.Default value is MenuPolicy.DEFAULT. |

## stopEditing

```TypeScript
stopEditing(): void
```

Exit edit state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextInputController-stopEditing(): void--><!--Device-TextInputController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

