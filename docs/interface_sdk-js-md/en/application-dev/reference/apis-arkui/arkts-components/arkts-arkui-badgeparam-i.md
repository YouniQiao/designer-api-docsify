# BadgeParam

Provides basic parameters for creating a badge.

**Since:** 7

<!--Device-unnamed-declare interface BadgeParam--><!--Device-unnamed-declare interface BadgeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## position

```TypeScript
position?: BadgePosition | Position
```

Position to display the badge relative to the parent component. Default value: **BadgePosition.RightTop** **NOTE：**With the **Position** type, percentage values are not supported. If an invalid value is set, the default value **(0,0)**, which indicates the upper left corner of the component, will be used. With the **BadgePosition** type, the position is mirrored based on the Direction property.

**Type:** [BadgePosition](arkts-arkui-badgeposition-e.md) \| Position

**Default:** BadgePosition.RightTop

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BadgeParam-position?: BadgePosition | Position--><!--Device-BadgeParam-position?: BadgePosition | Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Style of the badge, including the font color, font size, badge color, and badge size.

**Type:** [BadgeStyle](arkts-arkui-badgestyle-i.md)

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BadgeParam-style: BadgeStyle--><!--Device-BadgeParam-style: BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

