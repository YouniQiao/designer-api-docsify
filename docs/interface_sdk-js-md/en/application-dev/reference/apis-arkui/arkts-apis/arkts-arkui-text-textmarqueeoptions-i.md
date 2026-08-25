# TextMarqueeOptions

Defines the marquee options.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

The waiting time between each round of the marquee. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fadeout

```TypeScript
fadeout?: boolean
```

Set whether the text is faded out.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromStart

```TypeScript
fromStart?: boolean
```

The running direction of the marquee.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loop

```TypeScript
loop?: int
```

The rounds of the marquee. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marqueeStartPolicy

```TypeScript
marqueeStartPolicy?: MarqueeStartPolicy
```

The start policy for marquee.

**Type:** [MarqueeStartPolicy](arkts-arkui-text-marqueestartpolicy-e.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marqueeUpdatePolicy

```TypeScript
marqueeUpdatePolicy?: MarqueeUpdatePolicy
```

Marquee scrolling policy after text update. <p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute takes effect when the marquee is in the playing state and the text content width exceeds the width of the marquee component. Default value is MarqueeUpdatePolicy.DEFAULT. </p>

**Type:** [MarqueeUpdatePolicy](arkts-arkui-text-marqueeupdatepolicy-e.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spacing

```TypeScript
spacing?: LengthMetrics
```

The spacing between two rounds of marquee. <p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Default value is 48vp. </p>

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start: boolean
```

Is need start marquee.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: double
```

The step size of the marquee.

**Type:** double

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
