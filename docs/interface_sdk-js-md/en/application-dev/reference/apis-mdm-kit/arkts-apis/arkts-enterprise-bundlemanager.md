# @ohos.enterprise.bundleManager(Bundle Management)

This module provides package management capabilities, including installing and uninstalling application packages, and managing the installation trustlist, installation blocklist, uninstallation blocklist, and distribution types of installable applications. In enterprise device management scenarios, these capabilities enable fine-grained control over application installation and uninstallation, preventing unauthorized installations and uninstallations, thereby safeguarding enterprise device security and reducing security risks.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-addallowedinstallbundlessync-f.md) |
| [addDisallowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-adddisallowedinstallbundlessync-f.md) |
| [addDisallowedUninstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-adddisalloweduninstallbundlessync-f.md) |
| [addInstallationAllowedAppDistributionTypes(Bundle Management)](arkts-mdm-bundlemanager-addinstallationallowedappdistributiontypes-f.md) |
| [getAllowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md) |
| [getAllowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-getallowedinstallbundlessync-f.md) |
| [getDisallowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md) |
| [getDisallowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-getdisallowedinstallbundlessync-f.md) |
| [getDisallowedUninstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md) |
| [getDisallowedUninstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-getdisalloweduninstallbundlessync-f.md) |
| [getInstallationAllowedAppDistributionTypes(Bundle Management)](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md) |
| [getInstallationAllowedAppDistributionTypes(Bundle Management)](arkts-mdm-bundlemanager-getinstallationallowedappdistributiontypes-f.md) |
| [getInstalledBundleList(Bundle Management)](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md) |
| [getInstalledBundleList(Bundle Management)](arkts-mdm-bundlemanager-getinstalledbundlelist-f.md) |
| [getInstalledBundleStorageStats(Bundle Management)](arkts-mdm-bundlemanager-getinstalledbundlestoragestats-f.md) |
| [install(Bundle Management)](arkts-mdm-bundlemanager-install-f.md) |
| [installForResult(Bundle Management)](arkts-mdm-bundlemanager-installforresult-f.md) |
| [installMarketApps(Bundle Management)](arkts-mdm-bundlemanager-installmarketapps-f.md) |
| [removeAllowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-removeallowedinstallbundlessync-f.md) |
| [removeDisallowedInstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-removedisallowedinstallbundlessync-f.md) |
| [removeDisallowedUninstallBundlesSync(Bundle Management)](arkts-mdm-bundlemanager-removedisalloweduninstallbundlessync-f.md) |
| [removeInstallationAllowedAppDistributionTypes(Bundle Management)](arkts-mdm-bundlemanager-removeinstallationallowedappdistributiontypes-f.md) |
| [uninstall(Bundle Management)](arkts-mdm-bundlemanager-uninstall-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md) |
| [addAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md) |
| [addAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-addallowedinstallbundles-f-sys.md) |
| [addDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md) |
| [addDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md) |
| [addDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-adddisallowedinstallbundles-f-sys.md) |
| [addDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md) |
| [addDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md) |
| [addDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-adddisalloweduninstallbundles-f-sys.md) |
| [getAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md) |
| [getAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md) |
| [getAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getallowedinstallbundles-f-sys.md) |
| [getDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md) |
| [getDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md) |
| [getDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getdisallowedinstallbundles-f-sys.md) |
| [getDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md) |
| [getDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md) |
| [getDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-getdisalloweduninstallbundles-f-sys.md) |
| [install(Bundle Management)](arkts-mdm-bundlemanager-install-f-sys.md) |
| [install(Bundle Management)](arkts-mdm-bundlemanager-install-f-sys.md) |
| [removeAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md) |
| [removeAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md) |
| [removeAllowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removeallowedinstallbundles-f-sys.md) |
| [removeDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md) |
| [removeDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md) |
| [removeDisallowedInstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removedisallowedinstallbundles-f-sys.md) |
| [removeDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md) |
| [removeDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md) |
| [removeDisallowedUninstallBundles(Bundle Management)](arkts-mdm-bundlemanager-removedisalloweduninstallbundles-f-sys.md) |
| [uninstall(Bundle Management)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
| [uninstall(Bundle Management)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
| [uninstall(Bundle Management)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
| [uninstall(Bundle Management)](arkts-mdm-bundlemanager-uninstall-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationInfo(Bundle Management)](arkts-mdm-bundlemanager-applicationinfo-i.md) |
| [BundleInfo(Bundle Management)](arkts-mdm-bundlemanager-bundleinfo-i.md) |
| [BundleStorageStats(Bundle Management)](arkts-mdm-bundlemanager-bundlestoragestats-i.md) |
| [InstallParam(Bundle Management)](arkts-mdm-bundlemanager-installparam-i.md) |
| [Resource(Bundle Management)](arkts-mdm-bundlemanager-resource-i.md) |
| [SignatureInfo(Bundle Management)](arkts-mdm-bundlemanager-signatureinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppDistributionType(Bundle Management)](arkts-mdm-bundlemanager-appdistributiontype-e.md) |
| [BundleInfoGetFlag(Bundle Management)](arkts-mdm-bundlemanager-bundleinfogetflag-e.md) |
