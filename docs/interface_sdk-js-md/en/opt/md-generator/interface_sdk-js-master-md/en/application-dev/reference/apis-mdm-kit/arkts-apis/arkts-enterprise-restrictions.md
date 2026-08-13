# @ohos.enterprise.restrictions

This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable and re-enable features such as Bluetooth, HDC, USB, Wi-Fi, cellular data, camera, and microphone. **Use cases** - In enterprise device management scenarios, administrators need to restrict functions on employee devices to prevent data leaks or unauthorized use. - In Bring Your Own Device (BYOD) scenarios, the enterprise space needs to restrict device functions to comply with enterprise security policies. - In device security control scenarios, specific functions need to be disabled to protect sensitive enterprise information. **Problems that can be solved** - Prevent employees from transferring sensitive enterprise data via Bluetooth, USB, or other means. - Restrict device debugging capabilities (HDC) to enhance device security. - Control network access (Wi-Fi, cellular data, and so on) to comply with enterprise network policies. - Manage device multimedia capabilities (camera, microphone, and so on) to protect privacy and enterprise confidentiality **Benefits** - Enhance enterprise device security and reduces the risk of data leaks. - Meet compliance requirements and align with security audit standards. - Enable fine-grained device function control, balancing security and user experience. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace restrictions--><!--Device-unnamed-declare namespace restrictions-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedListForAccount](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md#addDisallowedListForAccount) |
| [getDisallowedListForAccount](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md#getDisallowedListForAccount) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getDisallowedPolicyForAccount) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getDisallowedPolicyForAccount) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getUserRestricted) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getUserRestricted) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getUserRestrictedForAccount) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getUserRestrictedForAccount) |
| [removeDisallowedListForAccount](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md#removeDisallowedListForAccount) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setUserRestriction) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setUserRestriction) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setUserRestrictionForAccount) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setUserRestrictionForAccount) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [disableMicrophone](arkts-mdm-restrictions-disablemicrophone-f-sys.md#disableMicrophone-(System-API)) |
| [isFingerprintAuthDisabled](arkts-mdm-restrictions-isfingerprintauthdisabled-f-sys.md#isFingerprintAuthDisabled-(System-API)) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#isHdcDisabled-(System-API)) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#isHdcDisabled-(System-API)) |
| [isMicrophoneDisabled](arkts-mdm-restrictions-ismicrophonedisabled-f-sys.md#isMicrophoneDisabled-(System-API)) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isPrinterDisabled-(System-API)) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isPrinterDisabled-(System-API)) |
| [setFingerprintAuthDisabled](arkts-mdm-restrictions-setfingerprintauthdisabled-f-sys.md#setFingerprintAuthDisabled-(System-API)) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#setHdcDisabled-(System-API)) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#setHdcDisabled-(System-API)) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setPrinterDisabled-(System-API)) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setPrinterDisabled-(System-API)) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) |
