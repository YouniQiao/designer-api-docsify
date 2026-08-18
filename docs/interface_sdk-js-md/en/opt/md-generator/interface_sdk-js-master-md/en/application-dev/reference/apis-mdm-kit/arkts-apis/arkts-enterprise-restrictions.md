# @ohos.enterprise.restrictions

This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable and re-enable features such as Bluetooth, HDC, USB, Wi-Fi, cellular data, camera, and microphone. **Use cases** - In enterprise device management scenarios, administrators need to restrict functions on employee devices to prevent data leaks or unauthorized use. - In Bring Your Own Device (BYOD) scenarios, the enterprise space needs to restrict device functions to comply with enterprise security policies. - In device security control scenarios, specific functions need to be disabled to protect sensitive enterprise information. **Problems that can be solved** - Prevent employees from transferring sensitive enterprise data via Bluetooth, USB, or other means. - Restrict device debugging capabilities (HDC) to enhance device security. - Control network access (Wi-Fi, cellular data, and so on) to comply with enterprise network policies. - Manage device multimedia capabilities (camera, microphone, and so on) to protect privacy and enterprise confidentiality **Benefits** - Enhance enterprise device security and reduces the risk of data leaks. - Meet compliance requirements and align with security audit standards. - Enable fine-grained device function control, balancing security and user experience. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

<!--Device-unnamed-declare namespace restrictions--><!--Device-unnamed-declare namespace restrictions-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDisallowedListForAccount](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md#adddisallowedlistforaccount) |
| [getDisallowedListForAccount](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md#getdisallowedlistforaccount) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy) |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getdisallowedpolicy) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getdisallowedpolicyforaccount) |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getdisallowedpolicyforaccount) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getuserrestricted) |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getuserrestricted) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getuserrestrictedforaccount) |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getuserrestrictedforaccount) |
| [removeDisallowedListForAccount](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md#removedisallowedlistforaccount) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setuserrestriction) |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setuserrestriction) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setuserrestrictionforaccount) |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setuserrestrictionforaccount) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [disableMicrophone](arkts-mdm-restrictions-disablemicrophone-f-sys.md#disablemicrophone-system-api) |
| [isFingerprintAuthDisabled](arkts-mdm-restrictions-isfingerprintauthdisabled-f-sys.md#isfingerprintauthdisabled-system-api) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#ishdcdisabled-system-api) |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#ishdcdisabled-system-api) |
| [isMicrophoneDisabled](arkts-mdm-restrictions-ismicrophonedisabled-f-sys.md#ismicrophonedisabled-system-api) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isprinterdisabled-system-api) |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isprinterdisabled-system-api) |
| [setFingerprintAuthDisabled](arkts-mdm-restrictions-setfingerprintauthdisabled-f-sys.md#setfingerprintauthdisabled-system-api) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#sethdcdisabled-system-api) |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#sethdcdisabled-system-api) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setprinterdisabled-system-api) |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setprinterdisabled-system-api) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) |
| [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) |
| [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) |
| [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) |
