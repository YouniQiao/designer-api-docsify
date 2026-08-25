# CanvasGradient

渐变对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: double, color: string | ColorMetrics): void
```

设置渐变断点值，包括偏移和颜色。支持设置rgb或者argb格式颜色。支持通过传入 [ColorMetrics](../../../reference/apis-arkui/js-apis-arkui-graphics.md#colormetrics12) 类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | double | 是 |
| color | string \| [ColorMetrics](arkts-arkui-colormetrics-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [103701](../errorcode-canvas.md#103701-参数错误) |
