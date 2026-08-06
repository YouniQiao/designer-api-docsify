# component/slider

## Summary

### Functions

| Name | Description |
| --- | --- |
| [Slider](slider-slider-f.md#slider) | Defines Slider Component. |

### Classes

| Name | Description |
| --- | --- |
| [ColorMetricsLinearGradient](slider-colormetricslineargradient-c.md) | ColorMetricsLinearGradient class |

### Interfaces

| Name | Description |
| --- | --- |
| [ColorMetricsStop](slider-colormetricsstop-i.md) | ColorMetricsStop type |
| [SlideRange](slider-sliderange-i.md) | Defines the callback type used in SlideRange. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_NOTE\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_: \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_3\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Currently, this API takes effect only when MIN ≤ from ≤ to ≤ MAX (the values of MIN and MAX do not depend on the values set, but on the actual values that take effect). You can set either from or to, or you can set both from and to. When the API is effective, if the set from value is between the adjacent multiples of step, then from takes the value of the left interval multiple of step or MIN as the corrected value. When the API is effective, if the set to value is between the adjacent multiples of step, then to takes the value of the right interval multiple of step or MAX as the corrected value. After from and to have taken their corrected values, when value is undefined or null, it takes the same value as from; when value is a number type, and if value ≤ from, then it takes from; if value > to, then it takes to. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_4\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ |
| [SliderAttribute](slider-sliderattribute-i.md) | Defines the attribute functions of Slider. |
| [SliderBlockStyle](slider-sliderblockstyle-i.md) | Describes the style of the slider in the block direction. |
| [SliderConfiguration](slider-sliderconfiguration-i.md) | You need a custom class to implement the ContentModifier API. |
| [SliderCustomContentOptions](slider-slidercustomcontentoptions-i.md) | Defines the options for customizing the accessibility of content within a slider. These options can be used to enhance the user experience for assistive technologies. |
| [SliderOptions](slider-slideroptions-i.md) | Parameters of the slider. |
| [SliderPrefixOptions](slider-sliderprefixoptions-i.md) | Options used for customizing the prefix part of the slider. It extends the SliderCustomContentOptions to inherit accessibility customization options. |
| [SliderShowStepOptions](slider-slidershowstepoptions-i.md) | Defines the accessibility information of slider step point. |
| [SliderStepItemAccessibility](slider-sliderstepitemaccessibility-i.md) | Defines the accessibility information of slider step point. |
| [SliderSuffixOptions](slider-slidersuffixoptions-i.md) | Options used for customizing the suffix part of the slider. It extends the SliderCustomContentOptions to inherit accessibility customization options. |

### Enums

| Name | Description |
| --- | --- |
| [SliderBlockType](slider-sliderblocktype-e.md) | Enumerates the types of the slider in the block direction. |
| [SliderChangeMode](slider-sliderchangemode-e.md) | State triggered by the event. |
| [SliderInteraction](slider-sliderinteraction-e.md) | Interaction mode between the user and the slider. |
| [SliderStyle](slider-sliderstyle-e.md) | Style of the slider thumb and track. |

### Types

| Name | Description |
| --- | --- |
| [SliderTriggerChangeCallback](arkts-na-slidertriggerchangecallback-t.md) | Defines the callback type used in SliderConfiguration. |

