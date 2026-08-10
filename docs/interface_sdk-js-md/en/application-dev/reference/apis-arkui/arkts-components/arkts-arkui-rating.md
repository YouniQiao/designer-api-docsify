# Rating

提供在给定范围内选择评分的组件，通常用于商品评价、内容打分等应用场景。

> **说明：**

> - 当Rating的父节点有指定宽高时，需为Rating组件指定宽高，或为父节点设置值为true的[clip]{@link CommonMethod#clip(clip: Optional<boolean>)}属性。

## 子组件

无

## 键盘走焦规格

| 按键 | 功能描述 |  
|------------|-----------------------------|  
| Tab | 组件间切换焦点。 |  
| 左右方向键 | 评分预览增加/减少（步长为stepSize），不改变实际分值。 |  
| Home | 移动到第一个星星， 不改变实际分值。 |  
| End | 移动到最后一个星星， 不改变实际分值。 |  
| Space/Enter | 将当前预览的评分值设置为实际评分。 |

## Rating

```TypeScript
Rating(options?: RatingOptions)
```

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RatingInterface-(options?: RatingOptions): RatingAttribute--><!--Device-RatingInterface-(options?: RatingOptions): RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](../arkts-apis/arkts-arkui-rating-ratingoptions-i.md) | No | 设置评分组件。<br/> 未设置时，则按照RatingOptions中各参数的默认值配置。 |

## Summary

- [RatingConfiguration](arkts-arkui-rating-ratingconfiguration-i.md)
- [RatingOptions](arkts-arkui-rating-ratingoptions-i.md)
- [StarStyleOptions](arkts-arkui-rating-starstyleoptions-i.md)
- [OnRatingChangeCallback](arkts-arkui-rating-onratingchangecallback-t.md)
