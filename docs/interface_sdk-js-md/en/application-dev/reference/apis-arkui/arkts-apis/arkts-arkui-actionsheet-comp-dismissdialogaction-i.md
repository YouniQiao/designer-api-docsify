# DismissDialogAction

```TypeScript
declare interface DismissDialogAction
```

Defines the information about the dialog box dismissal.

**Since:** 12

<!--Device-unnamed-declare interface DismissDialogAction--><!--Device-unnamed-declare interface DismissDialogAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss: Callback<void>
```

Callback for the dialog box dismiss event. The developer calls it when the dialog box needs to be closed. If the dialog box does not need to be closed, it is not called, and the dialog box remains open.

**Type:** Callback&lt;void&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissDialogAction-dismiss: Callback<void>--><!--Device-DismissDialogAction-dismiss: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

Type of the operation that triggers closing of the dialog box. The developer can determine the user's closing operation based on **reason** and decide whether to call **dismiss** to close the dialog box.

**Type:** [DismissReason](../arkts-components/arkts-arkui-common-comp-dismissreason-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissDialogAction-reason: DismissReason--><!--Device-DismissDialogAction-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
