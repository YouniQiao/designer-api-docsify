# ThemeControl

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ThemeControl--><!--Device-unnamed-export declare class ThemeControl-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { CustomColors, ThemeControl, Colors, CustomDarkColors, Theme, CustomTheme } from 'kits/@kit.ArkUI';
```

## setDefaultTheme

```TypeScript
static setDefaultTheme(theme: CustomTheme | undefined): void
```

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。

需确保在页面build前执行。因运行于静态类型上下文中的ArkTS不存在全局作用域，因此需要在入口组件的static闭包或aboutToAppear生命周期函数中调用该接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme | undefined): void--><!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [CustomTheme](arkts-arkui-arkui-theme-customtheme-i.md) \| undefined | Yes |  |

