# BadgeParam

Provides basic parameters for creating a badge.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface BadgeParam--><!--Device-unnamed-export declare interface BadgeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: BadgePosition | Position
```

Position to display the badge relative to the parent component. Default value: BadgePosition.RightTop. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: Percentage values are not supported for location types. &lt;br&gt;If an invalid value is set, the default value (0, 0) is used. Represents the upper left corner of the component, which will be used. &lt;br&gt;When using the BadgePosition type, the location is mirrored based on the orientation attribute. &lt;/p&gt;

**Type:** [BadgePosition](arkts-na-badge-badgeposition-e.md) \| [Position](../../apis-arkui/arkts-apis/arkts-arkui-position-i.md)

**Default:** BadgePosition.RightTop

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParam-position?: BadgePosition | Position--><!--Device-BadgeParam-position?: BadgePosition | Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Style of the badge, including the font color, font size, badge color, and badge size.

**Type:** [BadgeStyle](arkts-na-badge-badgestyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParam-style: BadgeStyle--><!--Device-BadgeParam-style: BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

