# TextAreaController

Provides the method of switching the cursor position.

**Inheritance/Implementation:** TextAreaController extends TextContentControllerBase

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class TextAreaController--><!--Device-unnamed-export declare class TextAreaController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: int): void
```

Called when the position of the insertion cursor is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-caretPosition(value: int): void--><!--Device-TextAreaController-caretPosition(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | Length from the start of the string to the position where the caret is located. |

## constructor

```TypeScript
constructor()
```

constructor. A constructor used to create a TextAreaController object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-constructor()--><!--Device-TextAreaController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

Text selection is achieved by specifying the start and end positions of the text.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If &lt;em&gt;selectionMenuHidden&lt;/em&gt; is set to &lt;em&gt;true&lt;/em&gt; or a 2-in-1 device is used, calling setTextSelection does not display the context menu even when options is set to &lt;em&gt;MenuPolicy.SHOW&lt;/em&gt;. <br>If the selected text contains an emoji, the emoji is selected when its start position is within the text selection range. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-TextAreaController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The start position of the selected text. The start position of text in the text box is 0. A value less than 0 is handled as 0. A value greater than the maximum text length is handled as the maximum text length. |
| selectionEnd | int | Yes | The end position of the selected text. A value less than 0 is handled as the value 0. A value greater than the maximum text length is handled as the maximum text length. |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | No | Indicates the options of the text selection. Default value is MenuPolicy.DEFAULT. |

## stopEditing

```TypeScript
stopEditing(): void
```

Exit edit state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-stopEditing(): void--><!--Device-TextAreaController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

