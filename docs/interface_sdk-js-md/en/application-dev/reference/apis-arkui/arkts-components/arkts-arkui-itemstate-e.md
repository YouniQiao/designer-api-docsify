# ItemState

Display status of **nextLabel** in the stepper.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** [Swiper](../arkts-apis/arkts-arkui-swiper-swiper-f.md/arkts-arkui-swiper-swiper-f.md#swiper)

<!--Device-unnamed-declare enum ItemState--><!--Device-unnamed-declare enum ItemState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Normal

```TypeScript
Normal
```

The button on the right is clickable and can navigate users to the next **StepperItem** when it is clicked.

**NOTE：**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use  
[index](../arkts-apis/arkts-arkui-swiper-swiperattribute-i.md/arkts-arkui-swiper-swiperattribute-i.md#index) instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** Swiper.SwiperAttribute#index

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ItemState-Normal--><!--Device-ItemState-Normal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Disabled

```TypeScript
Disabled
```

The button on the right is disabled.

**NOTE：**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use  
[indicatorInteractive](../arkts-apis/arkts-arkui-swiper-swiperattribute-i.md/arkts-arkui-swiper-swiperattribute-i.md#indicatorinteractive) instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** Swiper.SwiperAttribute#indicatorInteractive

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ItemState-Disabled--><!--Device-ItemState-Disabled-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Waiting

```TypeScript
Waiting
```

The button on the right is not displayed, and a progress bar is displayed instead.

**NOTE：**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use  
[Swiper](../arkts-apis/arkts-arkui-swiper-swiper-f.md/arkts-arkui-swiper-swiper-f.md#swiper) instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** [Swiper](../arkts-apis/arkts-arkui-swiper-swiper-f.md/arkts-arkui-swiper-swiper-f.md#swiper)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ItemState-Waiting--><!--Device-ItemState-Waiting-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Skip

```TypeScript
Skip
```

The button on the right reads "Skip" by default. You can define the processing logic for this state in the  
**onSkip** callback of the stepper.

**NOTE：**

This API is supported since API version 8 and deprecated since API version 22. You are advised to use  
[index](../arkts-apis/arkts-arkui-swiper-swiperattribute-i.md/arkts-arkui-swiper-swiperattribute-i.md#index) instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** Swiper.SwiperAttribute#index

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ItemState-Skip--><!--Device-ItemState-Skip-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

