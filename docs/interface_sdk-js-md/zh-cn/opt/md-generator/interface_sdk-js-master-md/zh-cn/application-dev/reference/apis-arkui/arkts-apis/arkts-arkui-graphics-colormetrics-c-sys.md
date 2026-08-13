# ColorMetrics

提供颜色的统一表示与封装，支持颜色混合以及 RGB、Alpha 分量的获取。

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare class ColorMetrics--><!--Device-unnamed-declare class ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## createHDRColor

```TypeScript
static createHDRColor(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

使用ColorSpace和rgba格式颜色实例化支持HDR的ColorMetrics类。适用于无需调整曝光系数、直接指定HDR颜色分量的场景，如HDR纯色背景绘制、固定HDR色彩配置。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColor(colorSpace: ColorSpace, red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |
| red | number | 是 |
| green | number | 是 |
| blue | number | 是 |
| alpha | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## createHDRColorWithLinearExposure

```TypeScript
static createHDRColorWithLinearExposure(linearExposure: number, colorSpace: ColorSpace,
    red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

使用ColorSpace、线性曝光系数和rgba格式颜色实例化支持HDR的ColorMetrics类。如不需要通过曝光系数调节，可使用 [createHDRColor](#createHDRColor)直接设置RGB分量值大于1.0来呈现HDR效果。适用于需要按线性比例均匀调整HDR亮度的场景，如HDR图像预览、视频播放器色彩调 节。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColorWithLinearExposure(linearExposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linearExposure | number | 是 |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |
| red | number | 是 |
| green | number | 是 |
| blue | number | 是 |
| alpha | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## createHDRColorWithLogExposure

```TypeScript
static createHDRColorWithLogExposure(exposure: number, colorSpace: ColorSpace,
    red: number, green: number, blue: number, alpha?: number): ColorMetrics
```

使用ColorSpace、对数型曝光系数和rgba格式颜色实例化支持HDR的ColorMetrics类。与 [createHDRColorWithLinearExposure](#createHDRColorWithLinearExposure)相比，两者均通过曝光系数创建HDR色彩，区别在于本方法使 用对数型曝光系数（指数级增加曝光程度），后者使用线性曝光系数（线性增加曝光程度），开发者可根据所需的曝光调节方式选择。如不需要通过曝光系数调节，可使用 [createHDRColor](#createHDRColor)直接设置RGB分量值大于1.0来呈现HDR效果。适用于需要按对数关系调整HDR亮度（更贴近人眼感知）的场景，如HDR照片编辑、影 视后期调色。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics--><!--Device-ColorMetrics-static createHDRColorWithLogExposure(exposure: double, colorSpace: ColorSpace,    red: double, green: double, blue: double, alpha?: double): ColorMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [exposure](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenepostprocesssettings-tonemappingsettings-i.md) | number | 是 |
| colorSpace | [ColorSpace](arkts-arkui-window-colorspace-e.md) | 是 |
| red | number | 是 |
| green | number | 是 |
| blue | number | 是 |
| alpha | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md) |

## getBlueValue

```TypeScript
getBlueValue(): number
```

获取ColorMetrics颜色的B分量（蓝色）。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-getBlueValue(): double--><!--Device-ColorMetrics-getBlueValue(): double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

## getColorSpace

```TypeScript
getColorSpace(): ColorSpace
```

获取ColorMetrics的色彩空间。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-getColorSpace(): ColorSpace--><!--Device-ColorMetrics-getColorSpace(): ColorSpace-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [ColorSpace](arkts-arkui-window-colorspace-e.md) |

## getGreenValue

```TypeScript
getGreenValue(): number
```

获取ColorMetrics颜色的G分量（绿色）。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-getGreenValue(): double--><!--Device-ColorMetrics-getGreenValue(): double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

## getRedValue

```TypeScript
getRedValue(): number
```

获取ColorMetrics颜色的R分量（红色）。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-getRedValue(): double--><!--Device-ColorMetrics-getRedValue(): double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

## isHDR

```TypeScript
isHDR(): boolean
```

获取ColorMetrics是否呈现了HDR色彩。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ColorMetrics-isHDR(): boolean--><!--Device-ColorMetrics-isHDR(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |
