# TextContentControllerBase

TextContentControllerBase

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare abstract class TextContentControllerBase--><!--Device-unnamed-export declare abstract class TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addText

```TypeScript
addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined
```

Add a text.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined--><!--Device-TextContentControllerBase-addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text value. |
| textOperationOptions | [TextContentControllerOptions](arkts-na-common-textcontentcontrolleroptions-i.md) | No | operation info. |

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-clearPreviewText(): void--><!--Device-TextContentControllerBase-clearPreviewText(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

Delete the last character of the input field component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-deleteBackward(): void--><!--Device-TextContentControllerBase-deleteBackward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteText

```TypeScript
deleteText(range?: TextRange): void
```

Delete text in TextRange.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-deleteText(range?: TextRange): void--><!--Device-TextContentControllerBase-deleteText(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textrange-i.md) | No | range for deleting. |

## getCaretOffset

```TypeScript
getCaretOffset(): CaretOffset | undefined
```

Get the index and relative position of the CaretOffset. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this API is called when the caret position is updated in the current frame, it will not take effect. <br>For the Search component, the returned position information is the offset of the first character relative to the search icon in the component. <br>If no text is entered in the Search component, the return value contains the position information relative to the component. <br>The location information in the return value is the location of the caret relative to the editable component. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getCaretOffset(): CaretOffset | undefined--><!--Device-TextContentControllerBase-getCaretOffset(): CaretOffset | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CaretOffset](arkts-na-common-caretoffset-i.md) | index and relative position of the CaretOffset. |

## getSelection

```TypeScript
getSelection(): TextRange | undefined
```

Gets the selected range of text content.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getSelection(): TextRange | undefined--><!--Device-TextContentControllerBase-getSelection(): TextRange | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TextRange](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textrange-i.md) | range for selecting. |

## getTextContentLineCount

```TypeScript
getTextContentLineCount(): int | undefined
```

Get the lines number of the text content. The getTextContentLineCount type is used to obtain the number of lines of the edited text.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

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

Get the start and end positions of the text content. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If no text is entered, the return value contains the position information, but the size is 0. <br>The position information is the offset of the first character relative to the editable area. <br>For the Search component, the returned position information is the offset of the first character relative to the search icon in the component. <br>If there is input, the width in the return value is the fixed width of the editable area. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getTextContentRect(): RectResult | undefined--><!--Device-TextContentControllerBase-getTextContentRect(): RectResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](arkts-na-common-rectresult-i.md) | Text content rect.The unit of the return value is pixel. |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

Scroll the input field component to make the specified content visible.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-scrollToVisible(range?: TextRange): void--><!--Device-TextContentControllerBase-scrollToVisible(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textrange-i.md) | No | The visible range. If the parameter is invalid, this method will have no effect. |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

Set the styled placeholder.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-setStyledPlaceholder(styledString: StyledString): void--><!--Device-TextContentControllerBase-setStyledPlaceholder(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-styledstring-c.md) | Yes | The styledString for placeholder. If the parameter is invalid, this method will have no effect. |

