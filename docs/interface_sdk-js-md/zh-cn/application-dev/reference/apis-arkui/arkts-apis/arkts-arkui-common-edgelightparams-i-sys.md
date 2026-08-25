# EdgeLightParams（系统接口）

Defines the parameters of the edge light effect.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## color

```TypeScript
color?: ResourceColor
```

The color of the light effect. <br>If not specified, the default color is white (#FFFFFF).

**类型：** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**默认值：** #FFFFFF

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## intensity

```TypeScript
intensity?: double
```

The luminous intensity of the Edge Streamer effect. <br>Valid range: [0.0, 1.0].Default value is 1. <br>Value 0.0 means the light effect is completely invisible. <br>Value 1.0 means the light effect is at maximum brightness. <br>Values exceeding 1.0 will be clamped to 1.0. <br>Negative values are treated as 0.0.

**类型：** double

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## length

```TypeScript
length: Length
```

Projection length of the edge streamer along the flow direction. <br>Negative values are treated as 0.

**类型：** [Length](arkts-arkui-length-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## position

```TypeScript
position: EdgeLightPosition
```

The location of the edge light effect.

**类型：** [EdgeLightPosition](arkts-arkui-edgelightposition-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## thickness

```TypeScript
thickness?: Length
```

The thickness (width) of the light effect line. <br>Negative values are treated as 0. <br>If not specified, the default value is 0vp.

**类型：** [Length](arkts-arkui-length-t.md)

**默认值：** 0vp

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
