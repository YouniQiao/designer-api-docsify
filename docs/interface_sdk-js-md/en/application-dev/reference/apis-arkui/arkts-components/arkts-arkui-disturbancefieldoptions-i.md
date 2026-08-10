# DisturbanceFieldOptions

设置粒子扰动场参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface DisturbanceFieldOptions--><!--Device-unnamed-declare interface DisturbanceFieldOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## feather

```TypeScript
feather?: number
```

羽化值，表示场从中心点到场边缘的衰减程度，取值范围0到100的整数，如果0则表示场是一个刚体，所有范围内的粒子都被排斥在外。羽化值越大场的缓和程度越大，场范围内出现越多靠近中心点的粒子。

默认值为0。

**Type:** number

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-feather?: number--><!--Device-DisturbanceFieldOptions-feather?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## noiseAmplitude

```TypeScript
noiseAmplitude?: number
```

噪声振幅，噪声的波动的范围，振幅越大噪音之间差异越大。取值大于等于0。

默认值1。

**Type:** number

**Default:** 1

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-noiseAmplitude?: number--><!--Device-DisturbanceFieldOptions-noiseAmplitude?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## noiseFrequency

```TypeScript
noiseFrequency?: number
```

噪声频率，频率越大噪声越细腻，取值大于等于0。

默认值1。

**Type:** number

**Default:** 1

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-noiseFrequency?: number--><!--Device-DisturbanceFieldOptions-noiseFrequency?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## noiseScale

```TypeScript
noiseScale?: number
```

噪声尺度，用于控制噪声图案的整体大小，取值大于等于0。

默认值1。

**Type:** number

**Default:** 1

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-noiseScale?: number--><!--Device-DisturbanceFieldOptions-noiseScale?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: PositionT<number>
```

场的位置。

默认值{x:0，y:0}。

x、y的取值范围：(-∞, +∞)。

**Type:** [PositionT](../arkts-apis/arkts-arkui-positiont-t.md)&lt;number&gt;

**Default:** {x:0,y:0}

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-position?: PositionT<number>--><!--Device-DisturbanceFieldOptions-position?: PositionT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: DisturbanceFieldShape
```

场的形状。

默认为DisturbanceFieldShape.RECT。

**Type:** [DisturbanceFieldShape](arkts-arkui-disturbancefieldshape-e.md)

**Default:** DisturbanceFieldShape.RECT

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-shape?: DisturbanceFieldShape--><!--Device-DisturbanceFieldOptions-shape?: DisturbanceFieldShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: SizeT<number>
```

场的大小。

默认值 {width:0，height:0}。

width和height的取值范围：[0, +∞)。

**Type:** [SizeT](../arkts-apis/arkts-arkui-graphics-sizet-i.md)&lt;number&gt;

**Default:** {width:0,height:0}

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-size?: SizeT<number>--><!--Device-DisturbanceFieldOptions-size?: SizeT<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strength

```TypeScript
strength?: number
```

场强，表示场从中心向外的排斥力的强度，默认值0。正数表示排斥力方向朝外，负数表示吸引力，方向朝内。

取值范围：(-∞, +∞)。

**Type:** number

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DisturbanceFieldOptions-strength?: number--><!--Device-DisturbanceFieldOptions-strength?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

