# ThemeControl

Class ThemeControl provides the Theme management for whole Ability and pages.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class ThemeControl--><!--Device-unnamed-export declare class ThemeControl-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setDefaultTheme

```TypeScript
static setDefaultTheme(theme: CustomTheme | undefined): void
```

Sets the default Theme: - for whole Ability when invoked from the Ability level code. - for the ArkUI page and for later opened pages when invoked at the ArkUI page level.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme | undefined): void--><!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [CustomTheme](arkts-na-arkui-theme-customtheme-i.md) \| undefined | Yes |  |

