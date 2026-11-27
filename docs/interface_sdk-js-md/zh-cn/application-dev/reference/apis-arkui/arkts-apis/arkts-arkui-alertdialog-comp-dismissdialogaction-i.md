# DismissDialogAction

```TypeScript
declare interface DismissDialogAction
```

Dialog关闭的信息。

**起始版本：** 12

<!--Device-unnamed-declare interface DismissDialogAction--><!--Device-unnamed-declare interface DismissDialogAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss: Callback<void>
```

Dialog关闭回调函数。调用此方法将允许弹窗关闭；不调用此方法将阻拦弹窗关闭。开发者可根据reason判断后，如需关闭则调用dismiss()，如需拦截则不调用。

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

触发本次拦截弹窗关闭的操作类型。开发者可根据reason的值判断是否调用dismiss()来允许关闭弹窗。

**类型：** [DismissReason](../arkts-components/arkts-arkui-common-comp-dismissreason-e.md)

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-DismissDialogAction-reason: DismissReason--><!--Device-DismissDialogAction-reason: DismissReason-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
