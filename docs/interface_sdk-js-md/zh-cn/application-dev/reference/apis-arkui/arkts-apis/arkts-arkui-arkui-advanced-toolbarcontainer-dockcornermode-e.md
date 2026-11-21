# DockCornerMode

```TypeScript
export enum DockCornerMode
```

定义浮动工具栏拖拽到角落时的吸附模式。

**起始版本：** 26.1.0

<!--Device-unnamed-export enum DockCornerMode--><!--Device-unnamed-export enum DockCornerMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## EXPAND

```TypeScript
EXPAND = 1
```

保持拖拽方向，不进行最小化。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-DockCornerMode-EXPAND = 1--><!--Device-DockCornerMode-EXPAND = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## MINIMIZE

```TypeScript
MINIMIZE = 0
```

吸附到角落并最小化；点击角落后跟随所在边缘。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-DockCornerMode-MINIMIZE = 0--><!--Device-DockCornerMode-MINIMIZE = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
