# SliderAttribute

Defines the attribute functions of Slider.

**Inheritance/Implementation:** SliderAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SliderAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SliderAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SliderAttribute-default attributeModifier(modifier: AttributeModifier<SliderAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;SliderAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blockBorderColor

```TypeScript
default blockBorderColor(value: ResourceColor | undefined): this
```

Called when the border color of block is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default blockBorderColor(value: ResourceColor | undefined): this--><!--Device-SliderAttribute-default blockBorderColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the border color of block. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blockBorderWidth

```TypeScript
default blockBorderWidth(value: Length | undefined): this
```

Called when the border width of block is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default blockBorderWidth(value: Length | undefined): this--><!--Device-SliderAttribute-default blockBorderWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | the border width of block. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blockColor

```TypeScript
default blockColor(value: ResourceColor | LinearGradient | undefined): this
```

Set the color of the slider bar, supporting gradient colors.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default blockColor(value: ResourceColor | LinearGradient | undefined): this--><!--Device-SliderAttribute-default blockColor(value: ResourceColor | LinearGradient | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient \| undefined | Yes | the color of the slider bar. Undefined indicates using the default color. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blockSize

```TypeScript
default blockSize(value: SizeOptions | undefined): this
```

Called when the size of block is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default blockSize(value: SizeOptions | undefined): this--><!--Device-SliderAttribute-default blockSize(value: SizeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | Yes | the size of block. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blockStyle

```TypeScript
default blockStyle(value: SliderBlockStyle | undefined): this
```

Sets the style of the slider in the block direction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default blockStyle(value: SliderBlockStyle | undefined): this--><!--Device-SliderAttribute-default blockStyle(value: SliderBlockStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SliderBlockStyle](../arkts-components/arkts-arkui-sliderblockstyle-i.md) \| undefined | Yes | Style of the slider in the block direction. &lt;br&gt;Default value is SliderBlockType.DEFAULT, indicating the round slider. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this
```

Creates a content modifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this--><!--Device-SliderAttribute-default contentModifier(modifier: ContentModifier<SliderConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;SliderConfiguration&gt; \| undefined | Yes | Content modifier to apply to the slider. modifier: content modifier. You need a custom class to implement the ContentModifier API. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

Set the sensitivity of rotating crown.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-SliderAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | Yes | The sensitivity of rotating crown, default value is { MEDIUM }. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enabled: boolean | undefined): this
```

Enable or disable haptic feedback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default enableHapticFeedback(enabled: boolean | undefined): this--><!--Device-SliderAttribute-default enableHapticFeedback(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Default value is true, set false to disable haptic feedback. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## minResponsiveDistance

```TypeScript
default minResponsiveDistance(value: double | undefined): this
```

Sets the min value when Slider response to drag event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default minResponsiveDistance(value: double | undefined): this--><!--Device-SliderAttribute-default minResponsiveDistance(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this
```

Triggered when the slider is dragged or clicked.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The Begin and End states are triggered when the slider is clicked with a gesture. The Moving and Click states are triggered when the value of value changes. If the coherent action is a drag action, the Click state will not be triggered.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this--><!--Device-SliderAttribute-default onChange(callback: ((value: double, mode: SliderChangeMode) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((value: double, mode: SliderChangeMode) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## prefix

```TypeScript
default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this
```

Set the prefix part of the slider.The prefix is the content that appears before the main slider component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this--><!--Device-SliderAttribute-default prefix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderPrefixOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| undefined | Yes | Custom components that will be displayed as the prefix. This can be any valid custom UI component structure. Undefined indicates that no prefix is set. |
| options | [SliderPrefixOptions](../arkts-components/arkts-arkui-sliderprefixoptions-i.md) \| undefined | No | Optional options for customizing the prefix. These options can include accessibility settings. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedBorderRadius

```TypeScript
default selectedBorderRadius(value: Dimension | undefined): this
```

Called when the radius of selected part is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default selectedBorderRadius(value: Dimension | undefined): this--><!--Device-SliderAttribute-default selectedBorderRadius(value: Dimension | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| undefined | Yes | the radius of selected part. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this
```

Called when the slider of the slider bar is set to slide over the area color.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this--><!--Device-SliderAttribute-default selectedColor(selectedColor: ResourceColor | LinearGradient | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setSliderOptions

```TypeScript
default setSliderOptions(options?: SliderOptions): this
```

Set slider options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default setSliderOptions(options?: SliderOptions): this--><!--Device-SliderAttribute-default setSliderOptions(options?: SliderOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SliderOptions](../arkts-components/arkts-arkui-slideroptions-i.md) | No | slider constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the SliderAttribute. |

## showSteps

```TypeScript
default showSteps(value: boolean | undefined): this
```

Set whether to display step size.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default showSteps(value: boolean | undefined): this--><!--Device-SliderAttribute-default showSteps(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Default value is false, undefined means set to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## showSteps

```TypeScript
default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this
```

Set whether to display step size, and support setting accessibility text configuration parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this--><!--Device-SliderAttribute-default showSteps(value: boolean | undefined, options?: SliderShowStepOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Default value is false, undefined means set to default value. |
| options | [SliderShowStepOptions](../arkts-components/arkts-arkui-slidershowstepoptions-i.md) \| undefined | No | Set the accessibility text on slider points. undefined means set to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## showTips

```TypeScript
default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this
```

Called when the percentage of bubble prompt is set when sliding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this--><!--Device-SliderAttribute-default showTips(value: boolean | undefined, content?: ResourceStr | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether to display the bubble. |
| content | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | No | Text content in the bubble. If the content is not specified, the current percentage is displayed by default. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## slideRange

```TypeScript
default slideRange(value: SlideRange | undefined): this
```

Set the valid slidable range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default slideRange(value: SlideRange | undefined): this--><!--Device-SliderAttribute-default slideRange(value: SlideRange | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SlideRange](arkts-arkui-slider-sliderange-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sliderInteractionMode

```TypeScript
default sliderInteractionMode(value: SliderInteraction | undefined): this
```

Sets the interaction mode between the user and the slider.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default sliderInteractionMode(value: SliderInteraction | undefined): this--><!--Device-SliderAttribute-default sliderInteractionMode(value: SliderInteraction | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SliderInteraction](arkts-arkui-slider-sliderinteraction-e.md) \| undefined | Yes | Interaction mode between the user and the slider. &lt;br&gt;Default value is SliderInteraction.SLIDE_AND_CLICK. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stepColor

```TypeScript
default stepColor(value: ResourceColor | undefined): this
```

Called when the color of step is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default stepColor(value: ResourceColor | undefined): this--><!--Device-SliderAttribute-default stepColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | the color of step. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stepSize

```TypeScript
default stepSize(value: Length | undefined): this
```

Called when the diameter of step is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default stepSize(value: Length | undefined): this--><!--Device-SliderAttribute-default stepSize(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | the diameter of step. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## suffix

```TypeScript
default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this
```

Set the suffix part of the slider.The suffix is the content that appears after the main slider component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this--><!--Device-SliderAttribute-default suffix<T extends Object>(content: ComponentContent<T> | undefined, options?: SliderSuffixOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;T&gt; \| undefined | Yes | Custom components that will be displayed as the suffix. This can be any valid custom UI component structure. Undefined indicates that no suffix is set. |
| options | [SliderSuffixOptions](arkts-arkui-slider-slidersuffixoptions-i.md) \| undefined | No | Optional options for customizing the suffix. These options can include accessibility settings. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## trackBorderRadius

```TypeScript
default trackBorderRadius(value: Length | undefined): this
```

Called when the radius of track border is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default trackBorderRadius(value: Length | undefined): this--><!--Device-SliderAttribute-default trackBorderRadius(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | the radius of track border. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## trackColor

```TypeScript
default trackColor(value: ResourceColor | LinearGradient | undefined): this
```

Called when the track color of the slider is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default trackColor(value: ResourceColor | LinearGradient | undefined): this--><!--Device-SliderAttribute-default trackColor(value: ResourceColor | LinearGradient | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## trackColorMetrics

```TypeScript
default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this
```

Set the track color of the slider using the color metrics.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this--><!--Device-SliderAttribute-default trackColorMetrics(color: ColorMetricsLinearGradient | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ColorMetricsLinearGradient](arkts-arkui-slider-colormetricslineargradient-c.md) \| undefined | Yes | Track color of the slider using the color metrics. Undefined indicates using the default color. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## trackThickness

```TypeScript
default trackThickness(value: Length | undefined): this
```

Called when the thickness of track is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderAttribute-default trackThickness(value: Length | undefined): this--><!--Device-SliderAttribute-default trackThickness(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

