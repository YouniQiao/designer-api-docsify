# TextContentControllerBase

TextContentControllerBase

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addText

```TypeScript
addText(text: string, textOperationOptions?: TextContentControllerOptions): int | undefined
```

Add a text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| textOperationOptions | [TextContentControllerOptions](arkts-arkui-common-textcontentcontrolleroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| int \| undefined |

## clearPreviewText

```TypeScript
clearPreviewText(): void
```

Clear the content of preview.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

Delete the last character of the input field component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## deleteText

```TypeScript
deleteText(range?: TextRange): void
```

Delete text in TextRange.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 否 |

## getCaretOffset

```TypeScript
getCaretOffset(): CaretOffset | undefined
```

Get the index and relative position of the CaretOffset.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this API is called when the caret position is updated in the current frame, it will not take effect. <br>For the Search component, the returned position information is the offset of the first character relative to the search icon in the component. <br>If no text is entered in the Search component, the return value contains the position information relative to the component. <br>The location information in the return value is the location of the caret relative to the editable component. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [CaretOffset](arkts-arkui-common-caretoffset-i.md) \| undefined |

## getSelection

```TypeScript
getSelection(): TextRange | undefined
```

Gets the selected range of text content.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [TextRange](arkts-arkui-textcommon-textrange-i.md) \| undefined |

## getTextContentLineCount

```TypeScript
getTextContentLineCount(): int | undefined
```

Get the lines number of the text content. The getTextContentLineCount type is used to obtain the number of lines of the edited text.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| int \| undefined |

## getTextContentRect

```TypeScript
getTextContentRect(): RectResult | undefined
```

Get the start and end positions of the text content.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If no text is entered, the return value contains the position information, but the size is 0. <br>The position information is the offset of the first character relative to the editable area. <br>For the Search component, the returned position information is the offset of the first character relative to the search icon in the component. <br>If there is input, the width in the return value is the fixed width of the editable area. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RectResult](arkts-arkui-common-rectresult-i.md) \| undefined |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

Scroll the input field component to make the specified content visible.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [TextRange](arkts-arkui-textcommon-textrange-i.md) | 否 |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

Set the styled placeholder.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | 是 |
