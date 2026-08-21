# ArcSliderValueOptions

The options for ArcSlider progress value.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ArcSliderValueOptions--><!--Device-unnamed-export declare class ArcSliderValueOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options?: ArcSliderValueOptionsConstructorOptions)
```

The constructor used to create a ArcSliderValueOptions object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ArcSliderValueOptions-constructor(options?: ArcSliderValueOptionsConstructorOptions)--><!--Device-ArcSliderValueOptions-constructor(options?: ArcSliderValueOptionsConstructorOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ArcSliderValueOptionsConstructorOptions](arkts-arkui-advanced-arcslider-arcslidervalueoptionsconstructoroptions-i.md) | No |  |

## max

```TypeScript
@Trace
  max?: double
```

Set the maximum progress value.

**Type:** double

**Default:** 100

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ArcSliderValueOptions-@Trace  max?: double--><!--Device-ArcSliderValueOptions-@Trace  max?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## min

```TypeScript
@Trace
  min?: double
```

Set the minimum progress value.

**Type:** double

**Default:** 0

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ArcSliderValueOptions-@Trace  min?: double--><!--Device-ArcSliderValueOptions-@Trace  min?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## progress

```TypeScript
@Trace
  progress?: double
```

Set current progress value. The default value is consistent with the value of the parameter min.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ArcSliderValueOptions-@Trace  progress?: double--><!--Device-ArcSliderValueOptions-@Trace  progress?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

