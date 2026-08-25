# ImageAttribute

属性的详细使用指导请参考 [添加属性](../../../ui/arkts-graphics-display.md#添加属性)。除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface ImageAttribute

**继承/实现关系：** ImageAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## analyzerConfig

```TypeScript
default analyzerConfig(config: ImageAnalyzerConfig | undefined): this
```

设置AI分析类型，包括主体识别和文字识别功能，默认全部开启。分析类型不支持动态修改。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ImageAnalyzerConfig](arkts-arkui-imagecommon-imageanalyzerconfig-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## edgeAntialiasing

```TypeScript
default edgeAntialiasing(value: double | undefined): this
```

设置SVG图源抗锯齿效果，仅对SVG图源生效。取值范围为\$(0.333, 1.333]\$，有效数字保留小数点后3位。适用于超低分辨率设备（PPI低于200的设备）的SVG图源的锯齿优化，存在一定的性能影响，请谨慎使用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## enhancedImageQuality

```TypeScript
default enhancedImageQuality(imageQuality: ResolutionQuality | undefined): this
```

设置图像解码时的图像解码分辨率选项。该属性不支持 svg、[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)和 DrawableDescriptor 等非解码图片类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageQuality | [ResolutionQuality](arkts-arkui-resolutionquality-t-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## pointLight

```TypeScript
default pointLight(value: PointLightStyle | undefined): this
```

设置点光源样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PointLightStyle](../arkts-components/arkts-arkui-pointlightstyle-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |
