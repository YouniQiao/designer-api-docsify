# TextBaseController

Define the text selection controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextBaseController--><!--Device-unnamed-export declare interface TextBaseController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

Close the select menu when menu is on.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextBaseController-closeSelectionMenu(): void--><!--Device-TextBaseController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager | undefined
```

Get LayoutManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextBaseController-getLayoutManager(): LayoutManager | undefined--><!--Device-TextBaseController-getLayoutManager(): LayoutManager | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - Return the LayoutManager. |

## setSelection

```TypeScript
setSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

Set selection to select a range of content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextBaseController-setSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-TextBaseController-setSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The start position of the selected text. |
| selectionEnd | int | Yes | The end position of the selected text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the options of selection. |

