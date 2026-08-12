# @ohos.enterprise.restrictions(Restrictions)

This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable and re-enable features such as Bluetooth, HDC, USB, Wi-Fi, cellular data, camera, and microphone.

**Use cases**

- In enterprise device management scenarios, administrators need to restrict functions on employee devices to prevent  
data leaks or unauthorized use.  
- In Bring Your Own Device (BYOD) scenarios, the enterprise space needs to restrict device functions to comply with  
enterprise security policies.  
- In device security control scenarios, specific functions need to be disabled to protect sensitive enterprise  
information.

**Problems that can be solved**

- Prevent employees from transferring sensitive enterprise data via Bluetooth, USB, or other means.  
- Restrict device debugging capabilities (HDC) to enhance device security.  
- Control network access (Wi-Fi, cellular data, and so on) to comply with enterprise network policies.  
- Manage device multimedia capabilities (camera, microphone, and so on) to protect privacy and enterprise  
confidentiality

**Benefits**

- Enhance enterprise device security and reduces the risk of data leaks.  
- Meet compliance requirements and align with security audit standards.  
- Enable fine-grained device function control, balancing security and user experience.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

<!--Device-unnamed-declare namespace restrictions--><!--Device-unnamed-declare namespace restrictions-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedListForAccount](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md#adddisallowedlistforaccount) |
| [disableMicrophone](arkts-mdm-restrictions-disablemicrophone-f.md#disablemicrophone) |
| [getDisallowedListForAccount](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md#getdisallowedlistforaccount) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy-1) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getdisallowedpolicyforaccount) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getdisallowedpolicyforaccount-1) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getuserrestricted) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getuserrestricted-1) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getuserrestrictedforaccount) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getuserrestrictedforaccount-1) |
| [isFingerprintAuthDisabled](arkts-mdm-restrictions-isfingerprintauthdisabled-f.md#isfingerprintauthdisabled) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f.md#ishdcdisabled) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f.md#ishdcdisabled-1) |
| [isMicrophoneDisabled](arkts-mdm-restrictions-ismicrophonedisabled-f.md#ismicrophonedisabled) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f.md#isprinterdisabled) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f.md#isprinterdisabled-1) |
| [removeDisallowedListForAccount](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md#removedisallowedlistforaccount) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy-1) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount-1) |
| [setFingerprintAuthDisabled](arkts-mdm-restrictions-setfingerprintauthdisabled-f.md#setfingerprintauthdisabled) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f.md#sethdcdisabled) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f.md#sethdcdisabled-1) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f.md#setprinterdisabled) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f.md#setprinterdisabled-1) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setuserrestriction) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setuserrestriction-1) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setuserrestrictionforaccount) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setuserrestrictionforaccount-1) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) |
