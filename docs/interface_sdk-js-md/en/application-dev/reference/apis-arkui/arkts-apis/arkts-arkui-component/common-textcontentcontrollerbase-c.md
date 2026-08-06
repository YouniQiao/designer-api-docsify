# TextContentControllerBase

TextContentControllerBase

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class TextContentControllerBase--><!--Device-unnamed-export declare abstract class TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addText

```TypeScript
addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined
```

Add a text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined--><!--Device-TextContentControllerBase-addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text value. |
| textOperationOptions | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | operation info. |

**Return value:**

| Type | Description |
| --- | --- |
| int | caret index |

## clearPreviewText

```TypeScript
clearPreviewText(): void
```

Clear the content of preview.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-clearPreviewText(): void--><!--Device-TextContentControllerBase-clearPreviewText(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

Delete the last character of the input field component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-deleteBackward(): void--><!--Device-TextContentControllerBase-deleteBackward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteText

```TypeScript
deleteText(range?: TextRange): void
```

Delete text in TextRange.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-deleteText(range?: TextRange): void--><!--Device-TextContentControllerBase-deleteText(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | range for deleting. |

## getCaretOffset

```TypeScript
getCaretOffset(): CaretOffset | undefined
```

Get the index and relative position of the CaretOffset.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If this API is called when the caret position is updated in the current frame, it will not take effect.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_For the Search component, the returned position information is the offset of the first character relative to the search icon in the component.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_If no text is entered in the Search component,the return value contains the position information relative to the component.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_The location information in the return value is the location of the caret relative to the editable component.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getCaretOffset(): CaretOffset | undefined--><!--Device-TextContentControllerBase-getCaretOffset(): CaretOffset | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | index and relative position of the CaretOffset. |

## getSelection

```TypeScript
getSelection(): TextRange | undefined
```

Gets the selected range of text content.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getSelection(): TextRange | undefined--><!--Device-TextContentControllerBase-getSelection(): TextRange | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | range for selecting. |

## getTextContentLineCount

```TypeScript
getTextContentLineCount(): int | undefined
```

Get the lines number of the text content.The getTextContentLineCount type is used to obtain the number of lines of the edited text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getTextContentLineCount(): int | undefined--><!--Device-TextContentControllerBase-getTextContentLineCount(): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | Text content line count |

## getTextContentRect

```TypeScript
getTextContentRect(): RectResult | undefined
```

Get the start and end positions of the text content.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If no text is entered, the return value contains the position information, but the size is 0.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_The position information is the offset of the first character relative to the editable area.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_For the Search component, the returned position information is the offset of the first character relative to the search icon in the component.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_If there is input, the width in the return value is the fixed width of the editable area.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getTextContentRect(): RectResult | undefined--><!--Device-TextContentControllerBase-getTextContentRect(): RectResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Text content rect.The unit of the return value is pixel. |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

Scroll the input field component to make the specified content visible.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-scrollToVisible(range?: TextRange): void--><!--Device-TextContentControllerBase-scrollToVisible(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The visible range. If the parameter is invalid, this method will have no effect. |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

Set the styled placeholder.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-setStyledPlaceholder(styledString: StyledString): void--><!--Device-TextContentControllerBase-setStyledPlaceholder(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The styledString for placeholder. If the parameter is invalid, this method will have no effect. |

