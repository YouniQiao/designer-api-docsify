# CustomTheme

Defines the struct of CustomTheme.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface CustomTheme--><!--Device-unnamed-export declare interface CustomTheme-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CustomColors, ThemeControl, Colors, CustomDarkColors, Theme, CustomTheme } from '@kit.ArkUI';
```

## colors

```TypeScript
colors?: CustomColors
```

Define tokens associated with color resources..

**Type:** [CustomColors](arkts-arkui-customcolors-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomTheme-colors?: CustomColors--><!--Device-CustomTheme-colors?: CustomColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## darkColors

```TypeScript
darkColors?: CustomDarkColors
```

Define tokens associated with dark mode color resources.

**Type:** [CustomDarkColors](arkts-arkui-customdarkcolors-t.md)

**Default:** If not set darkColors, color value will same as colors under light mode and will not change with color mode, unless the color is setted by resource in dark directory.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CustomTheme-darkColors?: CustomDarkColors--><!--Device-CustomTheme-darkColors?: CustomDarkColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

