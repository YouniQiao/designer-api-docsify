# DismissDialogAction

Dialog关闭的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DismissDialogAction--><!--Device-unnamed-export declare interface DismissDialogAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss(): void
```

Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用此函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissDialogAction-dismiss(): void--><!--Device-DismissDialogAction-dismiss(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

Reason why the dialog box cannot be dismissed. You must specify whether to close the dialog box for each of the listed actions.

**Type:** [DismissReason](../arkts-components/arkts-arkui-dismissreason-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissDialogAction-reason: DismissReason--><!--Device-DismissDialogAction-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

