# AlertDialogV2

操作确认类弹出框。当触发一个将产生严重后果的不可逆操作时，如删除、重置、取消编辑、停止等，会触发该类弹出框提示。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare struct AlertDialogV2--><!--Device-unnamed-export declare struct AlertDialogV2-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlertDialogV2-@Builder  build(): void--><!--Device-AlertDialogV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Require
  @Param
  content: ResourceStr
```

确认弹出框内容。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlertDialogV2-@Require  @Param  content: ResourceStr--><!--Device-AlertDialogV2-@Require  @Param  content: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
@Param
  primaryButton?: AdvancedDialogV2Button
```

确认弹出框左侧按钮。

默认不显示。

**类型：** [AdvancedDialogV2Button](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlertDialogV2-@Param  primaryButton?: AdvancedDialogV2Button--><!--Device-AlertDialogV2-@Param  primaryButton?: AdvancedDialogV2Button-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Param
  primaryTitle?: ResourceStr
```

确认弹出框一级标题。

默认不显示。

**说明：** 标题超过两行会显示“...”。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlertDialogV2-@Param  primaryTitle?: ResourceStr--><!--Device-AlertDialogV2-@Param  primaryTitle?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
@Param
  secondaryButton?: AdvancedDialogV2Button
```

确认弹出框右侧按钮。

默认不显示。

**类型：** [AdvancedDialogV2Button](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlertDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button--><!--Device-AlertDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Param
  secondaryTitle?: ResourceStr
```

确认弹出框二级标题。

默认不显示。

**说明：** 标题超过两行会显示“...”。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlertDialogV2-@Param  secondaryTitle?: ResourceStr--><!--Device-AlertDialogV2-@Param  secondaryTitle?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

