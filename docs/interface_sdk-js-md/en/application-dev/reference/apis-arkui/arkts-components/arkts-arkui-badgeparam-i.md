# BadgeParam

包含用于创建Badge组件的基础参数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface BadgeParam--><!--Device-unnamed-declare interface BadgeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: BadgePosition | Position
```

设置标记显示位置。

默认值：BadgePosition.RightTop 

**说明：**

Position作为入参，不支持设置百分比；设置为非法值时，按(0,0)处理，(0,0)为组件左上角位置。

BadgePosition作为入参时，会跟随[Direction](../arkts-apis/arkts-arkui-enums-direction-e.md/arkts-arkui-enums-direction-e.md)属性控制镜像显示。

**Type:** [BadgePosition](../arkts-apis/arkts-arkui-badge-badgeposition-e.md) \| Position

**Default:** BadgePosition.RightTop

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BadgeParam-position?: BadgePosition | Position--><!--Device-BadgeParam-position?: BadgePosition | Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style: BadgeStyle
```

Badge组件可设置样式，支持设置文本颜色、大小、标记颜色和标记大小。

**Type:** [BadgeStyle](arkts-arkui-badgestyle-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BadgeParam-style: BadgeStyle--><!--Device-BadgeParam-style: BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

