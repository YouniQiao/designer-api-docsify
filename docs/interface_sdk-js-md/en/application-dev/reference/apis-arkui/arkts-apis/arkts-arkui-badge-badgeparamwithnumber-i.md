# BadgeParamWithNumber

Inherits from BadgeParam and has all attributes of BadgeParam.

**Inheritance/Implementation:** BadgeParamWithNumber extends [BadgeParam](arkts-arkui-badge-badgeparam-i.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count: int
```

Number of notifications.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: The value must be an integer within [-2147483648,2147483647]. Value constraint: If the value is out of the range, 4294967296 is added or subtracted to ensure that the value is still in the range. If the value is not an integer, the decimal part is rounded off and the integer part is taken. For example, 5 is taken in 5.5.

**Type:** int

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxCount

```TypeScript
maxCount?: int
```

Maximum number of notifications. When the maximum number is reached, only maxCount+ is displayed. <p>&lt;strong&gt;NOTE&lt;/strong&gt;: Value range: [-2147483648, 2147483647]. Value constraint: If the value is out of the range, 4294967296 is added or subtracted to ensure that the value is still in the range. If the value is not an integer, the decimal part is rounded off and the integer part is taken. For example, 5 is taken in 5.5.. Default value: 99.

**Type:** int

**Default:** 99

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
