# @ohos.enterprise.applicationManager

This module provides application management capabilities, including managing the application running blocklist, application running trustlist, auto-startup application list, keep-alive application list, non-stoppable application list, background freeze-exempt application list, notification trustlist, and cross-device application trustlist. It is suitable for enterprise device management scenarios, enabling control over application running permissions, auto- startup management, keep-alive application management, and more, thereby enhancing enterprise device security and compliance. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md). The > [applicationManager.isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md#isAppKioskAllowed) API is available to all > applications.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace applicationManager--><!--Device-unnamed-declare namespace applicationManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedDistributeAbilityConnBundles](arkts-mdm-applicationmanager-addalloweddistributeabilityconnbundles-f.md#addAllowedDistributeAbilityConnBundles) |
| [addAllowedNotificationBundles](arkts-mdm-applicationmanager-addallowednotificationbundles-f.md#addAllowedNotificationBundles) |
| [addAllowedRunningBundles](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md#addAllowedRunningBundles) |
| [addAutoStartApps](arkts-mdm-applicationmanager-addautostartapps-f.md#addAutoStartApps) |
| [addAutoStartApps](arkts-mdm-applicationmanager-addautostartapps-f.md#addAutoStartApps) |
| [addDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md#addDisallowedRunningBundlesSync) |
| [addDockApp](arkts-mdm-applicationmanager-adddockapp-f.md#addDockApp) |
| [addFreezeExemptedApps](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md#addFreezeExemptedApps) |
| [addHideLauncherIcon](arkts-mdm-applicationmanager-addhidelaunchericon-f.md#addHideLauncherIcon) |
| [addKeepAliveApps](arkts-mdm-applicationmanager-addkeepaliveapps-f.md#addKeepAliveApps) |
| [addKeepAliveApps](arkts-mdm-applicationmanager-addkeepaliveapps-f.md#addKeepAliveApps) |
| [addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md#addUserNonStopApps) |
| [clearUpApplicationData](arkts-mdm-applicationmanager-clearupapplicationdata-f.md#clearUpApplicationData) |
| [getAllowedDistributeAbilityConnBundles](arkts-mdm-applicationmanager-getalloweddistributeabilityconnbundles-f.md#getAllowedDistributeAbilityConnBundles) |
| [getAllowedKioskApps](arkts-mdm-applicationmanager-getallowedkioskapps-f.md#getAllowedKioskApps) |
| [getAllowedKioskApps](arkts-mdm-applicationmanager-getallowedkioskapps-f.md#getAllowedKioskApps) |
| [getAllowedNotificationBundles](arkts-mdm-applicationmanager-getallowednotificationbundles-f.md#getAllowedNotificationBundles) |
| [getAllowedRunningBundles](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md#getAllowedRunningBundles) |
| [getAllowedRunningBundles](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md#getAllowedRunningBundles) |
| [getApplicationWindowStates](arkts-mdm-applicationmanager-getapplicationwindowstates-f.md#getApplicationWindowStates) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getAutoStartApps) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getAutoStartApps) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getAutoStartApps) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getAutoStartApps) |
| [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getDisallowedRunningBundlesSync) |
| [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getDisallowedRunningBundlesSync) |
| [getDockApps](arkts-mdm-applicationmanager-getdockapps-f.md#getDockApps) |
| [getFreezeExemptedApps](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md#getFreezeExemptedApps) |
| [getFreezeExemptedApps](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md#getFreezeExemptedApps) |
| [getHideLauncherIcon](arkts-mdm-applicationmanager-gethidelaunchericon-f.md#getHideLauncherIcon) |
| [getKeepAliveApps](arkts-mdm-applicationmanager-getkeepaliveapps-f.md#getKeepAliveApps) |
| [getKeepAliveApps](arkts-mdm-applicationmanager-getkeepaliveapps-f.md#getKeepAliveApps) |
| [getUserNonStopApps](arkts-mdm-applicationmanager-getusernonstopapps-f.md#getUserNonStopApps) |
| [getUserNonStopApps](arkts-mdm-applicationmanager-getusernonstopapps-f.md#getUserNonStopApps) |
| [isAbilityDisabled](arkts-mdm-applicationmanager-isabilitydisabled-f.md#isAbilityDisabled) |
| [isAbilityDisabled](arkts-mdm-applicationmanager-isabilitydisabled-f.md#isAbilityDisabled) |
| [isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md#isAppKioskAllowed) |
| [isModifyAutoStartAppsDisallowed](arkts-mdm-applicationmanager-ismodifyautostartappsdisallowed-f.md#isModifyAutoStartAppsDisallowed) |
| [isModifyKeepAliveAppsDisallowed](arkts-mdm-applicationmanager-ismodifykeepaliveappsdisallowed-f.md#isModifyKeepAliveAppsDisallowed) |
| [queryBundleStatsInfos](arkts-mdm-applicationmanager-querybundlestatsinfos-f.md#queryBundleStatsInfos) |
| [queryTrafficStats](arkts-mdm-applicationmanager-querytrafficstats-f.md#queryTrafficStats) |
| [removeAllowedDistributeAbilityConnBundles](arkts-mdm-applicationmanager-removealloweddistributeabilityconnbundles-f.md#removeAllowedDistributeAbilityConnBundles) |
| [removeAllowedNotificationBundles](arkts-mdm-applicationmanager-removeallowednotificationbundles-f.md#removeAllowedNotificationBundles) |
| [removeAllowedRunningBundles](arkts-mdm-applicationmanager-removeallowedrunningbundles-f.md#removeAllowedRunningBundles) |
| [removeAutoStartApps](arkts-mdm-applicationmanager-removeautostartapps-f.md#removeAutoStartApps) |
| [removeAutoStartApps](arkts-mdm-applicationmanager-removeautostartapps-f.md#removeAutoStartApps) |
| [removeDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-removedisallowedrunningbundlessync-f.md#removeDisallowedRunningBundlesSync) |
| [removeDockApp](arkts-mdm-applicationmanager-removedockapp-f.md#removeDockApp) |
| [removeFreezeExemptedApps](arkts-mdm-applicationmanager-removefreezeexemptedapps-f.md#removeFreezeExemptedApps) |
| [removeHideLauncherIcon](arkts-mdm-applicationmanager-removehidelaunchericon-f.md#removeHideLauncherIcon) |
| [removeKeepAliveApps](arkts-mdm-applicationmanager-removekeepaliveapps-f.md#removeKeepAliveApps) |
| [removeUserNonStopApps](arkts-mdm-applicationmanager-removeusernonstopapps-f.md#removeUserNonStopApps) |
| [setAbilityDisabled](arkts-mdm-applicationmanager-setabilitydisabled-f.md#setAbilityDisabled) |
| [setAllowedKioskApps](arkts-mdm-applicationmanager-setallowedkioskapps-f.md#setAllowedKioskApps) |
| [setKioskFeatures](arkts-mdm-applicationmanager-setkioskfeatures-f.md#setKioskFeatures) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles-(System-API)) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles-(System-API)) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles-(System-API)) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md#getDisallowedRunningBundles-(System-API)) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md#getDisallowedRunningBundles-(System-API)) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md#getDisallowedRunningBundles-(System-API)) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md#removeDisallowedRunningBundles-(System-API)) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md#removeDisallowedRunningBundles-(System-API)) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md#removeDisallowedRunningBundles-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BundleStatsInfo](arkts-mdm-applicationmanager-bundlestatsinfo-i.md) |
| [DockInfo](arkts-mdm-applicationmanager-dockinfo-i.md) |
| [WindowStateInfo](arkts-mdm-applicationmanager-windowstateinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KioskFeature](arkts-mdm-applicationmanager-kioskfeature-e.md) |
| [ServiceType](arkts-mdm-applicationmanager-servicetype-e.md) |
| [WindowState](arkts-mdm-applicationmanager-windowstate-e.md) |
