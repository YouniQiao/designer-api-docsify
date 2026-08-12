# @ohos.enterprise.bundleManager(Bundle Management)

This module provides package management capabilities, including installing and uninstalling application packages, and managing the installation trustlist, installation blocklist, uninstallation blocklist, and distribution types of installable applications. In enterprise device management scenarios, these capabilities enable fine-grained control over application installation and uninstallation, preventing unauthorized installations and uninstallations, thereby safeguarding enterprise device security and reducing security risks.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
