# @ohos.enterprise.bundleManager(包管理)

本模块提供包管理能力，包括安装和卸载应用包，管理包安装允许名单、包安装禁止名单、包卸载禁止名单、可安装应用的分发类型等。在企业设备管理场景中，通过这些能力可以实现应用安装卸载的精细化管控，防止未授权应用的安装和卸载，保障企业设备安全，降低安全风险。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f.md#addallowedinstallbundles) |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f.md#addallowedinstallbundles-1) |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f.md#addallowedinstallbundles-2) |
| [addAllowedInstallBundlesSync](arkts-mdm-bundlemanager-addallowedinstallbundlessync-f.md#addallowedinstallbundlessync) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f.md#adddisallowedinstallbundles) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f.md#adddisallowedinstallbundles-1) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f.md#adddisallowedinstallbundles-2) |
| [addDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-adddisallowedinstallbundlessync-f.md#adddisallowedinstallbundlessync) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f.md#adddisalloweduninstallbundles) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f.md#adddisalloweduninstallbundles-1) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f.md#adddisalloweduninstallbundles-2) |
| [addDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-adddisalloweduninstallbundlessync-f.md#adddisalloweduninstallbundlessync) |
| [addInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-addinstallationallowedappdistributiontypes-f.md#addinstallationallowedappdistributiontypes) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f.md#getallowedinstallbundles) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f.md#getallowedinstallbundles-1) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f.md#getallowedinstallbundles-2) |
| [getAllowedInstallBundlesSync](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md#getallowedinstallbundlessync) |
| [getAllowedInstallBundlesSync](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md#getallowedinstallbundlessync-1) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f.md#getdisallowedinstallbundles) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f.md#getdisallowedinstallbundles-1) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f.md#getdisallowedinstallbundles-2) |
| [getDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md#getdisallowedinstallbundlessync) |
| [getDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md#getdisallowedinstallbundlessync-1) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f.md#getdisalloweduninstallbundles) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f.md#getdisalloweduninstallbundles-1) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f.md#getdisalloweduninstallbundles-2) |
| [getDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md#getdisalloweduninstallbundlessync) |
| [getDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md#getdisalloweduninstallbundlessync-1) |
| [getInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md#getinstallationallowedappdistributiontypes) |
| [getInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md#getinstallationallowedappdistributiontypes-1) |
| [getInstalledBundleList](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md#getinstalledbundlelist) |
| [getInstalledBundleList](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md#getinstalledbundlelist-1) |
| [getInstalledBundleStorageStats](arkts-mdm-bundlemanager-getinstalledbundlestoragestats-f.md#getinstalledbundlestoragestats) |
| [install](arkts-mdm-bundlemanager-install-f.md#install) |
| [install](arkts-mdm-bundlemanager-install-f.md#install-1) |
| [install](arkts-mdm-bundlemanager-install-f.md#install-2) |
| [installForResult](arkts-mdm-bundlemanager-installforresult-f.md#installforresult) |
| [installMarketApps](arkts-mdm-bundlemanager-installmarketapps-f.md#installmarketapps) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f.md#removeallowedinstallbundles) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f.md#removeallowedinstallbundles-1) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f.md#removeallowedinstallbundles-2) |
| [removeAllowedInstallBundlesSync](arkts-mdm-bundlemanager-removeallowedinstallbundlessync-f.md#removeallowedinstallbundlessync) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f.md#removedisallowedinstallbundles) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f.md#removedisallowedinstallbundles-1) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f.md#removedisallowedinstallbundles-2) |
| [removeDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-removedisallowedinstallbundlessync-f.md#removedisallowedinstallbundlessync) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f.md#removedisalloweduninstallbundles) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f.md#removedisalloweduninstallbundles-1) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f.md#removedisalloweduninstallbundles-2) |
| [removeDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-removedisalloweduninstallbundlessync-f.md#removedisalloweduninstallbundlessync) |
| [removeInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-removeinstallationallowedappdistributiontypes-f.md#removeinstallationallowedappdistributiontypes) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f.md#uninstall) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f.md#uninstall-1) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f.md#uninstall-2) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f.md#uninstall-3) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f.md#uninstall-4) |

### 接口

| 名称 |
| --- |
| [ApplicationInfo](arkts-mdm-bundlemanager-applicationinfo-i.md) |
| [BundleInfo](arkts-mdm-bundlemanager-bundleinfo-i.md) |
| [BundleStorageStats](arkts-mdm-bundlemanager-bundlestoragestats-i.md) |
| [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) |
| [Resource](arkts-mdm-bundlemanager-resource-i.md) |
| [SignatureInfo](arkts-mdm-bundlemanager-signatureinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [AppDistributionType](arkts-mdm-bundlemanager-appdistributiontype-e.md) |
| [BundleInfoGetFlag](arkts-mdm-bundlemanager-bundleinfogetflag-e.md) |
