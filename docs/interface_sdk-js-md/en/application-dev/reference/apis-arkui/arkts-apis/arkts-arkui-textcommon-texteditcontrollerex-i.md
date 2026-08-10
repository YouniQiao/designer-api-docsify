# TextEditControllerEx

文本扩展编辑控制器。

继承自[TextBaseController](arkts-arkui-textcommon-textbasecontroller-i.md)。

**Inheritance/Implementation:** TextEditControllerEx extends [TextBaseController](arkts-arkui-textcommon-textbasecontroller-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextEditControllerEx extends TextBaseController--><!--Device-unnamed-export declare interface TextEditControllerEx extends TextBaseController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): int | undefined
```

返回当前光标所在位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-getCaretOffset(): int | undefined--><!--Device-TextEditControllerEx-getCaretOffset(): int | undefined-End-->

**Return value:**

| Type | Description |
| --- | --- |
| int | 当前光标所在位置。 |

## getPreviewText

```TypeScript
getPreviewText(): PreviewText | undefined
```

获取预上屏信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-getPreviewText(): PreviewText | undefined--><!--Device-TextEditControllerEx-getPreviewText(): PreviewText | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewText](arkts-arkui-previewtext-i.md) | 预上屏信息。 |

## isEditing

```TypeScript
isEditing(): boolean | undefined
```

获取当前富文本的编辑状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-isEditing(): boolean | undefined--><!--Device-TextEditControllerEx-isEditing(): boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true为编辑态，false为非编辑态。 |

## setCaretOffset

```TypeScript
setCaretOffset(offset: int): boolean | undefined
```

设置光标偏移位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-setCaretOffset(offset: int): boolean | undefined--><!--Device-TextEditControllerEx-setCaretOffset(offset: int): boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | 光标偏移位置。超出所有内容范围时，设置失败。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 光标是否设置成功。&lt;br/&gt;true表示光标设置成功，false表示设置失败。 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextEditControllerEx-stopEditing(): void--><!--Device-TextEditControllerEx-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

