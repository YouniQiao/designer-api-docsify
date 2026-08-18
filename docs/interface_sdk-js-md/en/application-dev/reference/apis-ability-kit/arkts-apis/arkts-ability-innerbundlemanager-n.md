# innerBundleManager

The module provides APIs for the Home Screen application. > **NOTE：**> > This module is deprecated since API version 9. You are advised to use > [launcherBundleManager](arkts-bundle-launcherbundlemanager.md#ohosbundlelauncherbundlemanager) and > [bundleMonitor](arkts-bundle-bundlemonitor.md#ohosbundlebundlemonitor) instead. > > The APIs provided by this module are system APIs.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [launcherBundleManager](arkts-bundle-launcherbundlemanager.md#ohosbundlelauncherbundlemanager)

<!--Device-unnamed-declare namespace innerBundleManager--><!--Device-unnamed-declare namespace innerBundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { innerBundleManager, BundleStatusCallback } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md#getlauncherabilityinfos) | Obtains an array of the launcher ability information based on a given bundle name. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getlauncherabilityinfo-system-api) > instead. |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md#getlauncherabilityinfos-system-api) | Obtains an array of the launcher ability information based on a given bundle name. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getlauncherabilityinfo-system-api) > instead. |
| [on_BundleStatusChange](arkts-ability-innerbundlemanager-onbundlestatuschange-f-sys.md#onbundlestatuschange) | Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [on](arkts-ability-bundlemonitor-onbundlechangedevent-f-sys.md#onbundlechangedevent) > instead. |
| [on_BundleStatusChange](arkts-ability-innerbundlemanager-onbundlestatuschange-f-sys.md#onbundlestatuschange-1) | Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [on](arkts-ability-bundlemonitor-onbundlechangedevent-f-sys.md#onbundlechangedevent) > instead. |
| [off_BundleStatusChange](arkts-ability-innerbundlemanager-offbundlestatuschange-f-sys.md#offbundlestatuschange) | Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [off](arkts-ability-bundlemonitor-offbundlechangedevent-f-sys.md#offbundlechangedevent) > instead. |
| [off_BundleStatusChange](arkts-ability-innerbundlemanager-offbundlestatuschange-f-sys.md#offbundlestatuschange-1) | Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [off](arkts-ability-bundlemonitor-offbundlechangedevent-f-sys.md#offbundlechangedevent) > instead. |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md#getalllauncherabilityinfos) | Obtains the information about all launcher abilities. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getalllauncherabilityinfo-system-api) > instead. |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md#getalllauncherabilityinfos-system-api) | Obtains the information about all launcher abilities. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md#getalllauncherabilityinfo-system-api) > instead. |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md#getshortcutinfos) | Obtains an array of the shortcut information based on a given bundle name. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getshortcutinfo-system-api) > instead. |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md#getshortcutinfos-system-api) | Obtains an array of the shortcut information based on a given bundle name. This API uses a promise to return the result. > **NOTE：**> > This API has been supported since API version 8 and deprecated since API version 9. You are advised to use > [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md#getshortcutinfo-system-api) > instead. |
<!--DelEnd-->

