# CustomTheme

Defines the struct of CustomTheme.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CustomTheme--><!--Device-unnamed-export declare interface CustomTheme-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors?: CustomColors
```

Define tokens associated with color resources..

**Type:** CustomColors

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomTheme-colors?: CustomColors--><!--Device-CustomTheme-colors?: CustomColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## darkColors

```TypeScript
darkColors?: CustomDarkColors
```

Define tokens associated with dark mode color resources.

**Type:** CustomDarkColors

**Default:** If not set darkColors, color value will same as colors under light mode and will not change with color
mode, unless the color is setted by resource in dark directory.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomTheme-darkColors?: CustomDarkColors--><!--Device-CustomTheme-darkColors?: CustomDarkColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

