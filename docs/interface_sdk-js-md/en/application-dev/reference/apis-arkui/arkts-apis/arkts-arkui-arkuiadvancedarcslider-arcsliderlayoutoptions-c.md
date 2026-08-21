# ArcSliderLayoutOptions

Defines the layout of the arc slider.

**Since:** 18

<!--Device-unnamed-declare class ArcSliderLayoutOptions--><!--Device-unnamed-declare class ArcSliderLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSlider, ArcSliderPosition, ArcSliderOptions, ArcSliderOptionsConstructorOptions, ArcSliderLayoutOptions, ArcSliderLayoutOptionsConstructorOptions, ArcSliderStyleOptions, ArcSliderStyleOptionsConstructorOptions, ArcSliderValueOptions, ArcSliderValueOptionsConstructorOptions } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ArcSliderLayoutOptionsConstructorOptions)
```

A constructor used to create an **ArcSliderLayoutOptions** instance.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderLayoutOptions-constructor(options?: ArcSliderLayoutOptionsConstructorOptions)--><!--Device-ArcSliderLayoutOptions-constructor(options?: ArcSliderLayoutOptionsConstructorOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArcSliderLayoutOptionsConstructorOptions](../../apis-default/arkts-apis/arkts-arkuiadvancedarcslider-arcsliderlayoutoptionsconstructoroptions-i.md) | No | Construction information for **ArcSliderLayoutOptions**. |

## position

```TypeScript
@Trace
  position?: ArcSliderPosition
```

Position of the arc slider on the screen.

Default value: **ArcSliderPosition.RIGHT**

@Trace

**Type:** [ArcSliderPosition](../../apis-default/arkts-apis/arkts-arkuiadvancedarcslider-arcsliderposition-e.md)

**Default:** ArcSliderPosition.RIGHT

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderLayoutOptions-@Trace  position?: ArcSliderPosition--><!--Device-ArcSliderLayoutOptions-@Trace  position?: ArcSliderPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## reverse

```TypeScript
@Trace
  reverse?: boolean
```

Whether the value range of the arc slider is reversed. **false**: top-to-bottom sliding.

**true** (default): bottom-to-top sliding.

@Trace

**Type:** boolean

**Default:** true

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderLayoutOptions-@Trace  reverse?: boolean--><!--Device-ArcSliderLayoutOptions-@Trace  reverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

