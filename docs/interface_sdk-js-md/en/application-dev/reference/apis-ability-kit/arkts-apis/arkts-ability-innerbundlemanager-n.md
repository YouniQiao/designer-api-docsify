# innerBundleManager

The module provides APIs for the Home Screen application. > **NOTE：**> > This module is deprecated since API version 9. You are advised to use > [launcherBundleManager](arkts-bundle-launcherbundlemanager.md#@ohos.bundle.launcherBundleManager) and > [bundleMonitor](arkts-bundle-bundlemonitor.md#@ohos.bundle.bundleMonitor) instead. > > The APIs provided by this module are system APIs.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [launcherBundleManager](arkts-bundle-launcherbundlemanager.md#@ohos.bundle.launcherBundleManager)

<!--Device-unnamed-declare namespace innerBundleManager--><!--Device-unnamed-declare namespace innerBundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { BundleStatusCallback } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md#getLauncherAbilityInfos) | Obtains an array of the launcher ability information based on a given bundle name. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getLauncherAbilityInfo-(System-API)) > instead. |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md#getLauncherAbilityInfos-(System-API)) | Obtains an array of the launcher ability information based on a given bundle name. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getLauncherAbilityInfo-(System-API)) > instead. |
| [on_BundleStatusChange](arkts-ability-innerbundlemanager-onbundlestatuschange-f-sys.md#on_BundleStatusChange) | Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [on](arkts-ability-bundlemonitor-onbundlechangedevent-f-sys.md#on_BundleChangedEvent) > instead. |
| [on_BundleStatusChange](arkts-ability-innerbundlemanager-onbundlestatuschange-f-sys.md#on_BundleStatusChange) | Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [on](arkts-ability-bundlemonitor-onbundlechangedevent-f-sys.md#on_BundleChangedEvent) > instead. |
| [off_BundleStatusChange](arkts-ability-innerbundlemanager-offbundlestatuschange-f-sys.md#off_BundleStatusChange) | Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [off](arkts-ability-bundlemonitor-offbundlechangedevent-f-sys.md#off_BundleChangedEvent) > instead. |
| [off_BundleStatusChange](arkts-ability-innerbundlemanager-offbundlestatuschange-f-sys.md#off_BundleStatusChange) | Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [off](arkts-ability-bundlemonitor-offbundlechangedevent-f-sys.md#off_BundleChangedEvent) > instead. |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md#getAllLauncherAbilityInfos) | Obtains the information about all launcher abilities. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo-(System-API)) > instead. |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md#getAllLauncherAbilityInfos-(System-API)) | Obtains the information about all launcher abilities. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getAllLauncherAbilityInfo-(System-API)) > instead. |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md#getShortcutInfos) | Obtains an array of the shortcut information based on a given bundle name. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getShortcutInfo-(System-API)) > instead. |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md#getShortcutInfos-(System-API)) | Obtains an array of the shortcut information based on a given bundle name. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getShortcutInfo-(System-API)) > instead. |
<!--DelEnd-->

