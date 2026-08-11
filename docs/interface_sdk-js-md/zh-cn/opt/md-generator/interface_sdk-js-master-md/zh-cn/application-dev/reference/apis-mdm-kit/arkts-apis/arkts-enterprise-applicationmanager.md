# @ohos.enterprise.applicationManager(应用管理)

本模块提供应用管理能力，包括管理应用运行禁止名单、应用运行允许名单、开机自启动应用名单、保活应用名单、不可关停应用名单、后台防冻结应用名单、允许发送通知应用名单、允许跨设备应用名单等。适用于企业设备管理场景，可实现应用运行权限管控、开机自启动管理、保活应用管理等，提升企业设备安全性和合规性。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。
> [applicationManager.isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md#isappkioskallowed)除外，该接口对所有应用开放。

**起始版本：** 12

<!--Device-unnamed-declare namespace applicationManager--><!--Device-unnamed-declare namespace applicationManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
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

### 接口

| 名称 |
| --- |
| [BundleStatsInfo](arkts-mdm-applicationmanager-bundlestatsinfo-i.md) |
| [DockInfo](arkts-mdm-applicationmanager-dockinfo-i.md) |
| [WindowStateInfo](arkts-mdm-applicationmanager-windowstateinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [KioskFeature](arkts-mdm-applicationmanager-kioskfeature-e.md) |
| [ServiceType](arkts-mdm-applicationmanager-servicetype-e.md) |
| [WindowState](arkts-mdm-applicationmanager-windowstate-e.md) |
