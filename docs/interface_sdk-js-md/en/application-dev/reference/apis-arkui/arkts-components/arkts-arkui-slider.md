# Slider

The **Slider** component is used to quickly adjust settings, such as the volume and brightness. > **NOTE**

## Child Components Not supported

## Slider

```TypeScript
Slider(options?: SliderOptions)
```

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SliderInterface-(options?: SliderOptions): SliderAttribute--><!--Device-SliderInterface-(options?: SliderOptions): SliderAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SliderOptions](arkts-arkui-slideroptions-i.md) | No | Parameters of the slider. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ColorMetricsStop](arkts-arkui-colormetricsstop-i.md) | Describes the breakpoint of the gradient color. |
| [SlideRange](arkts-arkui-sliderange-i.md) | Defines the callback type used in **SlideRange**. &gt; **NOTE：**&gt; &gt; - Currently, this API takes effect only when **min** ≤ **from** ≤ **to** ≤ **max** (the values of **min** and &gt; **max** do not depend on the values set, but on the actual values that take effect). &gt; &gt; - You can set either **from** or **to**, or you can set both **from** and **to**. &gt; &gt; - When the API is effective, if the set **from** value is between the adjacent multiples of **step**, then **from** &gt; takes the value of the left interval multiple of **step** or **min** as the corrected value. &gt; &gt; - When the API is effective, if the set **to** value is between the adjacent multiples of **step**, then **to** &gt; takes the value of the right interval multiple of **step** or **MAX** as the corrected value. &gt; &gt; - After **from** and **to** have taken their corrected values, when **value** is **undefined** or **null**, it &gt; takes the same value as **from**; when **value** is a number type, and if **value** ≤ **from**, then it takes &gt; **from**; if **value** &gt; **to**, then it takes **to**. |
| [SliderBlockStyle](arkts-arkui-sliderblockstyle-i.md) | Describes the style of the slider in the block direction. |
| [SliderConfiguration](arkts-arkui-sliderconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from CommonConfiguration. |
| [SliderCustomContentOptions](arkts-arkui-slidercustomcontentoptions-i.md) | Provides accessibility configuration of the slider prefix and suffix. |
| [SliderOptions](arkts-arkui-slideroptions-i.md) | Provides information about the slider. |
| [SliderPrefixOptions](arkts-arkui-sliderprefixoptions-i.md) | Provides accessibility configuration of the slider prefix. |
| [SliderShowStepOptions](arkts-arkui-slidershowstepoptions-i.md) | Provides accessibility text mapping for the slider step markers. |
| [SliderStepItemAccessibility](arkts-arkui-sliderstepitemaccessibility-i.md) | Provides accessibility configuration of the slider step markers. |
| [SliderSuffixOptions](arkts-arkui-slidersuffixoptions-i.md) | Provides accessibility configuration of the slider suffix. |

### Types

| Name | Description |
| --- | --- |
| [SliderTriggerChangeCallback](arkts-arkui-slidertriggerchangecallback-t.md) | Defines the callback type used in **SliderConfiguration**. |

### Enums

| Name | Description |
| --- | --- |
| [SliderBlockType](arkts-arkui-sliderblocktype-e.md) | Enumerates the types of the slider in the block direction. | Name | Value| Description | | ------- | -- | ---------------------- | | DEFAULT | 0 | Round slider. | | IMAGE | 1 | Slider with an image background. | | SHAPE | 2 | Slider in a custom shape.| |
| [SliderChangeMode](arkts-arkui-sliderchangemode-e.md) | Enumerates the slider states. |
| [SliderInteraction](arkts-arkui-sliderinteraction-e.md) | Interaction mode between the user and the slider. | Name | Value|Description | | ------ | -- | ----------------------------- | | SLIDE_AND_CLICK | 0 | Users can drag the slider or touch the track to move the slider. The slider moves as soon as the mouse or finger is pressed.| | SLIDE_ONLY | 1 | Users are not allowed to move the slider by touching the slider.| | SLIDE_AND_CLICK_UP | 2 |Users can drag the slider or touch the track to move the slider. The slider moves when the mouse is released or finger is lifted, if the release/lift position coincides with the screen press position.| |
| [SliderStyle](arkts-arkui-sliderstyle-e.md) | Enumerates the display styles of the slider thumb relative to the track. For details, see [How Are the Slider Thumb and Track of the Slider Component Aligned?](../../../ui/arkts-select-component-faq.md#how-are-the-slider-thumb-and-track-of-the-slider-component-aligned). &gt; **NOTE：**&gt; &gt; - By default, the slider has no padding. &gt; &gt; - For horizontal sliders, the default height is 40 vp, the width matches the parent container's width, and the &gt; track maintains center alignment. When **SliderStyle.OutSet** is used, it applies 9 vp (half of the &gt; blockSize value) margins on both left and right sides. When &gt; **SliderStyle.InSet** is used, it enforces 6 vp margins on both left and right sides. Custom padding values will be &gt; applied in addition to these default margins and will not override them. &gt; &gt; - For vertical sliders, the default width is 40 vp, the height matches the parent container's height, and the track &gt; maintains center alignment. When **SliderStyle.OutSet** is used, it applies 10 vp margins on both top and bottom &gt; sides. When **SliderStyle.InSet** is used, it enforces 6 vp margins on both top and bottom sides. Custom padding &gt; values will be applied in addition to these default margins and will not override them. |

