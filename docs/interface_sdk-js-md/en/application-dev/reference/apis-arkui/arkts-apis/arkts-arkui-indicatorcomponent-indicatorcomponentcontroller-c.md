# IndicatorComponentController

Indicator组件的控制器，可以将此对象绑定至Indicator组件来控制翻页。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class IndicatorComponentController--><!--Device-unnamed-export declare class IndicatorComponentController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(index: int | undefined, useAnimation?: boolean): void
```

翻至指定页面。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-changeIndex(index: int | undefined, useAnimation?: boolean): void--><!--Device-IndicatorComponentController-changeIndex(index: int | undefined, useAnimation?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes | 指定页面在Swiper中的索引值。 |
| useAnimation | boolean | No | 设置翻至指定页面时是否有动效，true表示有动效，false表示没有动效。&lt;br/&gt;默认值：false。 |

## constructor

```TypeScript
constructor()
```

IndicatorComponentController的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-constructor()--><!--Device-IndicatorComponentController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showNext

```TypeScript
showNext(): void
```

跳转到下一导航点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-showNext(): void--><!--Device-IndicatorComponentController-showNext(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showPrevious

```TypeScript
showPrevious(): void
```

跳转到上一导航点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndicatorComponentController-showPrevious(): void--><!--Device-IndicatorComponentController-showPrevious(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

