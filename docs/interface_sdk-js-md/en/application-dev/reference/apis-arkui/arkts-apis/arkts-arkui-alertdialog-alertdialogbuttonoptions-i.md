# AlertDialogButtonOptions

继承自[AlertDialogButtonBaseOptions](arkts-arkui-alertdialog-alertdialogbuttonbaseoptions-i.md)。

**Inheritance/Implementation:** AlertDialogButtonOptions extends [AlertDialogButtonBaseOptions](arkts-arkui-alertdialog-alertdialogbuttonbaseoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AlertDialogButtonOptions extends AlertDialogButtonBaseOptions--><!--Device-unnamed-export declare interface AlertDialogButtonOptions extends AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primary

```TypeScript
primary?: boolean
```

在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。

默认值：false 

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogButtonOptions-primary?: boolean--><!--Device-AlertDialogButtonOptions-primary?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

