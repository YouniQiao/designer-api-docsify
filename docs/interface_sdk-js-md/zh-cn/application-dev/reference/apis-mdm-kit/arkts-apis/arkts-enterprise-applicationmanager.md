# @ohos.enterprise.applicationManager(应用管理)

本模块提供应用管理能力，包括管理应用运行禁止名单、应用运行允许名单、开机自启动应用名单、保活应用名单、不可关停应用名单、后台防冻结应用名单、允许发送通知应用名单、允许跨设备应用名单等。适用于企业设备管理场景，可实现应用运行权限管控、开 机自启动管理、保活应用管理等，提升企业设备安全性和合规性。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。
> [applicationManager.isAppKioskAllowed](arkts-mdm-applicationmanager-isappkioskallowed-f.md)除外，该接口对所有应用开放。

**起始版本：** 12

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedDistributeAbilityConnBundles(应用管理)](arkts-mdm-applicationmanager-addalloweddistributeabilityconnbundles-f.md) |
| [addAllowedNotificationBundles(应用管理)](arkts-mdm-applicationmanager-addallowednotificationbundles-f.md) |
| [addAllowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md) |
| [addAutoStartApps(应用管理)](arkts-mdm-applicationmanager-addautostartapps-f.md) |
| [addAutoStartApps(应用管理)](arkts-mdm-applicationmanager-addautostartapps-f.md) |
| [addDisallowedRunningBundlesSync(应用管理)](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md) |
| [addDockApp(应用管理)](arkts-mdm-applicationmanager-adddockapp-f.md) |
| [addFreezeExemptedApps(应用管理)](arkts-mdm-applicationmanager-addfreezeexemptedapps-f.md) |
| [addHideLauncherIcon(应用管理)](arkts-mdm-applicationmanager-addhidelaunchericon-f.md) |
| [addKeepAliveApps(应用管理)](arkts-mdm-applicationmanager-addkeepaliveapps-f.md) |
| [addKeepAliveApps(应用管理)](arkts-mdm-applicationmanager-addkeepaliveapps-f.md) |
| [addUserNonStopApps(应用管理)](arkts-mdm-applicationmanager-addusernonstopapps-f.md) |
| [clearUpApplicationData(应用管理)](arkts-mdm-applicationmanager-clearupapplicationdata-f.md) |
| [getAllowedDistributeAbilityConnBundles(应用管理)](arkts-mdm-applicationmanager-getalloweddistributeabilityconnbundles-f.md) |
| [getAllowedKioskApps(应用管理)](arkts-mdm-applicationmanager-getallowedkioskapps-f.md) |
| [getAllowedKioskApps(应用管理)](arkts-mdm-applicationmanager-getallowedkioskapps-f.md) |
| [getAllowedNotificationBundles(应用管理)](arkts-mdm-applicationmanager-getallowednotificationbundles-f.md) |
| [getAllowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md) |
| [getAllowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-getallowedrunningbundles-f.md) |
| [getApplicationWindowStates(应用管理)](arkts-mdm-applicationmanager-getapplicationwindowstates-f.md) |
| [getAutoStartApps(应用管理)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getAutoStartApps(应用管理)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getAutoStartApps(应用管理)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getAutoStartApps(应用管理)](arkts-mdm-applicationmanager-getautostartapps-f.md) |
| [getDisallowedRunningBundlesSync(应用管理)](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md) |
| [getDisallowedRunningBundlesSync(应用管理)](arkts-mdm-applicationmanager-getdisallowedrunningbundlessync-f.md) |
| [getDockApps(应用管理)](arkts-mdm-applicationmanager-getdockapps-f.md) |
| [getFreezeExemptedApps(应用管理)](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md) |
| [getFreezeExemptedApps(应用管理)](arkts-mdm-applicationmanager-getfreezeexemptedapps-f.md) |
| [getHideLauncherIcon(应用管理)](arkts-mdm-applicationmanager-gethidelaunchericon-f.md) |
| [getKeepAliveApps(应用管理)](arkts-mdm-applicationmanager-getkeepaliveapps-f.md) |
| [getKeepAliveApps(应用管理)](arkts-mdm-applicationmanager-getkeepaliveapps-f.md) |
| [getUserNonStopApps(应用管理)](arkts-mdm-applicationmanager-getusernonstopapps-f.md) |
| [getUserNonStopApps(应用管理)](arkts-mdm-applicationmanager-getusernonstopapps-f.md) |
| [isAbilityDisabled(应用管理)](arkts-mdm-applicationmanager-isabilitydisabled-f.md) |
| [isAbilityDisabled(应用管理)](arkts-mdm-applicationmanager-isabilitydisabled-f.md) |
| [isAppKioskAllowed(应用管理)](arkts-mdm-applicationmanager-isappkioskallowed-f.md) |
| [isModifyAutoStartAppsDisallowed(应用管理)](arkts-mdm-applicationmanager-ismodifyautostartappsdisallowed-f.md) |
| [isModifyKeepAliveAppsDisallowed(应用管理)](arkts-mdm-applicationmanager-ismodifykeepaliveappsdisallowed-f.md) |
| [queryBundleStatsInfos(应用管理)](arkts-mdm-applicationmanager-querybundlestatsinfos-f.md) |
| [queryTrafficStats(应用管理)](arkts-mdm-applicationmanager-querytrafficstats-f.md) |
| [removeAllowedDistributeAbilityConnBundles(应用管理)](arkts-mdm-applicationmanager-removealloweddistributeabilityconnbundles-f.md) |
| [removeAllowedNotificationBundles(应用管理)](arkts-mdm-applicationmanager-removeallowednotificationbundles-f.md) |
| [removeAllowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-removeallowedrunningbundles-f.md) |
| [removeAutoStartApps(应用管理)](arkts-mdm-applicationmanager-removeautostartapps-f.md) |
| [removeAutoStartApps(应用管理)](arkts-mdm-applicationmanager-removeautostartapps-f.md) |
| [removeDisallowedRunningBundlesSync(应用管理)](arkts-mdm-applicationmanager-removedisallowedrunningbundlessync-f.md) |
| [removeDockApp(应用管理)](arkts-mdm-applicationmanager-removedockapp-f.md) |
| [removeFreezeExemptedApps(应用管理)](arkts-mdm-applicationmanager-removefreezeexemptedapps-f.md) |
| [removeHideLauncherIcon(应用管理)](arkts-mdm-applicationmanager-removehidelaunchericon-f.md) |
| [removeKeepAliveApps(应用管理)](arkts-mdm-applicationmanager-removekeepaliveapps-f.md) |
| [removeUserNonStopApps(应用管理)](arkts-mdm-applicationmanager-removeusernonstopapps-f.md) |
| [setAbilityDisabled(应用管理)](arkts-mdm-applicationmanager-setabilitydisabled-f.md) |
| [setAllowedKioskApps(应用管理)](arkts-mdm-applicationmanager-setallowedkioskapps-f.md) |
| [setKioskFeatures(应用管理)](arkts-mdm-applicationmanager-setkioskfeatures-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md) |
| [addDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md) |
| [addDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md) |
| [getDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md) |
| [getDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md) |
| [getDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-getdisallowedrunningbundles-f-sys.md) |
| [removeDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md) |
| [removeDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md) |
| [removeDisallowedRunningBundles(应用管理)](arkts-mdm-applicationmanager-removedisallowedrunningbundles-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BundleStatsInfo(应用管理)](arkts-mdm-applicationmanager-bundlestatsinfo-i.md) |
| [DockInfo(应用管理)](arkts-mdm-applicationmanager-dockinfo-i.md) |
| [WindowStateInfo(应用管理)](arkts-mdm-applicationmanager-windowstateinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [KioskFeature(应用管理)](arkts-mdm-applicationmanager-kioskfeature-e.md) |
| [ServiceType(应用管理)](arkts-mdm-applicationmanager-servicetype-e.md) |
| [WindowState(应用管理)](arkts-mdm-applicationmanager-windowstate-e.md) |
