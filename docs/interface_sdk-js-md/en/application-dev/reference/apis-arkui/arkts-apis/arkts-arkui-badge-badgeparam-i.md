# BadgeParam

Provides basic parameters for creating a badge.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: BadgePosition | Position
```

Position to display the badge relative to the parent component. Default value: BadgePosition.RightTop.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: Percentage values are not supported for location types. <br>If an invalid value is set, the default value (0, 0) is used. Represents the upper left corner of the component, which will be used. <br>When using the BadgePosition type, the location is mirrored based on the orientation attribute. </p>

**Type:** [BadgePosition](arkts-arkui-badge-badgeposition-e.md) \| [Position](arkts-arkui-position-i.md)

**Default:** BadgePosition.RightTop

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Style of the badge, including the font color, font size, badge color, and badge size.

**Type:** [BadgeStyle](arkts-arkui-badge-badgestyle-i.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
