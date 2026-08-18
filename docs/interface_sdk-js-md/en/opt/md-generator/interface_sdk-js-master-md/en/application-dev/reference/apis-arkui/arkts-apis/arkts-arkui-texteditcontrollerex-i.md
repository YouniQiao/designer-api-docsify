# TextEditControllerEx

Implements an extended text editing controller. Inherits [TextBaseController](arkts-arkui-textbasecontroller-i.md#textbasecontroller).

**Inheritance/Implementation:** TextEditControllerEx extends [TextBaseController](arkts-arkui-textbasecontroller-i.md#textbasecontroller)

**Since:** 12

<!--Device-unnamed-declare interface TextEditControllerEx--><!--Device-unnamed-declare interface TextEditControllerEx-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getCaretOffset

```TypeScript
getCaretOffset(): number
```

Obtains the current position of the caret.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextEditControllerEx-getCaretOffset(): number--><!--Device-TextEditControllerEx-getCaretOffset(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getPreviewText

```TypeScript
getPreviewText?(): PreviewText
```

Obtains the preview text.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextEditControllerEx-getPreviewText?(): PreviewText--><!--Device-TextEditControllerEx-getPreviewText?(): PreviewText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PreviewText](arkts-arkui-previewtext-i.md) |

## isEditing

```TypeScript
isEditing(): boolean
```

Obtains the editing status of the rich text.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextEditControllerEx-isEditing(): boolean--><!--Device-TextEditControllerEx-isEditing(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setCaretOffset

```TypeScript
setCaretOffset(offset: number): boolean
```

Sets the offset of the caret.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextEditControllerEx-setCaretOffset(offset: number): boolean--><!--Device-TextEditControllerEx-setCaretOffset(offset: number): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## stopEditing

```TypeScript
stopEditing(): void
```

Stops editing.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextEditControllerEx-stopEditing(): void--><!--Device-TextEditControllerEx-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
