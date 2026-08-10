# SwiperNestedScrollMode

Swiper组件和父组件的嵌套滚动模式枚举。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum SwiperNestedScrollMode--><!--Device-unnamed-declare enum SwiperNestedScrollMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_ONLY

```TypeScript
SELF_ONLY = 0
```

Swiper只自身滚动，不与父组件联动。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwiperNestedScrollMode-SELF_ONLY = 0--><!--Device-SwiperNestedScrollMode-SELF_ONLY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELF_FIRST

```TypeScript
SELF_FIRST = 1
```

Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SwiperNestedScrollMode-SELF_FIRST = 1--><!--Device-SwiperNestedScrollMode-SELF_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

