# SwiperContentTransitionProxy

Swiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知Swiper组件页面自定义动画已结束。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface SwiperContentTransitionProxy--><!--Device-unnamed-declare interface SwiperContentTransitionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finishTransition

```TypeScript
finishTransition(): void
```

通知Swiper组件，此页面的自定义动画已结束。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-SwiperContentTransitionProxy-finishTransition(): void--><!--Device-SwiperContentTransitionProxy-finishTransition(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: number
```

视窗内页面的索引。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-SwiperContentTransitionProxy-index: number--><!--Device-SwiperContentTransitionProxy-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mainAxisLength

```TypeScript
mainAxisLength: number
```

index对应页面在主轴方向上的长度，单位vp。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-SwiperContentTransitionProxy-mainAxisLength: number--><!--Device-SwiperContentTransitionProxy-mainAxisLength: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position: number
```

index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-SwiperContentTransitionProxy-position: number--><!--Device-SwiperContentTransitionProxy-position: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
selectedIndex: number
```

当前选中页面的索引。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-SwiperContentTransitionProxy-selectedIndex: number--><!--Device-SwiperContentTransitionProxy-selectedIndex: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

