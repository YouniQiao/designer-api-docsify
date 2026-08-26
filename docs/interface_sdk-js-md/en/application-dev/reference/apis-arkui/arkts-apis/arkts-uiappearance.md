# @ohos.uiAppearance(UI Appearance)

This module provides basic capabilities for obtaining system appearance configurations, including color mode (dark/ light) settings, font size scale factors, and font weight scale factors.

> **NOTE：**

**Since:** 20

**System capability:** SystemCapability.ArkUI.UiAppearance

## Modules to Import

```TypeScript
import uiAppearance from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getDarkMode(UI Appearance)](arkts-arkui-uiappearance-getdarkmode-f.md) | Obtains the current system dark mode configuration.<!--Del--> |
| [getFontScale(UI Appearance)](arkts-arkui-uiappearance-getfontscale-f.md) | Obtains the current font size scale factor.<!--Del--> |
| [getFontWeightScale(UI Appearance)](arkts-arkui-uiappearance-getfontweightscale-f.md) | Obtains the current font weight scale factor.<!--Del--> |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [setDarkMode(UI Appearance)](arkts-arkui-uiappearance-setdarkmode-f-sys.md) | Sets the system color mode. This API uses an asynchronous callback to return the result.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setDarkMode(UI Appearance)](arkts-arkui-uiappearance-setdarkmode-f-sys.md) | Sets the system color mode. This API uses a promise to return the result.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontScale(UI Appearance)](arkts-arkui-uiappearance-setfontscale-f-sys.md) | Sets the system font scale.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontWeightScale(UI Appearance)](arkts-arkui-uiappearance-setfontweightscale-f-sys.md) | Sets the system font weight scale.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [DarkMode(UI Appearance)](arkts-arkui-uiappearance-darkmode-e.md) | Enumerates the color modes. |
