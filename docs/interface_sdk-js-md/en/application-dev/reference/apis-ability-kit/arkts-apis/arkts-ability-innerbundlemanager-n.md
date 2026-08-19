# innerBundleManager

The module provides APIs for the Home Screen application. &gt; **NOTE：**&gt; &gt; This module is deprecated since API version 9. You are advised to use &gt; [launcherBundleManager](arkts-bundle-launcherbundlemanager.md) and &gt; [bundleMonitor](arkts-bundle-bundlemonitor.md) instead. &gt; &gt; The APIs provided by this module are system APIs.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [launcherBundleManager](arkts-bundle-launcherbundlemanager.md)

<!--Device-unnamed-declare namespace innerBundleManager--><!--Device-unnamed-declare namespace innerBundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { innerBundleManager, BundleStatusCallback } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md) | Obtains an array of the launcher ability information based on a given bundle name. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md) &gt; instead. |
| [getLauncherAbilityInfos](arkts-ability-innerbundlemanager-getlauncherabilityinfos-f-sys.md) | Obtains an array of the launcher ability information based on a given bundle name. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md) &gt; instead. |
| [on_BundleStatusChange](arkts-ability-innerbundlemanager-onbundlestatuschange-f-sys.md#onbundlestatuschange) | Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [on](arkts-ability-bundlemonitor-onbundlechangedevent-f-sys.md#on_bundlechangedevent) &gt; instead. |
| [on_BundleStatusChange](arkts-ability-innerbundlemanager-onbundlestatuschange-f-sys.md#onbundlestatuschange) | Registers a callback to receive bundle status changes. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [on](arkts-ability-bundlemonitor-onbundlechangedevent-f-sys.md#on_bundlechangedevent) &gt; instead. |
| [off_BundleStatusChange](arkts-ability-innerbundlemanager-offbundlestatuschange-f-sys.md#offbundlestatuschange) | Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [off](arkts-ability-bundlemonitor-offbundlechangedevent-f-sys.md#off_bundlechangedevent) &gt; instead. |
| [off_BundleStatusChange](arkts-ability-innerbundlemanager-offbundlestatuschange-f-sys.md#offbundlestatuschange) | Unregisters the callback that receives bundle status changes. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [off](arkts-ability-bundlemonitor-offbundlechangedevent-f-sys.md#off_bundlechangedevent) &gt; instead. |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md) | Obtains the information about all launcher abilities. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md) &gt; instead. |
| [getAllLauncherAbilityInfos](arkts-ability-innerbundlemanager-getalllauncherabilityinfos-f-sys.md) | Obtains the information about all launcher abilities. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [getAllLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getalllauncherabilityinfo-f-sys.md) &gt; instead. |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md) | Obtains an array of the shortcut information based on a given bundle name. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md) &gt; instead. |
| [getShortcutInfos](arkts-ability-innerbundlemanager-getshortcutinfos-f-sys.md) | Obtains an array of the shortcut information based on a given bundle name. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; This API has been supported since API version 8 and deprecated since API version 9. You are advised to use &gt; [getShortcutInfo](arkts-ability-launcherbundlemanager-getshortcutinfo-f-sys.md) &gt; instead. |
<!--DelEnd-->

