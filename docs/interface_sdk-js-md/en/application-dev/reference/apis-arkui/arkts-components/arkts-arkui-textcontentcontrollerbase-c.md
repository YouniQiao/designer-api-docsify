# TextContentControllerBase

TextContentControllerBase

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare abstract class TextContentControllerBase--><!--Device-unnamed-declare abstract class TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addText

```TypeScript
addText(text: string, textOperationOptions?: TextContentControllerOptions): number
```

Add a text.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextContentControllerBase-addText(text: string, textOperationOptions?: TextContentControllerOptions): number--><!--Device-TextContentControllerBase-addText(text: string, textOperationOptions?: TextContentControllerOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text value. |
| textOperationOptions | [TextContentControllerOptions](arkts-arkui-textcontentcontrolleroptions-i.md) | No | operation info. |

**Return value:**

| Type | Description |
| --- | --- |
| number | caret index |

## clearPreviewText

```TypeScript
clearPreviewText(): void
```

Clear the content of preview.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextContentControllerBase-clearPreviewText(): void--><!--Device-TextContentControllerBase-clearPreviewText(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

删除输入框文本末尾字符。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextContentControllerBase-deleteBackward(): void--><!--Device-TextContentControllerBase-deleteBackward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteText

```TypeScript
deleteText(range?: TextRange): void
```

Delete text in TextRange.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextContentControllerBase-deleteText(range?: TextRange): void--><!--Device-TextContentControllerBase-deleteText(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | No | range for deleting. |

## getCaretOffset

```TypeScript
getCaretOffset() : CaretOffset
```

Get the index and relative position of the CaretOffset.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;If this API is called when the caret position is updated in the current frame, it will not take effect.&lt;br&gt;For the Search component, the returned position information is the offset of the first character relative to the search icon in the component.&lt;br&gt;If no text is entered in the Search component,the return value contains the position information relative to the component.&lt;br&gt;The location information in the return value is the location of the caret relative to the editable component.&lt;/p&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextContentControllerBase-getCaretOffset() : CaretOffset--><!--Device-TextContentControllerBase-getCaretOffset() : CaretOffset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CaretOffset](../arkts-apis/arkts-arkui-common-caretoffset-i.md) | index and relative position of the CaretOffset. |

## getSelection

```TypeScript
getSelection(): TextRange
```

Gets the selected range of text content.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextContentControllerBase-getSelection(): TextRange--><!--Device-TextContentControllerBase-getSelection(): TextRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | range for selecting. |

## getTextContentLineCount

```TypeScript
getTextContentLineCount() : number
```

Get the lines number of the text content.The getTextContentLineCount type is used to obtain the number of lines of the edited text.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextContentControllerBase-getTextContentLineCount() : number--><!--Device-TextContentControllerBase-getTextContentLineCount() : number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Text content line count |

## getTextContentRect

```TypeScript
getTextContentRect() : RectResult
```

Get the start and end positions of the text content.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;If no text is entered, the return value contains the position information, but the size is 0.&lt;br&gt;The position information is the offset of the first character relative to the editable area.&lt;br&gt;For the Search component, the returned position information is the offset of the first character relative to the search icon in the component.&lt;br&gt;If there is input, the width in the return value is the fixed width of the editable area.&lt;/p&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextContentControllerBase-getTextContentRect() : RectResult--><!--Device-TextContentControllerBase-getTextContentRect() : RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](../arkts-apis/arkts-arkui-common-rectresult-i.md) | Text content rect.The unit of the return value is pixel. |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

将输入框文本滚动到可见区。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextContentControllerBase-scrollToVisible(range?: TextRange): void--><!--Device-TextContentControllerBase-scrollToVisible(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | No | 可见区范围。 若该参数非法，则本方法不会生效。 |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

设置提示文本的样式。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextContentControllerBase-setStyledPlaceholder(styledString: StyledString): void--><!--Device-TextContentControllerBase-setStyledPlaceholder(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | Yes | 设置提示文本样式的属性字符串 若传入的入参无效，则本接口不生效 |

