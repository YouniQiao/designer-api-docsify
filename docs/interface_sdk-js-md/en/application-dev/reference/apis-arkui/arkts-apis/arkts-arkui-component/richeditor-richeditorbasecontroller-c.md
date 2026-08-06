# RichEditorBaseController

Provides Base Controller for RichEditor.

**Inheritance/Implementation:** RichEditorBaseController implements [TextEditControllerEx](textcommon-texteditcontrollerex-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RichEditorBaseController implements TextEditControllerEx--><!--Device-unnamed-export declare class RichEditorBaseController implements TextEditControllerEx-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

close the select menu when menu is on.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-closeSelectionMenu(): void--><!--Device-RichEditorBaseController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

Delete the last character of the input field component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-deleteBackward(): void--><!--Device-RichEditorBaseController-deleteBackward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): int | undefined
```

Get caret offset from controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-getCaretOffset(): int | undefined--><!--Device-RichEditorBaseController-getCaretOffset(): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int |  |

## getCaretRect

```TypeScript
getCaretRect(): RectResult | undefined
```

Get CaretRect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-getCaretRect(): RectResult | undefined--><!--Device-RichEditorBaseController-getCaretRect(): RectResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  Return the caret rect or undefined value. |

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager | undefined
```

Get LayoutManager.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-getLayoutManager(): LayoutManager | undefined--><!--Device-RichEditorBaseController-getLayoutManager(): LayoutManager | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  Return the LayoutManager. |

## getPreviewText

```TypeScript
getPreviewText(): PreviewText | undefined
```

Get PreviewText.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-getPreviewText(): PreviewText | undefined--><!--Device-RichEditorBaseController-getPreviewText(): PreviewText | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  Return the PreviewText. |

## getTypingStyle

```TypeScript
getTypingStyle(): RichEditorTextStyle | undefined
```

Get the typing text style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-getTypingStyle(): RichEditorTextStyle | undefined--><!--Device-RichEditorBaseController-getTypingStyle(): RichEditorTextStyle | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## isEditing

```TypeScript
isEditing(): boolean | undefined
```

Judge whether is in editing state

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-isEditing(): boolean | undefined--><!--Device-RichEditorBaseController-isEditing(): boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  true is editing state, false is non editing status |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

Scroll the input field component to make the specified content visible.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-RichEditorBaseController-scrollToVisible(range?: TextRange): void--><!--Device-RichEditorBaseController-scrollToVisible(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The visible range. If the parameter is invalid, this method will have no effect. |

## setCaretOffset

```TypeScript
setCaretOffset(offset: int): boolean | undefined
```

Set caret offset.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-setCaretOffset(offset: int): boolean | undefined--><!--Device-RichEditorBaseController-setCaretOffset(offset: int): boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | caret offset. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## setSelection

```TypeScript
setSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

Specify the start and end positions to select a range of content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-setSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-RichEditorBaseController-setSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | The start position of the selected text. |
| selectionEnd | int | Yes | The end position of the selected text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Indicates the options of selection. |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

Set the styledString placeholder.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-setStyledPlaceholder(styledString: StyledString): void--><!--Device-RichEditorBaseController-setStyledPlaceholder(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The styledString for placeholder. If the parameter is invalid, this method will have no effect. |

## setTypingParagraphStyle

```TypeScript
setTypingParagraphStyle(style: RichEditorParagraphStyle | undefined): void
```

Set the typing paragraph style.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-setTypingParagraphStyle(style: RichEditorParagraphStyle | undefined): void--><!--Device-RichEditorBaseController-setTypingParagraphStyle(style: RichEditorParagraphStyle | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | set the typing paragraph style. |

## setTypingStyle

```TypeScript
setTypingStyle(value: RichEditorTextStyle): void
```

Set the typing text style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-setTypingStyle(value: RichEditorTextStyle): void--><!--Device-RichEditorBaseController-setTypingStyle(value: RichEditorTextStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | set the typing text style. |

## stopEditing

```TypeScript
stopEditing(): void
```

Stop editing state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBaseController-stopEditing(): void--><!--Device-RichEditorBaseController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

