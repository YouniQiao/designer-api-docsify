# ToolBarStateCallback

```TypeScript
export declare type ToolBarStateCallback = (state: ToolBarState) => void
```

工具栏状态变化时的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-export declare type ToolBarStateCallback = (state: ToolBarState) => void--><!--Device-unnamed-export declare type ToolBarStateCallback = (state: ToolBarState) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [ToolBarState](arkts-arkui-arkui-advanced-toolbarcontainer-toolbarstate-e.md) | 是 | 当前工具栏状态。 |
