# CachedCountOptions

定义用于控制缓存计数行为的属性

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface CachedCountOptions--><!--Device-unnamed-export declare interface CachedCountOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## independent

```TypeScript
independent?: boolean
```

[cachedCount](SwiperAttribute.default cachedCount(count: int | undefined, options: CachedCountOptions |undefined))是否按组计算。true表示cachedCount按实际子组件个数计算，不按组计算；false表示如果displayCount.swipeByGroup=true，则cachedCount按组计算，否则按实际子组件个数计算。默认值： false。undefined当设置为true时，cachedCount将根据实际的子组件计数来计算。独立于displayCount分组计算。&lt;br&gt;如果启用了SwiftByGroup并且该值为false，则cachedCount将按组计算。&lt;/p&gt;。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CachedCountOptions-independent?: boolean--><!--Device-CachedCountOptions-independent?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShown

```TypeScript
isShown?: boolean
```

预加载范围内的节点是否进行绘制。

true表示预加载范围内的节点进行绘制；false表示预加载范围内的节点不进行绘制。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CachedCountOptions-isShown?: boolean--><!--Device-CachedCountOptions-isShown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

