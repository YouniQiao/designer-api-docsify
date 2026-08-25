# Slider properties/events

All the universal attributes except **responseRegion** are supported.In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** SliderAttribute extends CommonMethod<SliderAttribute>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## blockBorderColor

```TypeScript
blockBorderColor(value: ResourceColor)
```

Sets the border color of the slider in the block direction.When **SliderBlockType.DEFAULT** is used, **blockBorderColor** sets the border color of the round slider.When **SliderBlockType.IMAGE** is used, **blockBorderColor** does not work as the slider has no border.When **SliderBlockType.SHAPE** is used, **blockBorderColor** sets the border color of the slider in a custom shape.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## blockBorderWidth

```TypeScript
blockBorderWidth(value: Length)
```

Sets the border width of the slider in the block direction.When **SliderBlockType.DEFAULT** is used, **blockBorderWidth** sets the border width of the round slider.When **SliderBlockType.IMAGE** is used, **blockBorderWidth** does not work as the slider has no border.When **SliderBlockType.SHAPE** is used, **blockBorderWidth** sets the border width of the slider in a custom shape.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## blockColor

```TypeScript
blockColor(value: ResourceColor)
```

Sets the color of the thumb.When **SliderBlockType.DEFAULT** is used, **blockColor** sets the color of the round thumb.When **SliderBlockType.IMAGE** is used, **blockColor** does not work as the thumb has no fill color.When **SliderBlockType.SHAPE** is used, **blockColor** sets the color of the thumb in a custom shape.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## blockColor

```TypeScript
blockColor(value: ResourceColor | LinearGradient)
```

Sets the color of the slider. Gradient colors are supported.When **SliderBlockType.DEFAULT** is used, **blockColor** sets the color of the round thumb.When **SliderBlockType.IMAGE** is used, **blockColor** does not work as the thumb has no fill color.When **SliderBlockType.SHAPE** is used, **blockColor** sets the color of the thumb in a custom shape.

**Since:** 21

**ArkTS mode:** Supports only ArkTS-Dyn, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ResourceColor \| [LinearGradient](arkts-arkui-lineargradient-c.md) | Yes |

## blockSize

```TypeScript
blockSize(value: SizeOptions)
```

Sets the size of the slider in the block direction.When the slider type is set to **SliderBlockType.DEFAULT**, the smaller of the width and height values is used as the radius of the circle.When the slider type is set to **SliderBlockType.IMAGE**, this API sets the size of the image, which is scaled using the **ObjectFit.Cover** strategy.When the slider type is set to **SliderBlockType.SHAPE**, this API sets the size of the custom shape, which is also scaled using the **ObjectFit.Cover** strategy.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SizeOptions](../arkts-apis/arkts-arkui-units-sizeoptions-i.md) | Yes |

## blockStyle

```TypeScript
blockStyle(value: SliderBlockStyle)
```

Sets the style of the slider in the block direction.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SliderBlockStyle](arkts-arkui-sliderblockstyle-i.md) | Yes |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<SliderConfiguration>)
```

Creates a content modifier.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | ContentModifier&lt;[SliderConfiguration](arkts-arkui-sliderconfiguration-i.md)&gt; | Yes |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)
```

Sets the sensitivity to the digital crown rotation.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sensitivity | Optional & lt;CrownSensitivity & gt; | Yes |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean)
```

Specifies whether to enable haptic feedback.To enable haptic feedback, you must declare the **ohos.permission.VIBRATE** permission under **requestPermissions** in the [module.json5](../../../quick-start/module-configuration-file.md) file of the project.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## maxLabel

```TypeScript
maxLabel(value: string)
```

Sets the maximum value.

> **NOTE：**&gt;
> This attribute is supported since API version 7 and deprecated since API version 9. You are advised to use
> **max** instead. **max** is an attribute of [SliderOptions](arkts-arkui-slideroptions-i.md).

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** max

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## minLabel

```TypeScript
minLabel(value: string)
```

Sets the minimum value.

> **NOTE：**&gt;
> This attribute is supported since API version 7 and deprecated since API version 9. You are advised to use
> **min** instead. **min** is an attribute of [SliderOptions](arkts-arkui-slideroptions-i.md).

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** min

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## minResponsiveDistance

```TypeScript
minResponsiveDistance(value: number)
```

Sets the minimum distance required for the slider to respond.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## onChange

```TypeScript
onChange(callback: (value: number, mode: SliderChangeMode) => void)
```

Triggered when the slider is dragged or clicked.The **Begin** and **End** states are triggered when the slider is clicked with a gesture. The **Moving** and **Click** states are triggered when the value of **value** changes.If the coherent action is a drag action, the **Click** state will not be triggered.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (value: number, mode: SliderChangeMode) = & gt; void | Yes |

## prefix

```TypeScript
prefix(content: ComponentContent, options?: SliderPrefixOptions)
```

Sets the prefix of the slider.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | Yes |
| options | [SliderPrefixOptions](arkts-arkui-sliderprefixoptions-i.md) | No |

## selectedBorderRadius

```TypeScript
selectedBorderRadius(value: Dimension)
```

Set the corner radius of the selected (highlighted) part of the slider.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes |

## selectedColor

```TypeScript
selectedColor(value: ResourceColor)
```

Sets the color of the portion of the track between the minimum value and the thumb, representing the selected portion.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## selectedColor

```TypeScript
selectedColor(selectedColor: ResourceColor | LinearGradient)
```

Sets the color of the portion of the track between the minimum value and the thumb, representing the selected portion. Compared to [selectedColor](#selectedcolor), this API supports the **LinearGradient** type.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [selectedColor](#selectedcolor) | ResourceColor \| [LinearGradient](arkts-arkui-lineargradient-c.md) | Yes |

## showSteps

```TypeScript
showSteps(value: boolean)
```

Sets whether to display the step markers along the slider track.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## showSteps

```TypeScript
showSteps(value: boolean, options?: SliderShowStepOptions)
```

Sets whether to display the step markers along the slider track.You can set custom accessibility text for each step value. If no accessibility text is provided, the numeric values are used.The accessibility text settings take effect only when the step markers are displayed.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
| options | [SliderShowStepOptions](arkts-arkui-slidershowstepoptions-i.md) | No |

## showTips

```TypeScript
showTips(value: boolean, content?: ResourceStr)
```

Sets whether to display a tooltip when the user drags the slider.When **direction** is set to **Axis.Horizontal**, the tooltip is displayed right above the slider; if there is insufficient space above, it will be displayed below. When **direction** is set to **Axis.Vertical**, the tooltip is displayed on the left of the slider; if there is insufficient space on the left, it will be displayed on the right. If the margins are not set or are set to small values, the tooltip may be clipped.The drawing area of the tooltip is the overlay of the slider.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
| content | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | No |

## slideRange

```TypeScript
slideRange(value: SlideRange)
```

Sets the slide range.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SlideRange](arkts-arkui-sliderange-i.md) | Yes |

## sliderInteractionMode

```TypeScript
sliderInteractionMode(value: SliderInteraction)
```

Sets the interaction mode between the user and the slider.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SliderInteraction](arkts-arkui-sliderinteraction-e.md) | Yes |

## stepColor

```TypeScript
stepColor(value: ResourceColor)
```

Sets the step color.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## stepSize

```TypeScript
stepSize(value: Length)
```

Sets the step size (diameter). If the value is 0, the step size is not displayed. If the value is less than 0, the default value is used.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## suffix

```TypeScript
suffix(content: ComponentContent, options?: SliderSuffixOptions)
```

Sets the suffix of the slider.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | Yes |
| options | [SliderSuffixOptions](arkts-arkui-slidersuffixoptions-i.md) | No |

## trackBorderRadius

```TypeScript
trackBorderRadius(value: Length)
```

Sets the radius of the rounded corner of the track.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## trackColor

```TypeScript
trackColor(value: ResourceColor | LinearGradient)
```

Sets the background color of the track.Since API version 12, **LinearGradient** can be used to create a gradient effect for the track.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ResourceColor \| [LinearGradient](arkts-arkui-lineargradient-c.md) | Yes |

## trackColorMetrics

```TypeScript
trackColorMetrics(color: ColorMetricsLinearGradient)
```

Sets the linear gradient background color of the track.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ColorMetricsLinearGradient](arkts-arkui-colormetricslineargradient-c.md) | Yes |

## trackThickness

```TypeScript
trackThickness(value: Length)
```

Sets the thickness of the track. If the value is less than or equal to 0, the default value is used.To ensure [SliderStyle](arkts-arkui-sliderstyle-e.md) works as expected for the thumb and track, [blockSize](#blocksize) should increase or decrease proportionally with **trackThickness**.Specially, when **style** is **[SliderStyle](arkts-arkui-sliderstyle-e.md).OutSet**, trackThickness: [blockSize](#blocksize) = 1:4; when **style** is **[SliderStyle](arkts-arkui-sliderstyle-e.md).InSet**, trackThickness: [blockSize](#blocksize) = 5:3.If the value of **trackThickness** or [blockSize](#blocksize) exceeds the width or height of the **Slider** component, the default value is used.When [SliderStyle](arkts-arkui-sliderstyle-e.md) is set to **OutSet**, if the specified value of [blockSize](#blocksize) exceeds the width or height of the **Slider** component, the default value is used, regardless of whether the value of **trackThickness** is valid or not.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |
