# TextEditControllerEx

Define the text extended editing controller.

**Inheritance/Implementation:** TextEditControllerEx extends [TextBaseController](arkts-arkui-textcommon-textbasecontroller-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextEditControllerEx extends TextBaseController--><!--Device-unnamed-export declare interface TextEditControllerEx extends TextBaseController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): int | undefined
```

Get caret offset from controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-getCaretOffset(): int | undefined--><!--Device-TextEditControllerEx-getCaretOffset(): int | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int |  |

## getPreviewText

```TypeScript
getPreviewText(): PreviewText | undefined
```

Get PreviewText.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-getPreviewText(): PreviewText | undefined--><!--Device-TextEditControllerEx-getPreviewText(): PreviewText | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewText](arkts-arkui-previewtext-i.md) | Return the PreviewText. |

## isEditing

```TypeScript
isEditing(): boolean | undefined
```

Judge whether is in editing state

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-isEditing(): boolean | undefined--><!--Device-TextEditControllerEx-isEditing(): boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true means that the component is in editing state, false means is non in editing status |

## setCaretOffset

```TypeScript
setCaretOffset(offset: int): boolean | undefined
```

Set caret offset.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-setCaretOffset(offset: int): boolean | undefined--><!--Device-TextEditControllerEx-setCaretOffset(offset: int): boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | caret offset. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return true if the caret offset was successfully set, false otherwise. |

## stopEditing

```TypeScript
stopEditing(): void
```

Stop editing state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-stopEditing(): void--><!--Device-TextEditControllerEx-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

