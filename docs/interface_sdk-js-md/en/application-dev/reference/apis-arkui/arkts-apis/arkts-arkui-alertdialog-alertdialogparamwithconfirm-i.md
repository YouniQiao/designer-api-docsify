# AlertDialogParamWithConfirm

继承自[AlertDialogParam](arkts-arkui-alertdialog-alertdialogparam-i.md)。

**Inheritance/Implementation:** AlertDialogParamWithConfirm extends [AlertDialogParam](arkts-arkui-alertdialog-alertdialogparam-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AlertDialogParamWithConfirm extends AlertDialogParam--><!--Device-unnamed-export declare interface AlertDialogParamWithConfirm extends AlertDialogParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## confirm

```TypeScript
confirm?: AlertDialogButtonBaseOptions
```

确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键。多重弹窗情况下，可自动获焦并连续响应。默认响应Enter键能力在defaultFocus为true时不生效。

**Type:** [AlertDialogButtonBaseOptions](arkts-arkui-alertdialog-alertdialogbuttonbaseoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParamWithConfirm-confirm?: AlertDialogButtonBaseOptions--><!--Device-AlertDialogParamWithConfirm-confirm?: AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

