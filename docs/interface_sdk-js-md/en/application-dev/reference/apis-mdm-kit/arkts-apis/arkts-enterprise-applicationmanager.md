# @ohos.enterprise.applicationManager(Application Management)

This module provides application management capabilities, including managing the application running blocklist, application running trustlist, auto-startup application list, keep-alive application list, non-stoppable application list, background freeze-exempt application list, notification trustlist, and cross-device application trustlist. It is suitable for enterprise device management scenarios, enabling control over application running permissions, auto- startup management, keep-alive application management, and more, thereby enhancing enterprise device security and compliance.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md). The
> [applicationManager.isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md) API is available to all
> applications.

**Since:** 12

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedDistributeAbilityConnBundles(Application Management)](arkts-mdm-applicationmanager-addalloweddistributeabilityconnbundles-f.md) |
| [addAllowedNotificationBundles(Application Management)](arkts-mdm-applicationmanager-addallowednotificationbundles-f.md) |
| [addAllowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md) |
| [addAutoStartApps(Application Management)](arkts-mdm-applicationmanager-addautostartapps-f.md) |
| [addAutoStartApps(Application Management)](arkts-mdm-applicationmanager-addautostartapps-f.md) |
| [addDisallowedRunningBundlesSync(Application Management)](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md) |
| [addDockApp(Application Management)](arkts-mdm-applicationmanager-adddockapp-f.md) |
| [addFreezeExemptedApps(Application Management)](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md) |
| [addHideLauncherIcon(Application Management)](arkts-mdm-applicationmanager-addhidelaunchericon-f.md) |
| [addKeepAliveApps(Application Management)](arkts-mdm-applicationmanager-addkeepaliveapps-f.md) |
| [addKeepAliveApps(Application Management)](arkts-mdm-applicationmanager-addkeepaliveapps-f.md) |
| [addUserNonStopApps(Application Management)](arkts-mdm-applicationmanager-addusernonstopapps-f.md) |
| [clearUpApplicationData(Application Management)](arkts-mdm-applicationmanager-clearupapplicationdata-f.md) |
| [getAllowedDistributeAbilityConnBundles(Application Management)](arkts-mdm-applicationmanager-getalloweddistributeabilityconnbundles-f.md) |
| [getAllowedKioskApps(Application Management)](arkts-mdm-applicationmanager-getallowedkioskapps-f.md) |
| [getAllowedKioskApps(Application Management)](arkts-mdm-applicationmanager-getallowedkioskapps-f.md) |
| [getAllowedNotificationBundles(Application Management)](arkts-mdm-applicationmanager-getallowednotificationbundles-f.md) |
| [getAllowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md) |
| [getAllowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md) |
| [getApplicationWindowStates(Application Management)](arkts-mdm-applicationmanager-getapplicationwindowstates-f.md) |
| [getAutoStartApps(Application Management)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getAutoStartApps(Application Management)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getAutoStartApps(Application Management)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getAutoStartApps(Application Management)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getDisallowedRunningBundlesSync(Application Management)](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md) |
| [getDisallowedRunningBundlesSync(Application Management)](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md) |
| [getDockApps(Application Management)](arkts-mdm-applicationmanager-getdockapps-f.md) |
| [getFreezeExemptedApps(Application Management)](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md) |
| [getFreezeExemptedApps(Application Management)](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md) |
| [getHideLauncherIcon(Application Management)](arkts-mdm-applicationmanager-gethidelaunchericon-f.md) |
| [getKeepAliveApps(Application Management)](arkts-mdm-applicationmanager-getkeepaliveapps-f.md) |
| [getKeepAliveApps(Application Management)](arkts-mdm-applicationmanager-getkeepaliveapps-f.md) |
| [getUserNonStopApps(Application Management)](arkts-mdm-applicationmanager-getusernonstopapps-f.md) |
| [getUserNonStopApps(Application Management)](arkts-mdm-applicationmanager-getusernonstopapps-f.md) |
| [isAbilityDisabled(Application Management)](arkts-mdm-applicationmanager-isabilitydisabled-f.md) |
| [isAbilityDisabled(Application Management)](arkts-mdm-applicationmanager-isabilitydisabled-f.md) |
| [isAppKioskAllowed(Application Management)](arkts-mdm-applicationmanager-isappkioskallowed-f.md) |
| [isModifyAutoStartAppsDisallowed(Application Management)](arkts-mdm-applicationmanager-ismodifyautostartappsdisallowed-f.md) |
| [isModifyKeepAliveAppsDisallowed(Application Management)](arkts-mdm-applicationmanager-ismodifykeepaliveappsdisallowed-f.md) |
| [queryBundleStatsInfos(Application Management)](arkts-mdm-applicationmanager-querybundlestatsinfos-f.md) |
| [queryTrafficStats(Application Management)](arkts-mdm-applicationmanager-querytrafficstats-f.md) |
| [removeAllowedDistributeAbilityConnBundles(Application Management)](arkts-mdm-applicationmanager-removealloweddistributeabilityconnbundles-f.md) |
| [removeAllowedNotificationBundles(Application Management)](arkts-mdm-applicationmanager-removeallowednotificationbundles-f.md) |
| [removeAllowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-removeallowedrunningbundles-f.md) |
| [removeAutoStartApps(Application Management)](arkts-mdm-applicationmanager-removeautostartapps-f.md) |
| [removeAutoStartApps(Application Management)](arkts-mdm-applicationmanager-removeautostartapps-f.md) |
| [removeDisallowedRunningBundlesSync(Application Management)](arkts-mdm-applicationmanager-removedisallowedrunningbundlessync-f.md) |
| [removeDockApp(Application Management)](arkts-mdm-applicationmanager-removedockapp-f.md) |
| [removeFreezeExemptedApps(Application Management)](arkts-mdm-applicationmanager-removefreezeexemptedapps-f.md) |
| [removeHideLauncherIcon(Application Management)](arkts-mdm-applicationmanager-removehidelaunchericon-f.md) |
| [removeKeepAliveApps(Application Management)](arkts-mdm-applicationmanager-removekeepaliveapps-f.md) |
| [removeUserNonStopApps(Application Management)](arkts-mdm-applicationmanager-removeusernonstopapps-f.md) |
| [setAbilityDisabled(Application Management)](arkts-mdm-applicationmanager-setabilitydisabled-f.md) |
| [setAllowedKioskApps(Application Management)](arkts-mdm-applicationmanager-setallowedkioskapps-f.md) |
| [setKioskFeatures(Application Management)](arkts-mdm-applicationmanager-setkioskfeatures-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md) |
| [addDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md) |
| [addDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md) |
| [getDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md) |
| [getDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md) |
| [getDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md) |
| [removeDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md) |
| [removeDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md) |
| [removeDisallowedRunningBundles(Application Management)](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BundleStatsInfo(Application Management)](arkts-mdm-applicationmanager-bundlestatsinfo-i.md) |
| [DockInfo(Application Management)](arkts-mdm-applicationmanager-dockinfo-i.md) |
| [WindowStateInfo(Application Management)](arkts-mdm-applicationmanager-windowstateinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KioskFeature(Application Management)](arkts-mdm-applicationmanager-kioskfeature-e.md) |
| [ServiceType(Application Management)](arkts-mdm-applicationmanager-servicetype-e.md) |
| [WindowState(Application Management)](arkts-mdm-applicationmanager-windowstate-e.md) |
