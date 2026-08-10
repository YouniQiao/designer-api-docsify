# DialogStyleOptions

固定样式对话框的选项。

**Inheritance/Implementation:** DialogStyleOptions extends [DialogBaseOptions](arkts-arkui-dialog-dialogbaseoptions-i.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

<!--Device-dialog-declare interface DialogStyleOptions extends DialogBaseOptions--><!--Device-dialog-declare interface DialogStyleOptions extends DialogBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DialogButtonOrientation, DialogState, DialogResult, DialogBaseController, DialogBaseAlignment, DialogDismissal } from 'kits/@kit.ArkUI';
```

## buttonDirection

```TypeScript
buttonDirection?: DialogButtonOrientation
```

按钮的排列。

**Type:** [DialogButtonOrientation](arkts-arkui-arkui-dialog-dialogbuttonorientation-e.md)

**Default:** DialogButtonOrientation.AUTO

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-buttonDirection?: DialogButtonOrientation--><!--Device-DialogStyleOptions-buttonDirection?: DialogButtonOrientation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttons

```TypeScript
buttons?: Array<DialogButton>
```

对话框中的按钮数组。提供时，对话框显示为带有按钮的警报样式对话框。与图纸一起使用时，按钮显示在图纸列表下方。

**Type:** Array&lt;DialogButton&gt;

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-buttons?: Array<DialogButton>--><!--Device-DialogStyleOptions-buttons?: Array<DialogButton>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gridCount

```TypeScript
gridCount?: int
```

对话框的网格计数。取值限定为整数。

**Type:** int

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-gridCount?: int--><!--Device-DialogStyleOptions-gridCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message?: DialogMessage
```

对话框的消息内容和文字样式。

**Type:** [DialogMessage](arkts-arkui-dialog-dialogmessage-i.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-message?: DialogMessage--><!--Device-DialogStyleOptions-message?: DialogMessage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sheets

```TypeScript
sheets?: Array<DialogSheet>
```

action-sheet样式的表单项数组。提供时，对话框将显示供用户选择的工作表项目。

**Type:** Array&lt;DialogSheet&gt;

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-sheets?: Array<DialogSheet>--><!--Device-DialogStyleOptions-sheets?: Array<DialogSheet>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subtitle

```TypeScript
subtitle?: ResourceStr
```

对话框的副标题。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-subtitle?: ResourceStr--><!--Device-DialogStyleOptions-subtitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

对话框标题。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogStyleOptions-title?: ResourceStr--><!--Device-DialogStyleOptions-title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

