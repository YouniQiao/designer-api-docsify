# @ohos.uiAppearance

This module provides basic capabilities for obtaining system appearance configurations, including color mode (dark/light) settings, font size scale factors, and font weight scale factors.
> **NOTE**

**Since:** 20

<!--Device-unnamed-declare namespace uiAppearance--><!--Device-unnamed-declare namespace uiAppearance-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getDarkMode](arkts-arkui-uiappearance-getdarkmode-f.md#getdarkmode) | Obtains the current system dark mode configuration.  <!--Del--> |
| [getFontScale](arkts-arkui-uiappearance-getfontscale-f.md#getfontscale) | Obtains the current font size scale factor.  <!--Del--> |
| [getFontWeightScale](arkts-arkui-uiappearance-getfontweightscale-f.md#getfontweightscale) | Obtains the current font weight scale factor.  <!--Del--> |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [setDarkMode](arkts-arkui-uiappearance-setdarkmode-f-sys.md#setdarkmode) | Sets the system color mode. This API uses an asynchronous callback to return the result.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setDarkMode](arkts-arkui-uiappearance-setdarkmode-f-sys.md#setdarkmode-1) | Sets the system color mode. This API uses a promise to return the result.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontScale](arkts-arkui-uiappearance-setfontscale-f-sys.md#setfontscale) | Sets the system font scale.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontWeightScale](arkts-arkui-uiappearance-setfontweightscale-f-sys.md#setfontweightscale) | Sets the system font weight scale.  **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [DarkMode](arkts-arkui-uiappearance-darkmode-e.md) | Enumerates the color modes. |

