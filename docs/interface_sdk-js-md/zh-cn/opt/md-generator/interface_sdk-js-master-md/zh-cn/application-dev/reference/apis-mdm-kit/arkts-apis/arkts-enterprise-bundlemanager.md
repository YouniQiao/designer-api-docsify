# @ohos.enterprise.bundleManager

本模块提供包管理能力，包括安装和卸载应用包，管理包安装允许名单、包安装禁止名单、包卸载禁止名单、可安装应用的分发类型等。在企业设备管理场景中，通过这些能力可以实现应用安装卸载的精细化管控，防止未授权应用的安装和卸载，保障企业设备安全， 降低安全风险。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 10

**废弃版本：** -1

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedInstallBundlesSync](arkts-mdm-bundlemanager-addallowedinstallbundlessync-f.md#addAllowedInstallBundlesSync) |
| [addDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-adddisallowedinstallbundlessync-f.md#addDisallowedInstallBundlesSync) |
| [addDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-adddisalloweduninstallbundlessync-f.md#addDisallowedUninstallBundlesSync) |
| [addInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-addinstallationallowedappdistributiontypes-f.md#addInstallationAllowedAppDistributionTypes) |
| [getAllowedInstallBundlesSync](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md#getAllowedInstallBundlesSync) |
| [getAllowedInstallBundlesSync](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md#getAllowedInstallBundlesSync) |
| [getDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md#getDisallowedInstallBundlesSync) |
| [getDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md#getDisallowedInstallBundlesSync) |
| [getDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md#getDisallowedUninstallBundlesSync) |
| [getDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md#getDisallowedUninstallBundlesSync) |
| [getInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md#getInstallationAllowedAppDistributionTypes) |
| [getInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md#getInstallationAllowedAppDistributionTypes) |
| [getInstalledBundleList](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md#getInstalledBundleList) |
| [getInstalledBundleList](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md#getInstalledBundleList) |
| [getInstalledBundleStorageStats](arkts-mdm-bundlemanager-getinstalledbundlestoragestats-f.md#getInstalledBundleStorageStats) |
| [install](arkts-mdm-bundlemanager-install-f.md#install) |
| [installForResult](arkts-mdm-bundlemanager-installforresult-f.md#installForResult) |
| [installMarketApps](arkts-mdm-bundlemanager-installmarketapps-f.md#installMarketApps) |
| [removeAllowedInstallBundlesSync](arkts-mdm-bundlemanager-removeallowedinstallbundlessync-f.md#removeAllowedInstallBundlesSync) |
| [removeDisallowedInstallBundlesSync](arkts-mdm-bundlemanager-removedisallowedinstallbundlessync-f.md#removeDisallowedInstallBundlesSync) |
| [removeDisallowedUninstallBundlesSync](arkts-mdm-bundlemanager-removedisalloweduninstallbundlessync-f.md#removeDisallowedUninstallBundlesSync) |
| [removeInstallationAllowedAppDistributionTypes](arkts-mdm-bundlemanager-removeinstallationallowedappdistributiontypes-f.md#removeInstallationAllowedAppDistributionTypes) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f.md#uninstall) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md#addAllowedInstallBundles（系统接口）) |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md#addAllowedInstallBundles（系统接口）) |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md#addAllowedInstallBundles（系统接口）) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md#addDisallowedInstallBundles（系统接口）) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md#addDisallowedInstallBundles（系统接口）) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md#addDisallowedInstallBundles（系统接口）) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md#addDisallowedUninstallBundles（系统接口）) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md#addDisallowedUninstallBundles（系统接口）) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md#addDisallowedUninstallBundles（系统接口）) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md#getAllowedInstallBundles（系统接口）) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md#getAllowedInstallBundles（系统接口）) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md#getAllowedInstallBundles（系统接口）) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md#getDisallowedInstallBundles（系统接口）) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md#getDisallowedInstallBundles（系统接口）) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md#getDisallowedInstallBundles（系统接口）) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md#getDisallowedUninstallBundles（系统接口）) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md#getDisallowedUninstallBundles（系统接口）) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md#getDisallowedUninstallBundles（系统接口）) |
| [install](arkts-mdm-bundlemanager-install-f-sys.md#install（系统接口）) |
| [install](arkts-mdm-bundlemanager-install-f-sys.md#install（系统接口）) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md#removeAllowedInstallBundles（系统接口）) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md#removeAllowedInstallBundles（系统接口）) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md#removeAllowedInstallBundles（系统接口）) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md#removeDisallowedInstallBundles（系统接口）) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md#removeDisallowedInstallBundles（系统接口）) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md#removeDisallowedInstallBundles（系统接口）) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md#removeDisallowedUninstallBundles（系统接口）) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md#removeDisallowedUninstallBundles（系统接口）) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md#removeDisallowedUninstallBundles（系统接口）) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall（系统接口）) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall（系统接口）) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall（系统接口）) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall（系统接口）) |
<!--DelEnd-->

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
