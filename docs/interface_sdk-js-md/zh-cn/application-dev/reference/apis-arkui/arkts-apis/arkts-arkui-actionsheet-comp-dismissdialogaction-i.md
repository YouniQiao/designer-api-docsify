# DismissDialogAction

```TypeScript
declare interface DismissDialogAction
```

弹窗关闭的信息。

**起始版本：** 12

<!--Device-unnamed-declare interface DismissDialogAction--><!--Device-unnamed-declare interface DismissDialogAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss: Callback<void>
```

弹窗关闭回调函数。开发者需要关闭弹窗时调用，不需要关闭时无需调用，弹窗保持打开。

**类型：** Callback&lt;void&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-DismissDialogAction-dismiss: Callback<void>--><!--Device-DismissDialogAction-dismiss: Callback<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

触发关闭弹窗的操作类型。开发者可根据reason判断用户的关闭操作，决定是否调用dismiss关闭弹窗。

**类型：** [DismissReason](../arkts-components/arkts-arkui-common-comp-dismissreason-e.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-DismissDialogAction-reason: DismissReason--><!--Device-DismissDialogAction-reason: DismissReason-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
