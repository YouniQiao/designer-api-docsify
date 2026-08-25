# @ohos.enterprise.systemManager(System Management)

This module provides system management capabilities, including NTP time server settings, OTA update policy management, system update management, key event handling policies, log collection, and device activation lock management. It is suitable for enterprise device management scenarios, helping enterprise administrators uniformly manage device system configurations, update policies, and security policies, thereby improving enterprise device management efficiency and security.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedNearLinkProtocols(System Management)](arkts-mdm-systemmanager-adddisallowednearlinkprotocols-f.md) |
| [addKeyEventPolicies(System Management)](arkts-mdm-systemmanager-addkeyeventpolicies-f.md) |
| [finishLogCollected(System Management)](arkts-mdm-systemmanager-finishlogcollected-f.md) |
| [getAutoUnlockAfterReboot(System Management)](arkts-mdm-systemmanager-getautounlockafterreboot-f.md) |
| [getAutoUnlockAfterReboot(System Management)](arkts-mdm-systemmanager-getautounlockafterreboot-f.md) |
| [getDisallowedNearLinkProtocols(System Management)](arkts-mdm-systemmanager-getdisallowednearlinkprotocols-f.md) |
| [getInstallLocalEnterpriseAppEnabled(System Management)](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabled-f.md) |
| [getInstallLocalEnterpriseAppEnabledForAccount(System Management)](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabledforaccount-f.md) |
| [getKeyEventPolicies(System Management)](arkts-mdm-systemmanager-getkeyeventpolicies-f.md) |
| [getKeyEventPolicies(System Management)](arkts-mdm-systemmanager-getkeyeventpolicies-f.md) |
| [getLocalHotaDomain(System Management)](arkts-mdm-systemmanager-getlocalhotadomain-f.md) |
| [getNTPServer(System Management)](arkts-mdm-systemmanager-getntpserver-f.md) |
| [getOtaUpdatePolicy(System Management)](arkts-mdm-systemmanager-getotaupdatepolicy-f.md) |
| [getUpdateAuthData(System Management)](arkts-mdm-systemmanager-getupdateauthdata-f.md) |
| [getUpdateResult(System Management)](arkts-mdm-systemmanager-getupdateresult-f.md) |
| [isActivationLockDisabled(System Management)](arkts-mdm-systemmanager-isactivationlockdisabled-f.md) |
| [isOtaUpdateNonceEnable(System Management)](arkts-mdm-systemmanager-isotaupdatenonceenable-f.md) |
| [notifyUpdatePackages(System Management)](arkts-mdm-systemmanager-notifyupdatepackages-f.md) |
| [removeDisallowedNearLinkProtocols(System Management)](arkts-mdm-systemmanager-removedisallowednearlinkprotocols-f.md) |
| [removeKeyEventPolicies(System Management)](arkts-mdm-systemmanager-removekeyeventpolicies-f.md) |
| [setActivationLockDisabled(System Management)](arkts-mdm-systemmanager-setactivationlockdisabled-f.md) |
| [setAutoUnlockAfterReboot(System Management)](arkts-mdm-systemmanager-setautounlockafterreboot-f.md) |
| [setInstallLocalEnterpriseAppEnabled(System Management)](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabled-f.md) |
| [setInstallLocalEnterpriseAppEnabledForAccount(System Management)](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabledforaccount-f.md) |
| [setLocalHotaDomain(System Management)](arkts-mdm-systemmanager-setlocalhotadomain-f.md) |
| [setNTPServer(System Management)](arkts-mdm-systemmanager-setntpserver-f.md) |
| [setOtaUpdateNonceEnable(System Management)](arkts-mdm-systemmanager-setotaupdatenonceenable-f.md) |
| [setOtaUpdatePolicy(System Management)](arkts-mdm-systemmanager-setotaupdatepolicy-f.md) |
| [startCollectLog(System Management)](arkts-mdm-systemmanager-startcollectlog-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ErrorInfo(System Management)](arkts-mdm-systemmanager-errorinfo-i.md) |
| [KeyEvent(System Management)](arkts-mdm-systemmanager-keyevent-i.md) |
| [KeyEventPolicy(System Management)](arkts-mdm-systemmanager-keyeventpolicy-i.md) |
| [KeyItem(System Management)](arkts-mdm-systemmanager-keyitem-i.md) |
| [NotifyDescription(System Management)](arkts-mdm-systemmanager-notifydescription-i.md) |
| [OtaUpdatePolicy(System Management)](arkts-mdm-systemmanager-otaupdatepolicy-i.md) |
| [Package(System Management)](arkts-mdm-systemmanager-package-i.md) |
| [PackageDescription(System Management)](arkts-mdm-systemmanager-packagedescription-i.md) |
| [SystemUpdateInfo(System Management)](arkts-mdm-systemmanager-systemupdateinfo-i.md) |
| [UpdatePackageInfo(System Management)](arkts-mdm-systemmanager-updatepackageinfo-i.md) |
| [UpdateResult(System Management)](arkts-mdm-systemmanager-updateresult-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KeyAction(System Management)](arkts-mdm-systemmanager-keyaction-e.md) |
| [KeyCode(System Management)](arkts-mdm-systemmanager-keycode-e.md) |
| [KeyPolicy(System Management)](arkts-mdm-systemmanager-keypolicy-e.md) |
| [NearLinkProtocol(System Management)](arkts-mdm-systemmanager-nearlinkprotocol-e.md) |
| [PackageType(System Management)](arkts-mdm-systemmanager-packagetype-e.md) |
| [PolicyType(System Management)](arkts-mdm-systemmanager-policytype-e.md) |
| [UpdateStatus(System Management)](arkts-mdm-systemmanager-updatestatus-e.md) |
