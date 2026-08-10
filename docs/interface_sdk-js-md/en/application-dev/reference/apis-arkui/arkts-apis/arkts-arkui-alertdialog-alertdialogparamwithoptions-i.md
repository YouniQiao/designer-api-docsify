# AlertDialogParamWithOptions

继承自[AlertDialogParam](arkts-arkui-alertdialog-alertdialogparam-i.md)。

**Inheritance/Implementation:** AlertDialogParamWithOptions extends [AlertDialogParam](arkts-arkui-alertdialog-alertdialogparam-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AlertDialogParamWithOptions extends AlertDialogParam--><!--Device-unnamed-export declare interface AlertDialogParamWithOptions extends AlertDialogParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonDirection

```TypeScript
buttonDirection?: DialogButtonDirection
```

按钮排布方向默认为DialogButtonDirection.AUTO。建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮）。非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。

**Type:** [DialogButtonDirection](arkts-arkui-alertdialog-dialogbuttondirection-e.md)

**Default:** DialogButtonDirection.AUTO

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParamWithOptions-buttonDirection?: DialogButtonDirection--><!--Device-AlertDialogParamWithOptions-buttonDirection?: DialogButtonDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttons

```TypeScript
buttons: Array<AlertDialogButtonOptions>
```

弹窗容器中的多个按钮。

**Type:** Array&lt;AlertDialogButtonOptions&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlertDialogParamWithOptions-buttons: Array<AlertDialogButtonOptions>--><!--Device-AlertDialogParamWithOptions-buttons: Array<AlertDialogButtonOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

