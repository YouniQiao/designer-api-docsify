# @ohos.uiAppearance

This module provides basic capabilities for obtaining system appearance configurations, including color mode (dark/ light) settings, font size scale factors, and font weight scale factors. > **NOTE：**

**Since:** 10

<!--Device-unnamed-declare namespace uiAppearance--><!--Device-unnamed-declare namespace uiAppearance-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiAppearance } from 'uiAppearance';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getDarkMode](arkts-arkui-uiappearance-getdarkmode-f-sys.md#getdarkmode) | Obtains the current system dark mode configuration. &lt;!--Del--&gt; > **NOTE：**> This API is a system API in API version 19 and earlier. Using this API requires the > [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) > permission. &lt;!--DelEnd--&gt; |
| [getFontScale](arkts-arkui-uiappearance-getfontscale-f-sys.md#getfontscale) | Obtains the current font size scale factor. &lt;!--Del--&gt; > **NOTE：**> This API is a system API in API version 19 and earlier. Using this API requires the > [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) > permission. &lt;!--DelEnd--&gt; |
| [getFontWeightScale](arkts-arkui-uiappearance-getfontweightscale-f-sys.md#getfontweightscale) | Obtains the current font weight scale factor. &lt;!--Del--&gt; > **NOTE：**> This API is a system API in API version 19 and earlier. Using this API requires the > [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) > permission. &lt;!--DelEnd--&gt; |
| [setDarkMode](arkts-arkui-uiappearance-setdarkmode-f-sys.md#setdarkmode) | Sets the system color mode. This API uses an asynchronous callback to return the result. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setDarkMode](arkts-arkui-uiappearance-setdarkmode-f-sys.md#setdarkmode-system-api) | Sets the system color mode. This API uses a promise to return the result. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontScale](arkts-arkui-uiappearance-setfontscale-f-sys.md#setfontscale) | Sets the system font scale. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontWeightScale](arkts-arkui-uiappearance-setfontweightscale-f-sys.md#setfontweightscale) | Sets the system font weight scale. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DarkMode](arkts-arkui-uiappearance-darkmode-e-sys.md) | Enumerates the color modes. |
<!--DelEnd-->

