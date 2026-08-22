# PopoverDialogV2

跟手弹出框，基于目标组件位置弹出，上文中的TipsDialogV2、SelectDialogV2、ConfirmDialogV2、AlertDialogV2、LoadingDialogV2、CustomContentDialogV2都 可作为弹出框内容。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare struct PopoverDialogV2--><!--Device-unnamed-export declare struct PopoverDialogV2-End-->

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

<!--Device-PopoverDialogV2-@Builder  build(): void--><!--Device-PopoverDialogV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## $visible

```TypeScript
@Event
  $visible?: PopoverDialogV2OnVisibleChange
```

修改跟手弹出框的显示状态时触发的回调函数，建议在visible后使用!!语法设置双向同步。

默认无事件。

**类型：** [PopoverDialogV2OnVisibleChange](arkts-popoverdialogv2onvisiblechange-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialogV2-@Event  $visible?: PopoverDialogV2OnVisibleChange--><!--Device-PopoverDialogV2-@Event  $visible?: PopoverDialogV2OnVisibleChange-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## popover

```TypeScript
@Require
  @Param
  popover: PopoverDialogV2Options
```

配置跟手弹出框的参数。

**类型：** [PopoverDialogV2Options](arkts-arkuiadvanceddialogv2-popoverdialogv2options-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialogV2-@Require  @Param  popover: PopoverDialogV2Options--><!--Device-PopoverDialogV2-@Require  @Param  popover: PopoverDialogV2Options-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
@BuilderParam
  targetBuilder: CustomBuilder
```

跟手弹出框基于的目标组件。

**类型：** CustomBuilder

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialogV2-@BuilderParam  targetBuilder: CustomBuilder--><!--Device-PopoverDialogV2-@BuilderParam  targetBuilder: CustomBuilder-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
@Require
  @Param
  visible: boolean
```

跟手弹出框的显示状态。

值为true时跟手弹出框显示，为false时隐藏。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialogV2-@Require  @Param  visible: boolean--><!--Device-PopoverDialogV2-@Require  @Param  visible: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

