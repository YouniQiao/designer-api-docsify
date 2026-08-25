# CanvasGradient

OffscreenCanvas支持以下属性：

**起始版本：** 8

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## addColorStop

```TypeScript
addColorStop(offset: number, color: string): void
```

设置渐变断点值，包括偏移和颜色。调用多次addColorStop可设置多个断点，断点按offset值从小到大排序，渲染时在相邻断点间进行颜色插值。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| color | string | 是 |

## addColorStop

```TypeScript
addColorStop(offset: number, color: string | ColorMetrics): void
```

设置渐变断点值，包括偏移和颜色。支持设置rgb或argb格式颜色。支持通过传入[ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)类型设置P3广色域颜色值，从API版 本26.0.0开始，新增支持BT2020广色域和HDR提亮。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| color | string \| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [103701](../errorcode-canvas.md#103701-参数错误) |
