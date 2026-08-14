# ArcSliderOptions

Defines the properties of the arc slider.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-declare class ArcSliderOptions--><!--Device-unnamed-declare class ArcSliderOptions-End-->

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
constructor(options?: ArcSliderOptionsConstructorOptions)
```

A constructor used to create an **ArcSliderOptions** instance.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-constructor(options?: ArcSliderOptionsConstructorOptions)--><!--Device-ArcSliderOptions-constructor(options?: ArcSliderOptionsConstructorOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArcSliderOptionsConstructorOptions](arkts-arkui-arkui-advanced-arcslider-arcslideroptionsconstructoroptions-i.md) | No | Constructor information for **ArcSliderOptions**. |

## digitalCrownSensitivity

```TypeScript
@Trace
  digitalCrownSensitivity?: CrownSensitivity
```

Sensitivity to the digital crown rotation. Default value: **CrownSensitivity.MEDIUM**

**Type:** CrownSensitivity

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  digitalCrownSensitivity?: CrownSensitivity--><!--Device-ArcSliderOptions-@Trace  digitalCrownSensitivity?: CrownSensitivity-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## layoutOptions

```TypeScript
@Trace
  layoutOptions?: ArcSliderLayoutOptions
```

Style of the arc slider. Default value: default values of all properties of [ArcSliderStyleOptions](arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md#ArcSliderStyleOptions)

**Type:** [ArcSliderLayoutOptions](arkts-arkui-arkui-advanced-arcslider-arcsliderlayoutoptions-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  layoutOptions?: ArcSliderLayoutOptions--><!--Device-ArcSliderOptions-@Trace  layoutOptions?: ArcSliderLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onChange

```TypeScript
@Trace
  onChange?: ArcSliderChangeHandler
```

Callback invoked to notify the application when the progress value of the arc slider changes. Default value: If this parameter is not provided, no callback will be invoked.

**Type:** [ArcSliderChangeHandler](arkts-arkui-arcsliderchangehandler-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  onChange?: ArcSliderChangeHandler--><!--Device-ArcSliderOptions-@Trace  onChange?: ArcSliderChangeHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onEnlarge

```TypeScript
@Trace
  onEnlarge?: ArcSliderEnlargeHandler
```

Callback invoked to notify the application when the arc slider is enlarged or reduced. Default value: If this parameter is not provided, no callback will be invoked.

**Type:** [ArcSliderEnlargeHandler](../../apis-na/arkts-apis/arkts-na-arcsliderenlargehandler-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  onEnlarge?: ArcSliderEnlargeHandler--><!--Device-ArcSliderOptions-@Trace  onEnlarge?: ArcSliderEnlargeHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## onTouch

```TypeScript
@Trace
  onTouch?: ArcSliderTouchHandler
```

Callback invoked to notify the application when the arc slider is touched. Default value: If this parameter is not provided, no callback will be invoked.

**Type:** [ArcSliderTouchHandler](arkts-arkui-arcslidertouchhandler-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  onTouch?: ArcSliderTouchHandler--><!--Device-ArcSliderOptions-@Trace  onTouch?: ArcSliderTouchHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## styleOptions

```TypeScript
@Trace
  styleOptions?: ArcSliderStyleOptions
```

Style of the arc slider. Default value: default values of all properties of [ArcSliderStyleOptions](arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md#ArcSliderStyleOptions)

**Type:** [ArcSliderStyleOptions](arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  styleOptions?: ArcSliderStyleOptions--><!--Device-ArcSliderOptions-@Trace  styleOptions?: ArcSliderStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## valueOptions

```TypeScript
@Trace
  valueOptions?: ArcSliderValueOptions
```

Style of the arc slider. Default value: default values of all properties of [ArcSliderStyleOptions](arkts-arkui-arkui-advanced-arcslider-arcsliderstyleoptions-c.md#ArcSliderStyleOptions)

**Type:** [ArcSliderValueOptions](arkts-arkui-arkui-advanced-arcslider-arcslidervalueoptions-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcSliderOptions-@Trace  valueOptions?: ArcSliderValueOptions--><!--Device-ArcSliderOptions-@Trace  valueOptions?: ArcSliderValueOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

