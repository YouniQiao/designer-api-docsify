# TextController

Defines the controller of Text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TextController--><!--Device-unnamed-export declare class TextController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

Close the select menu when menu is on.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-closeSelectionMenu(): void--><!--Device-TextController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager | undefined
```

Get LayoutManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-getLayoutManager(): LayoutManager | undefined--><!--Device-TextController-getLayoutManager(): LayoutManager | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  Return the LayoutManager. |

## setStyledString

```TypeScript
setStyledString(value: StyledString): void
```

Update the styles of StyledString by setStyledString.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The child class MutableStyledString of StyledString can also serve as the argument.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-setStyledString(value: StyledString): void--><!--Device-TextController-setStyledString(value: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void
```

Text selection is achieved by specifying the start and end positions of the text.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If selectionStart or selectionEnd is set to undefined, the value 0 will be used.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If a 2-in-1 device is used,calling setTextSelection does not display the context menu even when options is set to MenuPolicy.SHOW.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_If the selected text contains an emoji,the emoji is selected when its start position is within the text selection range.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void--><!--Device-TextController-setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int \| undefined | Yes | The start position of the selected text. |
| selectionEnd | int \| undefined | Yes | The end position of the selected text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the options of the text selection. Default value is MenuPolicy.DEFAULT. |

