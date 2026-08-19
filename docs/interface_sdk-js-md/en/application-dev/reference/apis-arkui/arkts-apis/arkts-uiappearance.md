# @ohos.uiAppearance

This module provides basic capabilities for obtaining system appearance configurations, including color mode (dark/ light) settings, font size scale factors, and font weight scale factors. &gt; **NOTE：**

**Since:** 10

<!--Device-unnamed-declare namespace uiAppearance--><!--Device-unnamed-declare namespace uiAppearance-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getDarkMode](arkts-arkui-uiappearance-getdarkmode-f-sys.md) | Obtains the current system dark mode configuration. <!--Del--> &gt; **NOTE：**&gt; This API is a system API in API version 19 and earlier. Using this API requires the &gt; [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) &gt; permission. <!--DelEnd--> |
| [getFontScale](arkts-arkui-uiappearance-getfontscale-f-sys.md) | Obtains the current font size scale factor. <!--Del--> &gt; **NOTE：**&gt; This API is a system API in API version 19 and earlier. Using this API requires the &gt; [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) &gt; permission. <!--DelEnd--> |
| [getFontWeightScale](arkts-arkui-uiappearance-getfontweightscale-f-sys.md) | Obtains the current font weight scale factor. <!--Del--> &gt; **NOTE：**&gt; This API is a system API in API version 19 and earlier. Using this API requires the &gt; [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) &gt; permission. <!--DelEnd--> |
| [setDarkMode](arkts-arkui-uiappearance-setdarkmode-f-sys.md) | Sets the system color mode. This API uses an asynchronous callback to return the result. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setDarkMode](arkts-arkui-uiappearance-setdarkmode-f-sys.md) | Sets the system color mode. This API uses a promise to return the result. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontScale](arkts-arkui-uiappearance-setfontscale-f-sys.md) | Sets the system font scale. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
| [setFontWeightScale](arkts-arkui-uiappearance-setfontweightscale-f-sys.md) | Sets the system font weight scale. **Permission required**: ohos.permission.UPDATE_CONFIGURATION |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [DarkMode](arkts-arkui-uiappearance-darkmode-e-sys.md) | Enumerates the color modes. |
<!--DelEnd-->

