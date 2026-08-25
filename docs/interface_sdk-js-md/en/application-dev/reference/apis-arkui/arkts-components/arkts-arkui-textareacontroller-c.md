# TextAreaController

The controller for the **TextArea** component inherits from [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md). The APIs involved are as follows:<!--Del--> system API getText and other APIs like<!--DelEnd--> [getTextContentRect](arkts-arkui-textcontentcontrollerbase-c.md#gettextcontentrect), [getTextContentLineCount](arkts-arkui-textcontentcontrollerbase-c.md#gettextcontentlinecount), getCaretOffset, addText, [deleteText](arkts-arkui-textcontentcontrollerbase-c.md#deletetext), getSelection, [clearPreviewText](arkts-arkui-textcontentcontrollerbase-c.md#clearpreviewtext), setStyledPlaceholder, and deleteBackward.

## Objects to Import

```ts
controller: TextAreaController = new TextAreaController();
```

**Inheritance/Implementation:** TextAreaController extends [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md)

**Since:** 8

**System capability:** 
- API version 10 and later: SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## caretPosition

```TypeScript
caretPosition(value: number): void
```

Sets the position of the caret.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TextAreaController** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectionStart | number | Yes |
| selectionEnd | number | Yes |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | No |

## stopEditing

```TypeScript
stopEditing(): void
```

Exits the editing state.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
