# DisturbanceFieldOptions

Defines particle disturbance Field params.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface DisturbanceFieldOptions--><!--Device-unnamed-export declare interface DisturbanceFieldOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## feather

```TypeScript
feather?: int
```

Attenuation degree of the field from the center point to the field boundary. ranging from 0 to 100 integers. If 0, it indicates that the field is a rigid body, and all particles within the range will be excluded. a larger feather value indicates a greater degree of relaxation in the field, and more particles near the center point will appear in the field strength range. The default value is 0.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-feather?: int--><!--Device-DisturbanceFieldOptions-feather?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## noiseAmplitude

```TypeScript
noiseAmplitude?: double
```

NoiseAmplitude fluctuation range of noise, value,

**Type:** double

**Default:** 1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-noiseAmplitude?: double--><!--Device-DisturbanceFieldOptions-noiseAmplitude?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## noiseFrequency

```TypeScript
noiseFrequency?: double
```

Noise frequency with a value greater or equal 0.

**Type:** double

**Default:** 1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-noiseFrequency?: double--><!--Device-DisturbanceFieldOptions-noiseFrequency?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## noiseScale

```TypeScript
noiseScale?: double
```

Scaling parameter is used to control the overall size of noise, with a value greater or equal 0.

**Type:** double

**Default:** 1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-noiseScale?: double--><!--Device-DisturbanceFieldOptions-noiseScale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: PositionT<double>
```

Disturbance filed position width value x, y.

**Type:** [PositionT](arkts-na-positiont-t.md)&lt;double&gt;

**Default:** {x:0,y:0}

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-position?: PositionT<double>--><!--Device-DisturbanceFieldOptions-position?: PositionT<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: DisturbanceFieldShape
```

Disturbance filed shape.

**Type:** [DisturbanceFieldShape](arkts-na-particle-disturbancefieldshape-e.md)

**Default:** DisturbanceFieldShape.RECT

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-shape?: DisturbanceFieldShape--><!--Device-DisturbanceFieldOptions-shape?: DisturbanceFieldShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: SizeT<double>
```

Disturbance filed size width value width, height.

**Type:** [SizeT](arkts-na-graphics-sizet-i.md)&lt;double&gt;

**Default:** {width:0,height:0}

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-size?: SizeT<double>--><!--Device-DisturbanceFieldOptions-size?: SizeT<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strength

```TypeScript
strength?: double
```

Strength of the repulsive force from the center outward, with positive numbers indicating outward repulsion and negative numbers indicating inward attraction.

**Type:** double

**Default:** 0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DisturbanceFieldOptions-strength?: double--><!--Device-DisturbanceFieldOptions-strength?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

