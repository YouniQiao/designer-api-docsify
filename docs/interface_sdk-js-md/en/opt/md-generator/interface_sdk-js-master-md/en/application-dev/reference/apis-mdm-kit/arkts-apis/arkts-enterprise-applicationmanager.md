# @ohos.enterprise.applicationManager(Application Management)

This module provides application management capabilities, including managing the application running blocklist,application running trustlist, auto-startup application list, keep-alive application list, non-stoppable application list, background freeze-exempt application list, notification trustlist, and cross-device application trustlist. It is suitable for enterprise device management scenarios, enabling control over application running permissions, auto-startup management, keep-alive application management, and more, thereby enhancing enterprise device security and compliance.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md). The
> [applicationManager.isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md#isAppKioskAllowed) API is available to all
> applications.

**Since:** 12

<!--Device-unnamed-declare namespace applicationManager--><!--Device-unnamed-declare namespace applicationManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedDistributeAbilityConnBundles](arkts-mdm-applicationmanager-addalloweddistributeabilityconnbundles-f.md#addalloweddistributeabilityconnbundles) |
| [addAllowedNotificationBundles](arkts-mdm-applicationmanager-addallowednotificationbundles-f.md#addallowednotificationbundles) |
| [addAllowedRunningBundles](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md#addallowedrunningbundles) |
| [addAutoStartApps](arkts-mdm-applicationmanager-addautostartapps-f.md#addautostartapps) |
| [addAutoStartApps](arkts-mdm-applicationmanager-addautostartapps-f.md#addautostartapps-1) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f.md#adddisallowedrunningbundles) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f.md#adddisallowedrunningbundles-1) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f.md#adddisallowedrunningbundles-2) |
| [addDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md#adddisallowedrunningbundlessync) |
| [addDockApp](arkts-mdm-applicationmanager-adddockapp-f.md#adddockapp) |
| [addFreezeExemptedApps](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md#addfreezeexemptedapps) |
| [addHideLauncherIcon](arkts-mdm-applicationmanager-addhidelaunchericon-f.md#addhidelaunchericon) |
| [addKeepAliveApps](arkts-mdm-applicationmanager-addkeepaliveapps-f.md#addkeepaliveapps) |
| [addKeepAliveApps](arkts-mdm-applicationmanager-addkeepaliveapps-f.md#addkeepaliveapps-1) |
| [addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md#addusernonstopapps) |
| [clearUpApplicationData](arkts-mdm-applicationmanager-clearupapplicationdata-f.md#clearupapplicationdata) |
| [getAllowedDistributeAbilityConnBundles](arkts-mdm-applicationmanager-getalloweddistributeabilityconnbundles-f.md#getalloweddistributeabilityconnbundles) |
| [getAllowedKioskApps](arkts-mdm-applicationmanager-getallowedkioskapps-f.md#getallowedkioskapps) |
| [getAllowedKioskApps](arkts-mdm-applicationmanager-getallowedkioskapps-f.md#getallowedkioskapps-1) |
| [getAllowedNotificationBundles](arkts-mdm-applicationmanager-getallowednotificationbundles-f.md#getallowednotificationbundles) |
| [getAllowedRunningBundles](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md#getallowedrunningbundles) |
| [getAllowedRunningBundles](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md#getallowedrunningbundles-1) |
| [getApplicationWindowStates](arkts-mdm-applicationmanager-getapplicationwindowstates-f.md#getapplicationwindowstates) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getautostartapps) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getautostartapps-1) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getautostartapps-2) |
| [getAutoStartApps](arkts-mdm-applicationmanager-getautostartapps-f.md#getautostartapps-3) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f.md#getdisallowedrunningbundles) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f.md#getdisallowedrunningbundles-1) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f.md#getdisallowedrunningbundles-2) |
| [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getdisallowedrunningbundlessync) |
| [getDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md#getdisallowedrunningbundlessync-1) |
| [getDockApps](arkts-mdm-applicationmanager-getdockapps-f.md#getdockapps) |
| [getFreezeExemptedApps](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md#getfreezeexemptedapps) |
| [getFreezeExemptedApps](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md#getfreezeexemptedapps-1) |
| [getHideLauncherIcon](arkts-mdm-applicationmanager-gethidelaunchericon-f.md#gethidelaunchericon) |
| [getKeepAliveApps](arkts-mdm-applicationmanager-getkeepaliveapps-f.md#getkeepaliveapps) |
| [getKeepAliveApps](arkts-mdm-applicationmanager-getkeepaliveapps-f.md#getkeepaliveapps-1) |
| [getUserNonStopApps](arkts-mdm-applicationmanager-getusernonstopapps-f.md#getusernonstopapps) |
| [getUserNonStopApps](arkts-mdm-applicationmanager-getusernonstopapps-f.md#getusernonstopapps-1) |
| [isAbilityDisabled](arkts-mdm-applicationmanager-isabilitydisabled-f.md#isabilitydisabled) |
| [isAbilityDisabled](arkts-mdm-applicationmanager-isabilitydisabled-f.md#isabilitydisabled-1) |
| [isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md#isappkioskallowed) |
| [isModifyAutoStartAppsDisallowed](arkts-mdm-applicationmanager-ismodifyautostartappsdisallowed-f.md#ismodifyautostartappsdisallowed) |
| [isModifyKeepAliveAppsDisallowed](arkts-mdm-applicationmanager-ismodifykeepaliveappsdisallowed-f.md#ismodifykeepaliveappsdisallowed) |
| [queryBundleStatsInfos](arkts-mdm-applicationmanager-querybundlestatsinfos-f.md#querybundlestatsinfos) |
| [queryTrafficStats](arkts-mdm-applicationmanager-querytrafficstats-f.md#querytrafficstats) |
| [removeAllowedDistributeAbilityConnBundles](arkts-mdm-applicationmanager-removealloweddistributeabilityconnbundles-f.md#removealloweddistributeabilityconnbundles) |
| [removeAllowedNotificationBundles](arkts-mdm-applicationmanager-removeallowednotificationbundles-f.md#removeallowednotificationbundles) |
| [removeAllowedRunningBundles](arkts-mdm-applicationmanager-removeallowedrunningbundles-f.md#removeallowedrunningbundles) |
| [removeAutoStartApps](arkts-mdm-applicationmanager-removeautostartapps-f.md#removeautostartapps) |
| [removeAutoStartApps](arkts-mdm-applicationmanager-removeautostartapps-f.md#removeautostartapps-1) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f.md#removedisallowedrunningbundles) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f.md#removedisallowedrunningbundles-1) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f.md#removedisallowedrunningbundles-2) |
| [removeDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-removedisallowedrunningbundlessync-f.md#removedisallowedrunningbundlessync) |
| [removeDockApp](arkts-mdm-applicationmanager-removedockapp-f.md#removedockapp) |
| [removeFreezeExemptedApps](arkts-mdm-applicationmanager-removefreezeexemptedapps-f.md#removefreezeexemptedapps) |
| [removeHideLauncherIcon](arkts-mdm-applicationmanager-removehidelaunchericon-f.md#removehidelaunchericon) |
| [removeKeepAliveApps](arkts-mdm-applicationmanager-removekeepaliveapps-f.md#removekeepaliveapps) |
| [removeUserNonStopApps](arkts-mdm-applicationmanager-removeusernonstopapps-f.md#removeusernonstopapps) |
| [setAbilityDisabled](arkts-mdm-applicationmanager-setabilitydisabled-f.md#setabilitydisabled) |
| [setAllowedKioskApps](arkts-mdm-applicationmanager-setallowedkioskapps-f.md#setallowedkioskapps) |
| [setKioskFeatures](arkts-mdm-applicationmanager-setkioskfeatures-f.md#setkioskfeatures) |

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
