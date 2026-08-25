# @ohos.enterprise.restrictions(Restrictions)

This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable and re-enable features such as Bluetooth, HDC, USB, Wi-Fi, cellular data, camera, and microphone.  
**Use cases**  
- In enterprise device management scenarios, administrators need to restrict functions on employee devices to prevent data leaks or unauthorized use. - In Bring Your Own Device (BYOD) scenarios, the enterprise space needs to restrict device functions to comply with enterprise security policies. - In device security control scenarios, specific functions need to be disabled to protect sensitive enterprise information.  
**Problems that can be solved**  
- Prevent employees from transferring sensitive enterprise data via Bluetooth, USB, or other means. - Restrict device debugging capabilities (HDC) to enhance device security. - Control network access (Wi-Fi, cellular data, and so on) to comply with enterprise network policies. - Manage device multimedia capabilities (camera, microphone, and so on) to protect privacy and enterprise confidentiality  
**Benefits**  
- Enhance enterprise device security and reduces the risk of data leaks. - Meet compliance requirements and align with security audit standards. - Enable fine-grained device function control, balancing security and user experience.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedListForAccount(Restrictions)](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md) |
| [getDisallowedListForAccount(Restrictions)](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md) |
| [getDisallowedPolicy(Restrictions)](arkts-mdm-restrictions-getdisallowedpolicy-f.md) |
| [getDisallowedPolicy(Restrictions)](arkts-mdm-restrictions-getdisallowedpolicy-f.md) |
| [getDisallowedPolicyForAccount(Restrictions)](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md) |
| [getDisallowedPolicyForAccount(Restrictions)](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md) |
| [getUserRestricted(Restrictions)](arkts-mdm-restrictions-getuserrestricted-f.md) |
| [getUserRestricted(Restrictions)](arkts-mdm-restrictions-getuserrestricted-f.md) |
| [getUserRestrictedForAccount(Restrictions)](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md) |
| [getUserRestrictedForAccount(Restrictions)](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md) |
| [removeDisallowedListForAccount(Restrictions)](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md) |
| [setDisallowedPolicy(Restrictions)](arkts-mdm-restrictions-setdisallowedpolicy-f.md) |
| [setDisallowedPolicy(Restrictions)](arkts-mdm-restrictions-setdisallowedpolicy-f.md) |
| [setDisallowedPolicyForAccount(Restrictions)](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md) |
| [setDisallowedPolicyForAccount(Restrictions)](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md) |
| [setUserRestriction(Restrictions)](arkts-mdm-restrictions-setuserrestriction-f.md) |
| [setUserRestriction(Restrictions)](arkts-mdm-restrictions-setuserrestriction-f.md) |
| [setUserRestrictionForAccount(Restrictions)](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md) |
| [setUserRestrictionForAccount(Restrictions)](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [disableMicrophone(Restrictions)](arkts-mdm-restrictions-disablemicrophone-f-sys.md) |
| [isFingerprintAuthDisabled(Restrictions)](arkts-mdm-restrictions-isfingerprintauthdisabled-f-sys.md) |
| [isHdcDisabled(Restrictions)](arkts-mdm-restrictions-ishdcdisabled-f-sys.md) |
| [isHdcDisabled(Restrictions)](arkts-mdm-restrictions-ishdcdisabled-f-sys.md) |
| [isMicrophoneDisabled(Restrictions)](arkts-mdm-restrictions-ismicrophonedisabled-f-sys.md) |
| [isPrinterDisabled(Restrictions)](arkts-mdm-restrictions-isprinterdisabled-f-sys.md) |
| [isPrinterDisabled(Restrictions)](arkts-mdm-restrictions-isprinterdisabled-f-sys.md) |
| [setFingerprintAuthDisabled(Restrictions)](arkts-mdm-restrictions-setfingerprintauthdisabled-f-sys.md) |
| [setHdcDisabled(Restrictions)](arkts-mdm-restrictions-sethdcdisabled-f-sys.md) |
| [setHdcDisabled(Restrictions)](arkts-mdm-restrictions-sethdcdisabled-f-sys.md) |
| [setPrinterDisabled(Restrictions)](arkts-mdm-restrictions-setprinterdisabled-f-sys.md) |
| [setPrinterDisabled(Restrictions)](arkts-mdm-restrictions-setprinterdisabled-f-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FeatureForAccount(Restrictions)](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice(Restrictions)](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount(Restrictions)](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice(Restrictions)](arkts-mdm-restrictions-settingsfordevice-e.md) |
