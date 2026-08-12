# @ohos.uiExtensionHost

Intended only for the **UIExtensionComponent** that has process isolation requirements, the **uiExtensionHost**module provides APIs for obtaining the host application window information and information about the component itself.

> **NOTE：**
> 
> No new function will be added to this module. Related functions will be provided in the
> [uiExtension](arkts-arkui-uiextension.md#uiExtension) interface.
> 
> The APIs provided by this module are system APIs.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace uiExtensionHost--><!--Device-unnamed-declare namespace uiExtensionHost-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiExtensionHost } from '@kit.ArkUI';
```

## Summary

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [UIExtensionHostWindowProxy](arkts-arkui-uiextensionhost-uiextensionhostwindowproxy-i-sys.md) | Transition Controller |
| [UIExtensionHostWindowProxyProperties](arkts-arkui-uiextensionhost-uiextensionhostwindowproxyproperties-i-sys.md) | Defines information about the host application window and **UIExtensionComponent**. |
<!--DelEnd-->

