# PopoverDialog

跟手弹出框，基于目标组件位置弹出，上文中的TipsDialog、SelectDialog、ConfirmDialog、AlertDialog、LoadingDialog、CustomContentDialog都可作为弹出框内容。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare struct PopoverDialog--><!--Device-unnamed-export declare struct PopoverDialog-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialog-@Builder build(): void--><!--Device-PopoverDialog-@Builder build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## popover

```TypeScript
@Require @PropRef
  popover: PopoverOptions
```

配置跟手弹出框的参数。

**类型：** [PopoverOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvanceddialog-popoveroptions-i.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialog-@Require @PropRef  popover: PopoverOptions--><!--Device-PopoverDialog-@Require @PropRef  popover: PopoverOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
@Require @BuilderParam
  targetBuilder: () => void
```

跟手弹出框基于的目标组件。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialog-@Require @BuilderParam  targetBuilder: () => void--><!--Device-PopoverDialog-@Require @BuilderParam  targetBuilder: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
@Link visible: boolean
```

跟手弹出框显示状态。visible为true时，表示显示弹出框，visible为false时，表示隐藏弹出框。

默认值为false，隐藏弹出框。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PopoverDialog-@Link visible: boolean--><!--Device-PopoverDialog-@Link visible: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

