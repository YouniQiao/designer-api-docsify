# ToolBarDockCallback

```TypeScript
export declare type ToolBarDockCallback = (area: DockArea, direction: Axis) => void
```

工具栏停靠到指定区域和方向时的回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-export declare type ToolBarDockCallback = (area: DockArea, direction: Axis) => void--><!--Device-unnamed-export declare type ToolBarDockCallback = (area: DockArea, direction: Axis) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| area | [DockArea](arkts-arkui-arkui-advanced-toolbarcontainer-dockarea-e.md) | 是 | 工具栏停靠的区域。 |
| direction | [Axis](arkts-arkui-axis-e.md) | 是 | 停靠方向。 |
