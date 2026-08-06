# TextAreaController

Provides the method of switching the cursor position.

**Inheritance/Implementation:** TextAreaController extends [TextContentControllerBase](common-textcontentcontrollerbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TextAreaController extends TextContentControllerBase--><!--Device-unnamed-export declare class TextAreaController extends TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: int): void
```

Called when the position of the insertion cursor is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

constructor.A constructor used to create a TextAreaController object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-constructor()--><!--Device-TextAreaController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

Text selection is achieved by specifying the start and end positions of the text.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_selectionMenuHidden\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ is set to \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_true\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ or a 2-in-1 device is used,calling setTextSelection does not display the context menu even when options is set to \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_MenuPolicy.SHOW\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_If the selected text contains an emoji,the emoji is selected when its start position is within the text selection range.\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-TextAreaController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The start position of the selected text. The start position of text in the text box is 0. A value less than 0 is handled as 0. A value greater than the maximum text length is handled as the maximum text length. |
| selectionEnd | int | Yes | The end position of the selected text. A value less than 0 is handled as the value 0. A value greater than the maximum text length is handled as the maximum text length. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the options of the text selection. Default value is MenuPolicy.DEFAULT. |

## stopEditing

```TypeScript
stopEditing(): void
```

Exit edit state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextAreaController-stopEditing(): void--><!--Device-TextAreaController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

