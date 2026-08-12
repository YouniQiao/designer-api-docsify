# TextInputController

The controller for the **TextInput** component inherits from  
[TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#TextContentControllerBase). The APIs involved are as follows:&lt;!--Del--&gt; system API  
[getText](TextContentControllerBase#getText) and other APIs like&lt;!--DelEnd--&gt;  
[getTextContentRect](arkts-arkui-textcontentcontrollerbase-c.md#getTextContentRect),  
[getTextContentLineCount](arkts-arkui-textcontentcontrollerbase-c.md#getTextContentLineCount),  
[getCaretOffset](TextContentControllerBase#getCaretOffset), [addText](TextContentControllerBase#addText),  
[deleteText](arkts-arkui-textcontentcontrollerbase-c.md#deleteText),  
[getSelection](TextContentControllerBase#getSelection),  
[clearPreviewText](arkts-arkui-textcontentcontrollerbase-c.md#clearPreviewText),  
[setStyledPlaceholder](TextContentControllerBase#setStyledPlaceholder), and  
[deleteBackward](TextContentControllerBase#deleteBackward).

## Objects to Import

```ts controller: TextInputController = new TextInputController();```

**Inheritance/Implementation:** TextInputController extends [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#TextContentControllerBase)

**Since:** 8

<!--Device-unnamed-declare class TextInputController extends TextContentControllerBase--><!--Device-unnamed-declare class TextInputController extends TextContentControllerBase-End-->

**System capability:** 
- API version 10 and later: SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

Sets the position of the caret. If the value is less than 0, the value **0** is used. If the value exceeds the text length, the caret is placed at the end of the text.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-caretPosition(value: number): void--><!--Device-TextInputController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **TextInputController** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-constructor()--><!--Device-TextInputController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

Sets the text selection area, which will be highlighted.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-TextInputController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

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

<!--Device-TextInputController-stopEditing(): void--><!--Device-TextInputController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
