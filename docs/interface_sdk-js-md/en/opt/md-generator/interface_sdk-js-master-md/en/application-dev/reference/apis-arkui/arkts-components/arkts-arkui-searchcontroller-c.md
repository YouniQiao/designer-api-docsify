# SearchController

The controller for the **Search** component inherits from [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#textcontentcontrollerbase). The APIs involved are as follows:&lt;!--Del--&gt; system API getText and other APIs like&lt;!--DelEnd--&gt; [getTextContentRect](arkts-arkui-textcontentcontrollerbase-c.md#gettextcontentrect), [getTextContentLineCount](arkts-arkui-textcontentcontrollerbase-c.md#gettextcontentlinecount), getCaretOffset, addText, [deleteText](arkts-arkui-textcontentcontrollerbase-c.md#deletetext), getSelection, [clearPreviewText](arkts-arkui-textcontentcontrollerbase-c.md#clearpreviewtext), setStyledPlaceholder, and deleteBackward.

## Objects to Import ```ts controller: SearchController = new SearchController(); ```

**Inheritance/Implementation:** SearchController extends [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#textcontentcontrollerbase)

**Since:** 8

<!--Device-unnamed-declare class SearchController--><!--Device-unnamed-declare class SearchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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

<!--Device-SearchController-caretPosition(value: number): void--><!--Device-SearchController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **SearchController** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchController-constructor()--><!--Device-SearchController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

Sets the text selection range and highlights the selected text when the component is focused. This API works only when the value of **selectionStart** is less than that of **selectionEnd**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SearchController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-SearchController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

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

<!--Device-SearchController-stopEditing(): void--><!--Device-SearchController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
