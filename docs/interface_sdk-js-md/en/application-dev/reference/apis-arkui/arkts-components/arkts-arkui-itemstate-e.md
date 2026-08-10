# ItemState

步骤导航器nextLabel的显示状态。

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

正常状态，右侧文本按钮正常显示，可点击进入下一个StepperItem。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[index](../arkts-apis/arkts-arkui-swiper-swiperattribute-i.md/arkts-arkui-swiper-swiperattribute-i.md#index)替代。

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

不可用状态，右侧文本按钮灰度显示，不可点击进入下一个StepperItem。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](../arkts-apis/arkts-arkui-swiper-swiperattribute-i.md/arkts-arkui-swiper-swiperattribute-i.md#indicatorinteractive)替代。

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

等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个StepperItem。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](../arkts-apis/arkts-arkui-swiper-swiper-f.md/arkts-arkui-swiper-swiper-f.md#swiper)替代。

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

跳过状态，右侧文本按钮默认显示“跳过”，此时可在Stepper的onSkip回调中自定义相关逻辑。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[index](../arkts-apis/arkts-arkui-swiper-swiperattribute-i.md/arkts-arkui-swiper-swiperattribute-i.md#index)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** Swiper.SwiperAttribute#index

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ItemState-Skip--><!--Device-ItemState-Skip-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

