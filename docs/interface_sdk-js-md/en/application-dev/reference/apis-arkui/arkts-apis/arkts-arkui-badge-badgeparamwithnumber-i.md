# BadgeParamWithNumber

BadgeParamWithNumber继承自[BadgeParam](../arkts-components/arkts-arkui-badgeparam-i.md/arkts-arkui-badgeparam-i.md)，具有BadgeParam的全部属性。

**Inheritance/Implementation:** BadgeParamWithNumber extends [BadgeParam](../arkts-components/arkts-arkui-badgeparam-i.md/arkts-arkui-badgeparam-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BadgeParamWithNumber extends BadgeParam--><!--Device-unnamed-export declare interface BadgeParamWithNumber extends BadgeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count: int
```

设置提醒消息数。  
**说明：**当该值小于等于0且小于maxCount时不显示信息标记。取值应为[-2147483648,2147483647]内的整数。取值约束：超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParamWithNumber-count: int--><!--Device-BadgeParamWithNumber-count: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxCount

```TypeScript
maxCount?: int
```

最大消息数，超过最大消息时仅显示maxCount+，如maxCount是99时，显示`99+`。取值范围：[-2147483648, 2147483647]。取值约束：超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。。默认值：99。

**Type:** int

**Default:** 99

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeParamWithNumber-maxCount?: int--><!--Device-BadgeParamWithNumber-maxCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

