# ConfirmDialogV2

信息确认类弹出框，操作未正确执行（如网络错误、电池电量过低），或未正确操作时（如指纹录入），反馈的错误或提示信息。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare struct ConfirmDialogV2--><!--Device-unnamed-export declare struct ConfirmDialogV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Builder  build(): void--><!--Device-ConfirmDialogV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## checkTips

```TypeScript
@Param
  checkTips?: ResourceStr
```

checkbox的提示内容。

默认不显示。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Param  checkTips?: ResourceStr--><!--Device-ConfirmDialogV2-@Param  checkTips?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## checked

```TypeScript
@Param
  checked?: boolean
```

checked为true时，表示checkbox已选中，为false时，表示未选中。

默认值：false

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Param  checked?: boolean--><!--Device-ConfirmDialogV2-@Param  checked?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Param
  content?: ResourceStr
```

确认弹出框内容。

默认不显示。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Param  content?: ResourceStr--><!--Device-ConfirmDialogV2-@Param  content?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onCheckedChange

```TypeScript
@Param
  onCheckedChange?: AdvancedDialogV2OnCheckedChange
```

checkbox的选中状态改变事件。

默认无事件。

**类型：** [AdvancedDialogV2OnCheckedChange](arkts-advanceddialogv2oncheckedchange-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Param  onCheckedChange?: AdvancedDialogV2OnCheckedChange--><!--Device-ConfirmDialogV2-@Param  onCheckedChange?: AdvancedDialogV2OnCheckedChange-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
@Param
  primaryButton?: AdvancedDialogV2Button
```

确认弹出框左侧按钮。

默认不显示。

**类型：** [AdvancedDialogV2Button](arkts-arkuiadvanceddialogv2-advanceddialogv2button-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Param  primaryButton?: AdvancedDialogV2Button--><!--Device-ConfirmDialogV2-@Param  primaryButton?: AdvancedDialogV2Button-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
@Param
  secondaryButton?: AdvancedDialogV2Button
```

确认弹出框右侧按钮。

默认不显示。

**类型：** [AdvancedDialogV2Button](arkts-arkuiadvanceddialogv2-advanceddialogv2button-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button--><!--Device-ConfirmDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Require
  @Param
  title: ResourceStr
```

确认弹出框标题。

**说明：** 标题超过两行会显示“...”。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConfirmDialogV2-@Require  @Param  title: ResourceStr--><!--Device-ConfirmDialogV2-@Require  @Param  title: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

