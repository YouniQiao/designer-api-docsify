# GradientBackground

品牌渐变色选项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-export interface GradientBackground--><!--Device-unnamed-export interface GradientBackground-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { GradientBackground, TitleBarType, MixMode, AtomicServiceNavigation, SideBarOptions, TitleOptions, GradientAlpha, NavDestinationBuilder, BackgroundTheme } from 'kits/@kit.ArkUI';
```

## alpha

```TypeScript
alpha?: GradientAlpha
```

设置渐变色显示区域的不透明度。

**Type:** [GradientAlpha](arkts-arkui-atomicservice-atomicservicenavigation-gradientalpha-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GradientBackground-alpha?: GradientAlpha--><!--Device-GradientBackground-alpha?: GradientAlpha-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundTheme

```TypeScript
backgroundTheme?: BackgroundTheme
```

导航栏背景底色。

**Type:** [BackgroundTheme](arkts-arkui-atomicservice-atomicservicenavigation-backgroundtheme-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GradientBackground-backgroundTheme?: BackgroundTheme--><!--Device-GradientBackground-backgroundTheme?: BackgroundTheme-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mixMode

```TypeScript
mixMode?: MixMode
```

同时设置primaryColor和secondaryColor时此参数生效。表示双色渐变下两种颜色的融合方式。

**Type:** [MixMode](arkts-arkui-atomicservice-atomicservicenavigation-mixmode-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GradientBackground-mixMode?: MixMode--><!--Device-GradientBackground-mixMode?: MixMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryColor

```TypeScript
primaryColor: ResourceColor
```

单色渐变色彩值和双色渐变第一色彩值。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GradientBackground-primaryColor: ResourceColor--><!--Device-GradientBackground-primaryColor: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryColor

```TypeScript
secondaryColor?: ResourceColor
```

双色渐变色第二色彩值。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-GradientBackground-secondaryColor?: ResourceColor--><!--Device-GradientBackground-secondaryColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

