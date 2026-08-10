# AlertDialogParamWithButtons

继承自[AlertDialogParam](arkts-arkui-alertdialog-alertdialogparam-i.md)。

**Inheritance/Implementation:** AlertDialogParamWithButtons extends [AlertDialogParam](arkts-arkui-alertdialog-alertdialogparam-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AlertDialogParamWithButtons extends AlertDialogParam--><!--Device-unnamed-export declare interface AlertDialogParamWithButtons extends AlertDialogParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
primaryButton: AlertDialogButtonBaseOptions
```

主要Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。 具体使用方式请参考  
[示例7](../../../reference/apis-arkui/arkui-ts/ts-methods-alert-dialog-box copy.md#示例7自定义背景模糊效果参数) 。

**Type:** [AlertDialogButtonBaseOptions](arkts-arkui-alertdialog-alertdialogbuttonbaseoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParamWithButtons-primaryButton: AlertDialogButtonBaseOptions--><!--Device-AlertDialogParamWithButtons-primaryButton: AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
secondaryButton: AlertDialogButtonBaseOptions
```

次要Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。

**Type:** [AlertDialogButtonBaseOptions](arkts-arkui-alertdialog-alertdialogbuttonbaseoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParamWithButtons-secondaryButton: AlertDialogButtonBaseOptions--><!--Device-AlertDialogParamWithButtons-secondaryButton: AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

