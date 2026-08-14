# ArcSliderStyleOptions

Defines the style of the arc slider.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-declare class ArcSliderStyleOptions--><!--Device-unnamed-declare class ArcSliderStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSlider } from 'ArcSlider';
import { ArcSliderPosition } from 'ArcSliderPosition';
import { ArcSliderOptions } from 'ArcSliderOptions';
import { ArcSliderOptionsConstructorOptions } from 'ArcSliderOptionsConstructorOptions';
import { ArcSliderLayoutOptions } from 'ArcSliderLayoutOptions';
import { ArcSliderLayoutOptionsConstructorOptions } from 'ArcSliderLayoutOptionsConstructorOptions';
import { ArcSliderStyleOptions } from 'ArcSliderStyleOptions';
import { ArcSliderStyleOptionsConstructorOptions } from 'ArcSliderStyleOptionsConstructorOptions';
import { ArcSliderValueOptions } from 'ArcSliderValueOptions';
import { ArcSliderValueOptionsConstructorOptions } from 'ArcSliderValueOptionsConstructorOptions';
```

## constructor

```TypeScript
constructor(options?: ArcSliderStyleOptionsConstructorOptions)
```

A constructor used to create an **ArcSliderStyleOptions** instance.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderStyleOptions-constructor(options?: ArcSliderStyleOptionsConstructorOptions)--><!--Device-ArcSliderStyleOptions-constructor(options?: ArcSliderStyleOptionsConstructorOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArcSliderStyleOptionsConstructorOptions](arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptionsconstructoroptions-i.md) | No | Constructor information for **ArcSliderStyleOptions**. |

## activeTrackThickness

```TypeScript
@Trace
  activeTrackThickness?: number
```

Stroke width of the arc slider when it is in an enlarged state, in vp. Default value: **24** Value range: [24, 36]. If the value is invalid, the default value is used.

**Type:** number

**Default:** 24

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderStyleOptions-@Trace  activeTrackThickness?: number--><!--Device-ArcSliderStyleOptions-@Trace  activeTrackThickness?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## selectedColor

```TypeScript
@Trace
  selectedColor?: string
```

Highlight color of the stroke. Default value: **#FF5EA1FF**

**Type:** string

**Default:** #FF5EA1FF

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderStyleOptions-@Trace  selectedColor?: string--><!--Device-ArcSliderStyleOptions-@Trace  selectedColor?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## trackBlur

```TypeScript
@Trace
  trackBlur?: number
```

Blur effect applied to the stroke background, in vp. Default value: **20** If a value less than 0 is set, the default is used.

**Type:** number

**Default:** 20

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderStyleOptions-@Trace  trackBlur?: number--><!--Device-ArcSliderStyleOptions-@Trace  trackBlur?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## trackColor

```TypeScript
@Trace
  trackColor?: string
```

Background color of the stroke. Default value: **#33FFFFFF**

**Type:** string

**Default:** #33FFFFFF

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderStyleOptions-@Trace  trackColor?: string--><!--Device-ArcSliderStyleOptions-@Trace  trackColor?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## trackThickness

```TypeScript
@Trace
  trackThickness?: number
```

Stroke width of the arc slider in the normal state, in vp. Default value: **5** Value range: [5, 16]. If the value is invalid, the default value is used.

**Type:** number

**Default:** 5

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderStyleOptions-@Trace  trackThickness?: number--><!--Device-ArcSliderStyleOptions-@Trace  trackThickness?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

