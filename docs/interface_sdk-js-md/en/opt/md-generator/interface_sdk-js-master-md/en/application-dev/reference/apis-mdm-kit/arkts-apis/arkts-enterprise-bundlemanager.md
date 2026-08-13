# @ohos.enterprise.bundleManager

This module provides package management capabilities, including installing and uninstalling application packages, and managing the installation trustlist, installation blocklist, uninstallation blocklist, and distribution types of installable applications. In enterprise device management scenarios, these capabilities enable fine-grained control over application installation and uninstallation, preventing unauthorized installations and uninstallations, thereby safeguarding enterprise device security and reducing security risks. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md#addAllowedInstallBundles-(System-API)) |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md#addAllowedInstallBundles-(System-API)) |
| [addAllowedInstallBundles](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md#addAllowedInstallBundles-(System-API)) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md#addDisallowedInstallBundles-(System-API)) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md#addDisallowedInstallBundles-(System-API)) |
| [addDisallowedInstallBundles](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md#addDisallowedInstallBundles-(System-API)) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md#addDisallowedUninstallBundles-(System-API)) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md#addDisallowedUninstallBundles-(System-API)) |
| [addDisallowedUninstallBundles](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md#addDisallowedUninstallBundles-(System-API)) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md#getAllowedInstallBundles-(System-API)) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md#getAllowedInstallBundles-(System-API)) |
| [getAllowedInstallBundles](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md#getAllowedInstallBundles-(System-API)) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md#getDisallowedInstallBundles-(System-API)) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md#getDisallowedInstallBundles-(System-API)) |
| [getDisallowedInstallBundles](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md#getDisallowedInstallBundles-(System-API)) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md#getDisallowedUninstallBundles-(System-API)) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md#getDisallowedUninstallBundles-(System-API)) |
| [getDisallowedUninstallBundles](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md#getDisallowedUninstallBundles-(System-API)) |
| [install](arkts-mdm-bundlemanager-install-f-sys.md#install-(System-API)) |
| [install](arkts-mdm-bundlemanager-install-f-sys.md#install-(System-API)) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md#removeAllowedInstallBundles-(System-API)) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md#removeAllowedInstallBundles-(System-API)) |
| [removeAllowedInstallBundles](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md#removeAllowedInstallBundles-(System-API)) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md#removeDisallowedInstallBundles-(System-API)) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md#removeDisallowedInstallBundles-(System-API)) |
| [removeDisallowedInstallBundles](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md#removeDisallowedInstallBundles-(System-API)) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md#removeDisallowedUninstallBundles-(System-API)) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md#removeDisallowedUninstallBundles-(System-API)) |
| [removeDisallowedUninstallBundles](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md#removeDisallowedUninstallBundles-(System-API)) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall-(System-API)) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall-(System-API)) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall-(System-API)) |
| [uninstall](arkts-mdm-bundlemanager-uninstall-f-sys.md#uninstall-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationInfo](arkts-mdm-bundlemanager-applicationinfo-i.md) |
| [BundleInfo](arkts-mdm-bundlemanager-bundleinfo-i.md) |
| [BundleStorageStats](arkts-mdm-bundlemanager-bundlestoragestats-i.md) |
| [InstallParam](arkts-mdm-bundlemanager-installparam-i.md) |
| [Resource](arkts-mdm-bundlemanager-resource-i.md) |
| [SignatureInfo](arkts-mdm-bundlemanager-signatureinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppDistributionType](arkts-mdm-bundlemanager-appdistributiontype-e.md) |
| [BundleInfoGetFlag](arkts-mdm-bundlemanager-bundleinfogetflag-e.md) |
