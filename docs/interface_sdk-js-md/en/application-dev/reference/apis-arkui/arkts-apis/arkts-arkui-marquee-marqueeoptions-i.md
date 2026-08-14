# MarqueeOptions

Defines Marquee constructor options. Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface MarqueeOptions--><!--Device-unnamed-export interface MarqueeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

The waiting time between each round of the marquee. Unit: ms. The value should be an integer. Default value: 0.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-delay?: int--><!--Device-MarqueeOptions-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fromStart

```TypeScript
fromStart?: boolean
```

Set text to scroll from the beginning or backward. Anonymous Object Rectification.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-fromStart?: boolean--><!--Device-MarqueeOptions-fromStart?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loop

```TypeScript
loop?: int
```

Set the number of times the scroll is repeated, infinite loop if it is less than or equal to zero. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is less than or equal to 0, the marquee will scroll continuously. <br>Regardless of the value, the marquee scrolls only once on an ArkTS widget. &lt;/p&gt;

**Type:** int

**Default:** -1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-loop?: int--><!--Device-MarqueeOptions-loop?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spacing

```TypeScript
spacing?: LengthMetrics
```

The spacing between two rounds of marquee. Default value is marquee width.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-spacing?: LengthMetrics--><!--Device-MarqueeOptions-spacing?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: string | undefined
```

Text that needs scrolling. In Marquee component, the default value is an empty string. Set to `undefined` will restore it to the default value. Anonymous Object Rectification.

**Type:** string \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-src: string | undefined--><!--Device-MarqueeOptions-src: string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start: boolean | undefined
```

Control whether the running lamp enters the playing state. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>&lt;em&gt;true&lt;/em&gt;: Start scrolling. <br>&lt;em&gt;false&lt;/em&gt;: Do not start scrolling. <br>This parameter cannot be used to restart scrolling that has been completed. <br>In Marquee component, the default value is false. Set to `undefined` will restore it to the default value. &lt;/p&gt;

**Type:** boolean \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-start: boolean | undefined--><!--Device-MarqueeOptions-start: boolean | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: double
```

Scroll animation text scroll step, when step is larger than the text width of Marquee, take the default value. Anonymous Object Rectification. Unit: vp. Default value: 6. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value is greater than the text width of the marquee, the default value is used. &lt;/p&gt;

**Type:** double

**Default:** 6

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MarqueeOptions-step?: double--><!--Device-MarqueeOptions-step?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

