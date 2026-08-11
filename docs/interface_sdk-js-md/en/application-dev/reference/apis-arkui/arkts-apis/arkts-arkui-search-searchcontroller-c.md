# SearchController

Provides the method of switching the cursor position.

**Inheritance/Implementation:** SearchController extends [TextContentControllerBase](arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SearchController extends TextContentControllerBase--><!--Device-unnamed-export declare class SearchController extends TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: int): void
```

Called when the position of the insertion cursor is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-caretPosition(value: int): void--><!--Device-SearchController-caretPosition(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | Length from the start of the character string to the position where the caret is located. |

## constructor

```TypeScript
constructor()
```

constructor.A constructor used to create a SearchController object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-constructor()--><!--Device-SearchController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

Text selection is achieved by specifying the start and end positions of the text.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;If selectionStart or selectionEnd is set to undefined, the value 0 will be used.&lt;br&gt;If &lt;em&gt;selectionMenuHidden&lt;/em&gt; is set to &lt;em&gt;true&lt;/em&gt; or a 2-in-1 device is used,calling setTextSelection does not display the context menu even when options is set to &lt;em&gt;MenuPolicy.SHOW&lt;/em&gt;.&lt;br&gt;If the selected text contains an emoji, the emoji is selected when its start position is within the text selection range.&lt;br&gt;Sets the text selection range and highlights the selected text when the component is focused.&lt;br&gt;This API works only when the value of selectionStart is less than that of selectionEnd.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-SearchController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The start position of the selected text. The start position of text in the text box is 0. A value less than 0 is handled as 0. A value greater than the maximum text length is handled as the maximum text length. |
| selectionEnd | int | Yes | The end position of the selected text. A value less than 0 is handled as the value 0. A value greater than the maximum text length is handled as the maximum text length. |
| options | [SelectionOptions](../arkts-components/arkts-arkui-selectionoptions-i.md) | No | Indicates the options of the text selection. Default value is MenuPolicy.DEFAULT. |

## stopEditing

```TypeScript
stopEditing(): void
```

Exit edit state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-stopEditing(): void--><!--Device-SearchController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

