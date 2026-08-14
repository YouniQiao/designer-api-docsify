# SliderOptions

Parameters of the slider.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface SliderOptions--><!--Device-unnamed-export declare interface SliderOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: Axis
```

Whether the slider moves horizontally or vertically.

**Type:** [Axis](../../apis-arkui/arkts-apis/arkts-arkui-axis-e.md)

**Default:** Axis.Horizontal

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-direction?: Axis--><!--Device-SliderOptions-direction?: Axis-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## max

```TypeScript
max?: double
```

Maximum value. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the value of min is greater than or equal to the value of max, the min value defaults to 0, and the max value defaults to 100. If the value is not within the [min, max] range, the value of min or max is used, whichever is closer. &lt;/p&gt;

**Type:** double

**Default:** 100

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-max?: double--><!--Device-SliderOptions-max?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## min

```TypeScript
min?: double
```

Minimum value.

**Type:** double

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-min?: double--><!--Device-SliderOptions-min?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reverse

```TypeScript
reverse?: boolean
```

Whether the slider values are reversed. By default, the values increase from left to right for a horizontal slider and from top to bottom for a vertical slider.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-reverse?: boolean--><!--Device-SliderOptions-reverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## step

```TypeScript
step?: double
```

Step of the slider. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If this parameter is set to a value less than 0 or greater than the value of max, the default value is used. &lt;/p&gt;

**Type:** double

**Default:** 1 - Value range: [0.01, max - min]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-step?: double--><!--Device-SliderOptions-step?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: SliderStyle
```

Style of the slider thumb and track.

**Type:** [SliderStyle](arkts-na-slider-sliderstyle-e.md)

**Default:** SliderStyle.OutSet

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-style?: SliderStyle--><!--Device-SliderOptions-style?: SliderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: double | undefined | Bindable<double>
```

Current value of Slider.

**Type:** double \| undefined \| [Bindable](arkts-na-common-bindable-i.md)&lt;double&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderOptions-value?: double | undefined | Bindable<double>--><!--Device-SliderOptions-value?: double | undefined | Bindable<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

