# ColorMetrics

提供颜色的统一表示与封装，支持颜色混合以及 RGB、Alpha 分量的获取。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## autoRefresh

```TypeScript
autoRefresh?(value: boolean): ColorMetrics
```

设置ColorMetrics对象是否跟随系统配置变化自动更新。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## blendColor

```TypeScript
blendColor(overlayColor: ColorMetrics): ColorMetrics
```

在当前颜色的上方叠加上一层指定的颜色（overlayColor），并返回混合后的新颜色。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| overlayColor | [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## colorWithSpace

```TypeScript
static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

使用ColorSpace和rgba格式颜色实例化ColorMetrics类。仅red、green、blue属性支持在display-p3色彩空间中设置颜色，alpha属性不受色彩空间影响。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |
| [red](#red) | number | 是 |
| [green](#green) | number | 是 |
| [blue](#blue) | number | 是 |
| [alpha](#alpha) | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## numeric

```TypeScript
static numeric(value: number): ColorMetrics
```

使用HEX格式颜色实例化 ColorMetrics 类。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## resourceColor

```TypeScript
static resourceColor(color: ResourceColor): ColorMetrics
```

使用资源格式颜色实例化 ColorMetrics 类。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [color](#color) | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [180003](../errorcode-event.md#180003-该事件不是克隆事件) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## rgba

```TypeScript
static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

使用rgb或者rgba格式颜色实例化 ColorMetrics 类。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [red](#red) | number | 是 |
| [green](#green) | number | 是 |
| [blue](#blue) | number | 是 |
| [alpha](#alpha) | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## alpha

```TypeScript
get alpha(): number
```

获取ColorMetrics颜色的A分量（透明度）。

**类型：** number

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## blue

```TypeScript
get blue(): number
```

获取ColorMetrics颜色的B分量（蓝色）。

**类型：** number

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
get color(): string
```

获取ColorMetrics的颜色，返回的是rgba字符串的格式。

**类型：** string

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## green

```TypeScript
get green(): number
```

获取ColorMetrics颜色的G分量（绿色）。

**类型：** number

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## red

```TypeScript
get red(): number
```

获取ColorMetrics颜色的R分量（红色）。

**类型：** number

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
