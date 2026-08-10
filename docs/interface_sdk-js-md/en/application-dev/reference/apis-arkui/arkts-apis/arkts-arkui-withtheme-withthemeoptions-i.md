# WithThemeOptions

设置WithTheme作用域内组件缺省样式及深浅色模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WithThemeOptions--><!--Device-unnamed-export declare interface WithThemeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorMode

```TypeScript
colorMode?: ThemeColorMode
```

用于指定WithTheme作用域内组件配色深浅色模式。

默认值：ThemeColorMode.SYSTEM

**Type:** [ThemeColorMode](../arkts-components/arkts-arkui-themecolormode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeOptions-colorMode?: ThemeColorMode--><!--Device-WithThemeOptions-colorMode?: ThemeColorMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## theme

```TypeScript
theme?: CustomTheme
```

用于自定义WithTheme作用域内组件缺省配色。 

默认值：undefined，缺省样式跟随系统[token默认样式](../../../ui/theme_skinning.md#系统缺省token色值)。

**Type:** [CustomTheme](arkts-arkui-arkui-theme-customtheme-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithThemeOptions-theme?: CustomTheme--><!--Device-WithThemeOptions-theme?: CustomTheme-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

