# TextController

Defines the controller of Text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class TextController--><!--Device-unnamed-export declare class TextController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

Close the select menu when menu is on.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-closeSelectionMenu(): void--><!--Device-TextController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager | undefined
```

Get LayoutManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-getLayoutManager(): LayoutManager | undefined--><!--Device-TextController-getLayoutManager(): LayoutManager | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LayoutManager](../arkts-apis/arkts-arkui-textcommon-layoutmanager-i.md) \| undefined | Return the LayoutManager. |

## setStyledString

```TypeScript
setStyledString(value: StyledString): void
```

Update the styles of StyledString by setStyledString.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The child class MutableStyledString of StyledString can also serve as the argument. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-setStyledString(value: StyledString): void--><!--Device-TextController-setStyledString(value: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [StyledString](../arkts-apis/arkts-arkui-styledstring-styledstring-c.md) | Yes |  |

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void
```

Text selection is achieved by specifying the start and end positions of the text.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If selectionStart or selectionEnd is set to undefined, the value 0 will be used. <br>If a 2-in-1 device is used, calling setTextSelection does not display the context menu even when options is set to MenuPolicy.SHOW. <br>If the selected text contains an emoji, the emoji is selected when its start position is within the text selection range. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextController-setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void--><!--Device-TextController-setTextSelection(selectionStart: int | undefined, selectionEnd: int | undefined, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int \| undefined | Yes | The start position of the selected text. |
| selectionEnd | int \| undefined | Yes | The end position of the selected text. |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | No | Indicates the options of the text selection. Default value is MenuPolicy.DEFAULT. |

