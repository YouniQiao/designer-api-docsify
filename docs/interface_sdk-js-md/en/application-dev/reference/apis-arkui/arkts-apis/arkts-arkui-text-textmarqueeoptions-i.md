# TextMarqueeOptions

Defines the marquee options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface TextMarqueeOptions--><!--Device-unnamed-export declare interface TextMarqueeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

The waiting time between each round of the marquee. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-delay?: int--><!--Device-TextMarqueeOptions-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fadeout

```TypeScript
fadeout?: boolean
```

Set whether the text is faded out.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-fadeout?: boolean--><!--Device-TextMarqueeOptions-fadeout?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromStart

```TypeScript
fromStart?: boolean
```

The running direction of the marquee.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-fromStart?: boolean--><!--Device-TextMarqueeOptions-fromStart?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loop

```TypeScript
loop?: int
```

The rounds of the marquee. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-loop?: int--><!--Device-TextMarqueeOptions-loop?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marqueeStartPolicy

```TypeScript
marqueeStartPolicy?: MarqueeStartPolicy
```

The start policy for marquee.

**Type:** [MarqueeStartPolicy](arkts-arkui-text-marqueestartpolicy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-marqueeStartPolicy?: MarqueeStartPolicy--><!--Device-TextMarqueeOptions-marqueeStartPolicy?: MarqueeStartPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marqueeUpdatePolicy

```TypeScript
marqueeUpdatePolicy?: MarqueeUpdatePolicy
```

Marquee scrolling policy after text update. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;This attribute takes effect when the marquee is in the playing state and the text content width exceeds the width of the marquee component. Default value is MarqueeUpdatePolicy.DEFAULT. &lt;/p&gt;

**Type:** [MarqueeUpdatePolicy](arkts-arkui-text-marqueeupdatepolicy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-marqueeUpdatePolicy?: MarqueeUpdatePolicy--><!--Device-TextMarqueeOptions-marqueeUpdatePolicy?: MarqueeUpdatePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spacing

```TypeScript
spacing?: LengthMetrics
```

The spacing between two rounds of marquee. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;Default value is 48vp. &lt;/p&gt;

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-spacing?: LengthMetrics--><!--Device-TextMarqueeOptions-spacing?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start: boolean
```

Is need start marquee.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-start: boolean--><!--Device-TextMarqueeOptions-start: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: double
```

The step size of the marquee.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMarqueeOptions-step?: double--><!--Device-TextMarqueeOptions-step?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

