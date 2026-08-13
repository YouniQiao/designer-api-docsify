# EdgeLightParams (System API)

Defines the parameters of the edge light effect.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface EdgeLightParams--><!--Device-unnamed-export declare interface EdgeLightParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## color

```TypeScript
color?: ResourceColor
```

The color of the light effect. &lt;br&gt;If not specified, the default color is white (#FFFFFF).

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #FFFFFF

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-color?: ResourceColor--><!--Device-EdgeLightParams-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## intensity

```TypeScript
intensity?: double
```

The luminous intensity of the Edge Streamer effect. &lt;br&gt;Valid range: [0.0, 1.0].Default value is 1. &lt;br&gt;Value 0.0 means the light effect is completely invisible. &lt;br&gt;Value 1.0 means the light effect is at maximum brightness. &lt;br&gt;Values exceeding 1.0 will be clamped to 1.0. &lt;br&gt;Negative values are treated as 0.0.

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-intensity?: double--><!--Device-EdgeLightParams-intensity?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## length

```TypeScript
length: Length
```

Projection length of the edge streamer along the flow direction. &lt;br&gt;Negative values are treated as 0.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-length: Length--><!--Device-EdgeLightParams-length: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## position

```TypeScript
position: EdgeLightPosition
```

The location of the edge light effect.

**Type:** [EdgeLightPosition](../../apis-arkui/arkts-apis/arkts-arkui-edgelightposition-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-position: EdgeLightPosition--><!--Device-EdgeLightParams-position: EdgeLightPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## thickness

```TypeScript
thickness?: Length
```

The thickness (width) of the light effect line. &lt;br&gt;Negative values are treated as 0. &lt;br&gt;If not specified, the default value is 0vp.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Default:** 0vp

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EdgeLightParams-thickness?: Length--><!--Device-EdgeLightParams-thickness?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

