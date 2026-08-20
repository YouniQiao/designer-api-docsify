# LengthUnit

Defines the Length Unit.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum LengthUnit--><!--Device-unnamed-export declare enum LengthUnit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PX

```TypeScript
PX = 0
```

Logical pixel used in Ace1.0. It's based on frontend design width. For example, when a frontend with 750px design width running on a device with 1080 pixels width, 1px represents 1.44 pixels.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthUnit-PX = 0--><!--Device-LengthUnit-PX = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## VP

```TypeScript
VP = 1
```

Density independent pixels, one vp is one pixel on a 160 dpi screen.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthUnit-VP = 1--><!--Device-LengthUnit-VP = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FP

```TypeScript
FP = 2
```

Scale independent pixels. This is like VP but will be scaled by user's font size preference.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthUnit-FP = 2--><!--Device-LengthUnit-FP = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PERCENT

```TypeScript
PERCENT = 3
```

The percentage of either a value from the element's parent or from another property of the element itself.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthUnit-PERCENT = 3--><!--Device-LengthUnit-PERCENT = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LPX

```TypeScript
LPX = 4
```

Logic pixels used in ACE2.0 instead of PX, and PX is the physical pixels in ACE2.0.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LengthUnit-LPX = 4--><!--Device-LengthUnit-LPX = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

