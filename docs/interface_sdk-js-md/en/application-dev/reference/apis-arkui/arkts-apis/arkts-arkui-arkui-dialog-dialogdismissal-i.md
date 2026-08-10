# DialogDismissal

提供有关关闭对话框的操作的信息。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

<!--Device-unnamed-export interface DialogDismissal--><!--Device-unnamed-export interface DialogDismissal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DialogButtonOrientation, DialogState, DialogResult, DialogBaseController, DialogBaseAlignment, DialogDismissal } from 'kits/@kit.ArkUI';
```

## dismiss

```TypeScript
dismiss: VoidCallback
```

关闭对话框的回调。只有当需要退出对话框时，才会调用此接口。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogDismissal-dismiss: VoidCallback--><!--Device-DialogDismissal-dismiss: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

无法关闭对话框的原因。

**Type:** [DismissReason](../arkts-components/arkts-arkui-dismissreason-e.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-DialogDismissal-reason: DismissReason--><!--Device-DialogDismissal-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

