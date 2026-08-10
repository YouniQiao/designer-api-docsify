# IndicatorComponentController

Indicator组件的控制器，可以将此对象绑定至Indicator组件来控制翻页。通过将同一IndicatorComponentController实例传入IndicatorComponent的构造函数和Swiper组件的indicator属性，可实现Indicator与Swiper的绑定联动。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare class IndicatorComponentController--><!--Device-unnamed-declare class IndicatorComponentController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(index: number, useAnimation?: boolean):void
```

翻至指定导航点。适用于需要跳转到指定导航点的场景。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-IndicatorComponentController-changeIndex(index: number, useAnimation?: boolean):void--><!--Device-IndicatorComponentController-changeIndex(index: number, useAnimation?: boolean):void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 指定导航点在Swiper中的索引值。&lt;br/&gt;**说明：** &lt;br/&gt;设置的值小于0或大于最大导航点索引时，取0。 |
| useAnimation | boolean | No | 设置翻至指定导航点时是否有动效，true表示有动效，false表示没有动效。&lt;br/&gt;默认值：false。 |

## constructor

```TypeScript
constructor()
```

IndicatorComponentController的构造函数。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-IndicatorComponentController-constructor()--><!--Device-IndicatorComponentController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showNext

```TypeScript
showNext():void
```

跳转到下一导航点。当与Swiper组件绑定时，同时会控制Swiper切换至下一页面。适用于通过按钮或其他交互方式控制导航点切换的场景。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-IndicatorComponentController-showNext():void--><!--Device-IndicatorComponentController-showNext():void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showPrevious

```TypeScript
showPrevious():void
```

跳转到上一导航点。当与Swiper组件绑定时，同时会控制Swiper切换至上一页面。适用于通过按钮等交互方式控制导航点切换的场景。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-IndicatorComponentController-showPrevious():void--><!--Device-IndicatorComponentController-showPrevious():void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

