# @ohos.app.ability.quickFixManager

The quickFixManager module provides APIs for quick fix. With quick fix, you can fix bugs in your application by applying patches, which is more efficient than by updating the entire application.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace quickFixManager--><!--Device-unnamed-declare namespace quickFixManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.QuickFix

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { quickFixManager } from 'quickFixManager';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [applyQuickFix](arkts-ability-quickfixmanager-applyquickfix-f-sys.md#applyQuickFix) | Applies a quick fix patch. This API uses an asynchronous callback to return the result. |
| [applyQuickFix](arkts-ability-quickfixmanager-applyquickfix-f-sys.md#applyQuickFix-(System-API)) | Applies a quick fix patch. This API uses a promise to return the result. |
| [getApplicationQuickFixInfo](arkts-ability-quickfixmanager-getapplicationquickfixinfo-f-sys.md#getApplicationQuickFixInfo) | Obtains the quick fix information of the application. This API uses an asynchronous callback to return the result. |
| [getApplicationQuickFixInfo](arkts-ability-quickfixmanager-getapplicationquickfixinfo-f-sys.md#getApplicationQuickFixInfo-(System-API)) | Obtains the quick fix information of the application. This API uses a promise to return the result. |
| [revokeQuickFix](arkts-ability-quickfixmanager-revokequickfix-f-sys.md#revokeQuickFix) | Revokes quick fix. This API uses an asynchronous callback to return the result. |
| [revokeQuickFix](arkts-ability-quickfixmanager-revokequickfix-f-sys.md#revokeQuickFix-(System-API)) | Revokes quick fix. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ApplicationQuickFixInfo](arkts-ability-quickfixmanager-applicationquickfixinfo-i-sys.md) | Defines the quick fix information at the application level. |
| [HapModuleQuickFixInfo](arkts-ability-quickfixmanager-hapmodulequickfixinfo-i-sys.md) | Defines the quick fix information at the HAP file level. |
<!--DelEnd-->

