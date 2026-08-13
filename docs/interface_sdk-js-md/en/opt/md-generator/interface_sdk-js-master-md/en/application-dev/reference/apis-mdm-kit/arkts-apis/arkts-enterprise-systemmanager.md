# @ohos.enterprise.systemManager

This module provides system management capabilities, including NTP time server settings, OTA update policy management, system update management, key event handling policies, log collection, and device activation lock management. It is suitable for enterprise device management scenarios, helping enterprise administrators uniformly manage device system configurations, update policies, and security policies, thereby improving enterprise device management efficiency and security. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace systemManager--><!--Device-unnamed-declare namespace systemManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedNearLinkProtocols](arkts-mdm-systemmanager-adddisallowednearlinkprotocols-f.md#addDisallowedNearLinkProtocols) |
| [addKeyEventPolicies](arkts-mdm-systemmanager-addkeyeventpolicies-f.md#addKeyEventPolicies) |
| [finishLogCollected](arkts-mdm-systemmanager-finishlogcollected-f.md#finishLogCollected) |
| [getAutoUnlockAfterReboot](arkts-mdm-systemmanager-getautounlockafterreboot-f.md#getAutoUnlockAfterReboot) |
| [getAutoUnlockAfterReboot](arkts-mdm-systemmanager-getautounlockafterreboot-f.md#getAutoUnlockAfterReboot) |
| [getDisallowedNearLinkProtocols](arkts-mdm-systemmanager-getdisallowednearlinkprotocols-f.md#getDisallowedNearLinkProtocols) |
| [getInstallLocalEnterpriseAppEnabled](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabled-f.md#getInstallLocalEnterpriseAppEnabled) |
| [getInstallLocalEnterpriseAppEnabledForAccount](arkts-mdm-systemmanager-getinstalllocalenterpriseappenabledforaccount-f.md#getInstallLocalEnterpriseAppEnabledForAccount) |
| [getKeyEventPolicies](arkts-mdm-systemmanager-getkeyeventpolicies-f.md#getKeyEventPolicies) |
| [getKeyEventPolicies](arkts-mdm-systemmanager-getkeyeventpolicies-f.md#getKeyEventPolicies) |
| [getLocalHotaDomain](arkts-mdm-systemmanager-getlocalhotadomain-f.md#getLocalHotaDomain) |
| [getNTPServer](arkts-mdm-systemmanager-getntpserver-f.md#getNTPServer) |
| [getOtaUpdatePolicy](arkts-mdm-systemmanager-getotaupdatepolicy-f.md#getOtaUpdatePolicy) |
| [getUpdateAuthData](arkts-mdm-systemmanager-getupdateauthdata-f.md#getUpdateAuthData) |
| [getUpdateResult](arkts-mdm-systemmanager-getupdateresult-f.md#getUpdateResult) |
| [isActivationLockDisabled](arkts-mdm-systemmanager-isactivationlockdisabled-f.md#isActivationLockDisabled) |
| [isOtaUpdateNonceEnable](arkts-mdm-systemmanager-isotaupdatenonceenable-f.md#isOtaUpdateNonceEnable) |
| [notifyUpdatePackages](arkts-mdm-systemmanager-notifyupdatepackages-f.md#notifyUpdatePackages) |
| [removeDisallowedNearLinkProtocols](arkts-mdm-systemmanager-removedisallowednearlinkprotocols-f.md#removeDisallowedNearLinkProtocols) |
| [removeKeyEventPolicies](arkts-mdm-systemmanager-removekeyeventpolicies-f.md#removeKeyEventPolicies) |
| [setActivationLockDisabled](arkts-mdm-systemmanager-setactivationlockdisabled-f.md#setActivationLockDisabled) |
| [setAutoUnlockAfterReboot](arkts-mdm-systemmanager-setautounlockafterreboot-f.md#setAutoUnlockAfterReboot) |
| [setInstallLocalEnterpriseAppEnabled](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabled-f.md#setInstallLocalEnterpriseAppEnabled) |
| [setInstallLocalEnterpriseAppEnabledForAccount](arkts-mdm-systemmanager-setinstalllocalenterpriseappenabledforaccount-f.md#setInstallLocalEnterpriseAppEnabledForAccount) |
| [setLocalHotaDomain](arkts-mdm-systemmanager-setlocalhotadomain-f.md#setLocalHotaDomain) |
| [setNTPServer](arkts-mdm-systemmanager-setntpserver-f.md#setNTPServer) |
| [setOtaUpdateNonceEnable](arkts-mdm-systemmanager-setotaupdatenonceenable-f.md#setOtaUpdateNonceEnable) |
| [setOtaUpdatePolicy](arkts-mdm-systemmanager-setotaupdatepolicy-f.md#setOtaUpdatePolicy) |
| [startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md#startCollectLog) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ErrorInfo](arkts-mdm-systemmanager-errorinfo-i.md) |
| [KeyEvent](arkts-mdm-systemmanager-keyevent-i.md) |
| [KeyEventPolicy](arkts-mdm-systemmanager-keyeventpolicy-i.md) |
| [KeyItem](arkts-mdm-systemmanager-keyitem-i.md) |
| [NotifyDescription](arkts-mdm-systemmanager-notifydescription-i.md) |
| [OtaUpdatePolicy](arkts-mdm-systemmanager-otaupdatepolicy-i.md) |
| [Package](arkts-mdm-systemmanager-package-i.md) |
| [PackageDescription](arkts-mdm-systemmanager-packagedescription-i.md) |
| [SystemUpdateInfo](arkts-mdm-systemmanager-systemupdateinfo-i.md) |
| [UpdatePackageInfo](arkts-mdm-systemmanager-updatepackageinfo-i.md) |
| [UpdateResult](arkts-mdm-systemmanager-updateresult-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KeyAction](arkts-mdm-systemmanager-keyaction-e.md) |
| [KeyCode](arkts-mdm-systemmanager-keycode-e.md) |
| [KeyPolicy](arkts-mdm-systemmanager-keypolicy-e.md) |
| [NearLinkProtocol](arkts-mdm-systemmanager-nearlinkprotocol-e.md) |
| [PackageType](arkts-mdm-systemmanager-packagetype-e.md) |
| [PolicyType](arkts-mdm-systemmanager-policytype-e.md) |
| [UpdateStatus](arkts-mdm-systemmanager-updatestatus-e.md) |
