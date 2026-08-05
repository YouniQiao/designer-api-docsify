# BadgeParam

Provides basic parameters for creating a badge.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BadgeParam--><!--Device-unnamed-export declare interface BadgeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: BadgePosition | Position
```

Position to display the badge relative to the parent component. Default value: BadgePosition.RightTop. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: Percentage values are not supported for location types. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If an invalid value is set, the default value (0, 0) is used. Represents the upper left corner of the component, which will be used. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_When using the BadgePosition type, the location is mirrored based on the orientation attribute. \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_

**Type:** BadgePosition \| Position

**Default:** BadgePosition.RightTop

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParam-position?: BadgePosition | Position--><!--Device-BadgeParam-position?: BadgePosition | Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Style of the badge, including the font color, font size, badge color, and badge size.

**Type:** BadgeStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParam-style: BadgeStyle--><!--Device-BadgeParam-style: BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

