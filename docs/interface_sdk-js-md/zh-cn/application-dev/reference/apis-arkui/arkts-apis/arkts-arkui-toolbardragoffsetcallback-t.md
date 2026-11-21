# ToolBarDragOffsetCallback

```TypeScript
export declare type ToolBarDragOffsetCallback = (x: number, y: number) => void
```

相对于ToolBarContainer容器的拖拽偏移量回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-export declare type ToolBarDragOffsetCallback = (x: number, y: number) => void--><!--Device-unnamed-export declare type ToolBarDragOffsetCallback = (x: number, y: number) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | X轴偏移量，单位为vp。 |
| y | number | 是 | Y轴偏移量，单位为vp。 |
