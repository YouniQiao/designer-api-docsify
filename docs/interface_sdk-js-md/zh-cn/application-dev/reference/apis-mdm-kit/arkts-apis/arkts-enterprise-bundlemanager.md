# @ohos.enterprise.bundleManager(包管理)

本模块提供包管理能力，包括安装和卸载应用包，管理包安装允许名单、包安装禁止名单、包卸载禁止名单、可安装应用的分发类型等。在企业设备管理场景中，通过这些能力可以实现应用安装卸载的精细化管控，防止未授权应用的安装和卸载，保障企业设备安全， 降低安全风险。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-addallowedinstallbundlessync-f.md) |
| [addDisallowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-adddisallowedinstallbundlessync-f.md) |
| [addDisallowedUninstallBundlesSync(包管理)](arkts-mdm-bundlemanager-adddisalloweduninstallbundlessync-f.md) |
| [addInstallationAllowedAppDistributionTypes(包管理)](arkts-mdm-bundlemanager-addinstallationallowedappdistributiontypes-f.md) |
| [getAllowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md) |
| [getAllowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md) |
| [getDisallowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md) |
| [getDisallowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md) |
| [getDisallowedUninstallBundlesSync(包管理)](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md) |
| [getDisallowedUninstallBundlesSync(包管理)](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md) |
| [getInstallationAllowedAppDistributionTypes(包管理)](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md) |
| [getInstallationAllowedAppDistributionTypes(包管理)](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md) |
| [getInstalledBundleList(包管理)](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md) |
| [getInstalledBundleList(包管理)](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md) |
| [getInstalledBundleStorageStats(包管理)](arkts-mdm-bundlemanager-getinstalledbundlestoragestats-f.md) |
| [install(包管理)](arkts-mdm-bundlemanager-install-f.md) |
| [installForResult(包管理)](arkts-mdm-bundlemanager-installforresult-f.md) |
| [installMarketApps(包管理)](arkts-mdm-bundlemanager-installmarketapps-f.md) |
| [removeAllowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-removeallowedinstallbundlessync-f.md) |
| [removeDisallowedInstallBundlesSync(包管理)](arkts-mdm-bundlemanager-removedisallowedinstallbundlessync-f.md) |
| [removeDisallowedUninstallBundlesSync(包管理)](arkts-mdm-bundlemanager-removedisalloweduninstallbundlessync-f.md) |
| [removeInstallationAllowedAppDistributionTypes(包管理)](arkts-mdm-bundlemanager-removeinstallationallowedappdistributiontypes-f.md) |
| [uninstall(包管理)](arkts-mdm-bundlemanager-uninstall-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md) |
| [addAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md) |
| [addAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md) |
| [addDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md) |
| [addDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md) |
| [addDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md) |
| [addDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md) |
| [addDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md) |
| [addDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md) |
| [getAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md) |
| [getAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md) |
| [getAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md) |
| [getDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md) |
| [getDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md) |
| [getDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md) |
| [getDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md) |
| [getDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md) |
| [getDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md) |
| [install(包管理)](arkts-mdm-bundlemanager-install-f-sys.md) |
| [install(包管理)](arkts-mdm-bundlemanager-install-f-sys.md) |
| [removeAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md) |
| [removeAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md) |
| [removeAllowedInstallBundles(包管理)](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md) |
| [removeDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md) |
| [removeDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md) |
| [removeDisallowedInstallBundles(包管理)](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md) |
| [removeDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md) |
| [removeDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md) |
| [removeDisallowedUninstallBundles(包管理)](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md) |
| [uninstall(包管理)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
| [uninstall(包管理)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
| [uninstall(包管理)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
| [uninstall(包管理)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [ApplicationInfo(包管理)](arkts-mdm-bundlemanager-applicationinfo-i.md) |
| [BundleInfo(包管理)](arkts-mdm-bundlemanager-bundleinfo-i.md) |
| [BundleStorageStats(包管理)](arkts-mdm-bundlemanager-bundlestoragestats-i.md) |
| [InstallParam(包管理)](arkts-mdm-bundlemanager-installparam-i.md) |
| [Resource(包管理)](arkts-mdm-bundlemanager-resource-i.md) |
| [SignatureInfo(包管理)](arkts-mdm-bundlemanager-signatureinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [AppDistributionType(包管理)](arkts-mdm-bundlemanager-appdistributiontype-e.md) |
| [BundleInfoGetFlag(包管理)](arkts-mdm-bundlemanager-bundleinfogetflag-e.md) |
