# ActionSheet

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 26.0.0

**替代接口：** [showActionSheet](arkts-arkui-arkui-uicontext-uicontext-c.md#showactionsheet)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## show

```TypeScript
static show(value: ActionSheetOptions)
```

定义列表弹窗并弹出。

> **说明：**
showActionSheet需先获取[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)实例后再进行调用。

> 从API version 10开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [showActionSheet](arkts-arkui-arkui-uicontext-uicontext-c.md#showactionsheet)来明确UI的执行上下文。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 18

**替代接口：** [showActionSheet](arkts-arkui-arkui-uicontext-uicontext-c.md#showactionsheet)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ActionSheetOptions](arkts-arkui-actionsheetoptions-i.md) | 是 |
