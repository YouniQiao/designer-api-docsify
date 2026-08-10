# CachedCountOptions

预加载子组件的配置选项。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

<!--Device-unnamed-declare interface CachedCountOptions--><!--Device-unnamed-declare interface CachedCountOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## independent

```TypeScript
independent?: boolean
```

[cachedCount](SwiperAttribute#cachedCount(count: number, options: CachedCountOptions))是否按实际子组件个数计算。

设置为true时，cachedCount按实际子组件个数计算，不按组计算。

设置为false时，如果displayCount.swipeByGroup=true，则cachedCount按组计算，否则按实际子组件个数计算。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CachedCountOptions-independent?: boolean--><!--Device-CachedCountOptions-independent?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShown

```TypeScript
isShown?: boolean
```

预加载范围内的节点是否进行绘制。

设置为true时，预加载范围内的节点进行绘制。

设置为false时，预加载范围内的节点不进行绘制。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-CachedCountOptions-isShown?: boolean--><!--Device-CachedCountOptions-isShown?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

