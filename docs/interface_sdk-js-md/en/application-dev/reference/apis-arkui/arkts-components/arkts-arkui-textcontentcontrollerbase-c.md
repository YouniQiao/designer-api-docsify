# TextContentControllerBase

Represents the base controller for **TextInput**, **TextArea**, and **Search** components.

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addText

```TypeScript
addText(text: string, textOperationOptions?: TextContentControllerOptions): number
```

Inserts text at a specified position in the editable content. If no position is specified, the text is appended to the end of the existing content.This API does not work when the text is being dragged.  
**addText** only affects the UI performance within the application and has no effect on the internal logic of the input method application. Therefore, avoid calling this API for the preview text.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| textOperationOptions | [TextContentControllerOptions](arkts-arkui-textcontentcontrolleroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## clearPreviewText

```TypeScript
clearPreviewText(): void
```

Notifies the input method to clear the current preview text.

> **NOTE：**&gt;
> When the controller is not bound to any component or the component bound to the controller is released, this interface does not take effect.

**Since:** 17

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

Deletes the character before the text cursor in the text box bound to the basic controller. If some text has been selected using the mouse or keyboard before this function is called, the selected text will be deleted.This API is not supported in preview display scenarios.

> **NOTE：**&gt;
> When the controller is not bound to any component or the component bound to the controller is released, this interface does not take effect.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteText

```TypeScript
deleteText(range?: TextRange): void
```

Deletes text within a specified range in the editable content.

> **NOTE：**&gt;
> - This API does not work when the text is being dragged.&gt;
> - **deleteText** only affects the UI performance within the application and has no effect on the internal logic
> of the input method application. Therefore, avoid calling this API for the preview text.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | No |

## getCaretOffset

```TypeScript
getCaretOffset() : CaretOffset
```

Obtains the position information of the caret.

> **NOTE：**&gt;
> - If this API is called when the caret position is updated in the current frame, it will not take effect.&gt;
> - For the **Search** component, the returned position information is the offset of the first character relative
> to the search icon in the component.&gt;
> - If no text is entered in the **Search** component, the return value contains the position information relative
> to the component.&gt;
> - The location information in the return value is the location of the caret relative to the editable component.&gt;
> - If the caret position cannot be obtained (for example, when the
> [TextInputController](arkts-arkui-textinputcontroller-c.md) is not bound to the TextInput component),
> **null** is returned.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CaretOffset](arkts-arkui-caretoffset-i.md) |

## getSelection

```TypeScript
getSelection(): TextRange
```

Obtains the current text selection range.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) |

## getTextContentLineCount

```TypeScript
getTextContentLineCount() : number
```

Obtains the number of lines of the edited text.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getTextContentRect

```TypeScript
getTextContentRect() : RectResult
```

Obtains the position of the edited text area relative to the component and its size. The unit of the return value is pixel.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectResult](arkts-arkui-rectresult-i.md) |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

Passes the start and end indexes to the bound text box components (**TextInput**, **TextArea**, and **Search**), and scrolls the text within the range to the visible area.

> **NOTE：**
> When the controller is not bound to any component or the component bound to the controller is released, this interface does not take effect.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | No |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

Binds or updates the styled placeholder string.

> **NOTE：**&gt;
> When the controller is not bound to any component or the component bound to the controller is released, this interface does not take effect.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styledString | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | Yes |
