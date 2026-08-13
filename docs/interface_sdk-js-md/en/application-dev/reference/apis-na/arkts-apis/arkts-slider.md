# slider

## Summary

### Functions

| Name | Description |
| --- | --- |
| [Slider](arkts-na-slider-slider-f.md#Slider) | Defines Slider Component. |

### Classes

| Name | Description |
| --- | --- |
| [ColorMetricsLinearGradient](arkts-na-slider-colormetricslineargradient-c.md) | ColorMetricsLinearGradient class |

### Interfaces

| Name | Description |
| --- | --- |
| [ColorMetricsStop](arkts-na-slider-colormetricsstop-i.md) | ColorMetricsStop type |
| [SlideRange](arkts-na-slider-sliderange-i.md) | Defines the callback type used in SlideRange. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;Currently, this API takes effect only when MIN ≤ from ≤ to ≤ MAX (the values of MIN and MAX do not depend on the values set, but on the actual values that take effect). You can set either from or to, or you can set both from and to. When the API is effective, if the set from value is between the adjacent multiples of step, then from takes the value of the left interval multiple of step or MIN as the corrected value. When the API is effective, if the set to value is between the adjacent multiples of step, then to takes the value of the right interval multiple of step or MAX as the corrected value. After from and to have taken their corrected values, when value is undefined or null, it takes the same value as from; when value is a number type, and if value ≤ from, then it takes from; if value > to, then it takes to. &lt;/p&gt; |
| [SliderAttribute](arkts-na-slider-sliderattribute-i.md) | Defines the attribute functions of Slider. |
| [SliderBlockStyle](arkts-na-slider-sliderblockstyle-i.md) | Describes the style of the slider in the block direction. |
| [SliderConfiguration](arkts-na-slider-sliderconfiguration-i.md) | You need a custom class to implement the ContentModifier API. |
| [SliderCustomContentOptions](arkts-na-slider-slidercustomcontentoptions-i.md) | Defines the options for customizing the accessibility of content within a slider. These options can be used to enhance the user experience for assistive technologies. |
| [SliderOptions](arkts-na-slider-slideroptions-i.md) | Parameters of the slider. |
| [SliderPrefixOptions](arkts-na-slider-sliderprefixoptions-i.md) | Options used for customizing the prefix part of the slider. It extends the SliderCustomContentOptions to inherit accessibility customization options. |
| [SliderShowStepOptions](arkts-na-slider-slidershowstepoptions-i.md) | Defines the accessibility information of slider step point. |
| [SliderStepItemAccessibility](arkts-na-slider-sliderstepitemaccessibility-i.md) | Defines the accessibility information of slider step point. |
| [SliderSuffixOptions](arkts-na-slider-slidersuffixoptions-i.md) | Options used for customizing the suffix part of the slider. It extends the SliderCustomContentOptions to inherit accessibility customization options. |

### Enums

| Name | Description |
| --- | --- |
| [SliderBlockType](arkts-na-slider-sliderblocktype-e.md) | Enumerates the types of the slider in the block direction. |
| [SliderChangeMode](arkts-na-slider-sliderchangemode-e.md) | State triggered by the event. |
| [SliderInteraction](arkts-na-slider-sliderinteraction-e.md) | Interaction mode between the user and the slider. |
| [SliderStyle](arkts-na-slider-sliderstyle-e.md) | Style of the slider thumb and track. |

### Types

| Name | Description |
| --- | --- |
| [SliderTriggerChangeCallback](arkts-na-slidertriggerchangecallback-t.md) | Defines the callback type used in SliderConfiguration. |

