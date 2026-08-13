# @ohos.enterprise.applicationManager

本模块提供应用管理能力，包括管理应用运行禁止名单、应用运行允许名单、开机自启动应用名单、保活应用名单、不可关停应用名单、后台防冻结应用名单、允许发送通知应用名单、允许跨设备应用名单等。适用于企业设备管理场景，可实现应用运行权限管控、开 机自启动管理、保活应用管理等，提升企业设备安全性和合规性。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。 > [applicationManager.isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md#isAppKioskAllowed)除外，该接口对所有应用开放。

**起始版本：** 10

**废弃版本：** -1

<!--Device-unnamed-declare namespace applicationManager--><!--Device-unnamed-declare namespace applicationManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles（系统接口）) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles（系统接口）) |
| [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles（系统接口）) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md#getDisallowedRunningBundles（系统接口）) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md#getDisallowedRunningBundles（系统接口）) |
| [getDisallowedRunningBundles](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md#getDisallowedRunningBundles（系统接口）) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md#removeDisallowedRunningBundles（系统接口）) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md#removeDisallowedRunningBundles（系统接口）) |
| [removeDisallowedRunningBundles](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md#removeDisallowedRunningBundles（系统接口）) |
<!--DelEnd-->

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
