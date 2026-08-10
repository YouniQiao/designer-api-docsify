# TitleOptions

标题栏选项。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export interface TitleOptions--><!--Device-unnamed-export interface TitleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { GradientBackground, TitleBarType, MixMode, AtomicServiceNavigation, SideBarOptions, TitleOptions, GradientAlpha, NavDestinationBuilder, BackgroundTheme } from 'kits/@kit.ArkUI';
```

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

标题栏背景颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TitleOptions-backgroundColor?: ResourceColor--><!--Device-TitleOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barStyle

```TypeScript
barStyle?: BarStyle
```

设置标题栏样式。

**Type:** [BarStyle](../arkts-components/arkts-arkui-barstyle-e.md)

**Default:** BarStyle.STANDARD

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TitleOptions-barStyle?: BarStyle--><!--Device-TitleOptions-barStyle?: BarStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isBlurEnabled

```TypeScript
isBlurEnabled?: boolean
```

标题栏是否模糊。

**Type:** boolean

**Default:** true

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TitleOptions-isBlurEnabled?: boolean--><!--Device-TitleOptions-isBlurEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleBarType

```TypeScript
titleBarType?: TitleBarType
```

设置标题栏类型。

**Type:** [TitleBarType](arkts-arkui-atomicservice-atomicservicenavigation-titlebartype-e.md)

**Default:** TitleBarType.ROUND_ICON

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TitleOptions-titleBarType?: TitleBarType--><!--Device-TitleOptions-titleBarType?: TitleBarType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleIcon

```TypeScript
titleIcon?: Resource | SymbolGlyphModifier
```

设置标题栏的图标。

**Type:** [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| SymbolGlyphModifier

**Default:** atomicservice icon

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TitleOptions-titleIcon?: Resource | SymbolGlyphModifier--><!--Device-TitleOptions-titleIcon?: Resource | SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

