# ThemeControl

Class ThemeControl provides the Theme management for whole Ability and pages.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare class ThemeControl--><!--Device-unnamed-export declare class ThemeControl-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Colors } from 'Colors';
import { CustomColors } from 'CustomColors';
import { Theme } from 'Theme';
import { ThemeControl } from 'ThemeControl';
import { CustomTheme } from 'CustomTheme';
import { CustomDarkColors } from 'CustomDarkColors';
```

## setDefaultTheme

```TypeScript
static setDefaultTheme(theme: CustomTheme): void
```

Sets the default Theme: - for whole Ability when invoked from the Ability level code. - for the ArkUI page and for later opened pages when invoked at the ArkUI page level.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme): void--><!--Device-ThemeControl-static setDefaultTheme(theme: CustomTheme): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| theme | [CustomTheme](../../apis-na/arkts-apis/arkts-na-arkui-theme-customtheme-i.md) | Yes |  |

