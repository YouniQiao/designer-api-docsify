# @ohos.enterprise.restrictions

This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable and re-enable features such as Bluetooth, HDC, USB, Wi-Fi, cellular data, camera, and microphone. **Use cases** - In enterprise device management scenarios, administrators need to restrict functions on employee devices to prevent data leaks or unauthorized use. - In Bring Your Own Device (BYOD) scenarios, the enterprise space needs to restrict device functions to comply with enterprise security policies. - In device security control scenarios, specific functions need to be disabled to protect sensitive enterprise information. **Problems that can be solved** - Prevent employees from transferring sensitive enterprise data via Bluetooth, USB, or other means. - Restrict device debugging capabilities (HDC) to enhance device security. - Control network access (Wi-Fi, cellular data, and so on) to comply with enterprise network policies. - Manage device multimedia capabilities (camera, microphone, and so on) to protect privacy and enterprise confidentiality **Benefits** - Enhance enterprise device security and reduces the risk of data leaks. - Meet compliance requirements and align with security audit standards. - Enable fine-grained device function control, balancing security and user experience. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace restrictions--><!--Device-unnamed-declare namespace restrictions-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { restrictions } from 'restrictions';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addDisallowedListForAccount](arkts-mdm-restrictions-adddisallowedlistforaccount-f.md#addDisallowedListForAccount) | Adds a list of applications that are not allowed to use a feature for a specified user. |
| [getDisallowedListForAccount](arkts-mdm-restrictions-getdisallowedlistforaccount-f.md#getDisallowedListForAccount) | Obtains the list of applications that are not allowed to use a feature for a specified user. |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy) | Queries whether a feature is disabled. |
| [getDisallowedPolicy](arkts-mdm-restrictions-getdisallowedpolicy-f.md#getDisallowedPolicy) | Queries whether a specified device feature is disabled. |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getDisallowedPolicyForAccount) | Obtains the status of a feature for a specified user. |
| [getDisallowedPolicyForAccount](arkts-mdm-restrictions-getdisallowedpolicyforaccount-f.md#getDisallowedPolicyForAccount) | Obtains the status of a feature for a specified user. |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getUserRestricted) | Obtains the disabled status of a setting item. |
| [getUserRestricted](arkts-mdm-restrictions-getuserrestricted-f.md#getUserRestricted) | Obtains the disabled status of the specified device setting item. |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getUserRestrictedForAccount) | Obtains the disabled status of a setting item for a specified user. |
| [getUserRestrictedForAccount](arkts-mdm-restrictions-getuserrestrictedforaccount-f.md#getUserRestrictedForAccount) | Obtains the disabled status of a setting item for a specified user. |
| [removeDisallowedListForAccount](arkts-mdm-restrictions-removedisallowedlistforaccount-f.md#removeDisallowedListForAccount) | Removes the list of applications that are not allowed to use a feature for a specified user. |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) | Disallows a feature. > **NOTE：**> > This API applies a device-level restriction policy that affects all users of the device. To set a restriction > policy for a specific user, use the > [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) API. |
| [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) | Enables or disables a specified device feature. Once disabled, the feature cannot be used. |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) | Disallows a feature for a specified user. |
| [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) | Disallows a feature for a specified user. |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setUserRestriction) | Sets restrictions on user behaviors. |
| [setUserRestriction](arkts-mdm-restrictions-setuserrestriction-f.md#setUserRestriction) | Restricts users from modifying specified device setting items. |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setUserRestrictionForAccount) | Sets restrictions on specified user behaviors. |
| [setUserRestrictionForAccount](arkts-mdm-restrictions-setuserrestrictionforaccount-f.md#setUserRestrictionForAccount) | Restricts a specified user from modifying specified setting items. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disableMicrophone](arkts-mdm-restrictions-disablemicrophone-f-sys.md#disableMicrophone) | Enables or disables the microphone. |
| [isFingerprintAuthDisabled](arkts-mdm-restrictions-isfingerprintauthdisabled-f-sys.md#isFingerprintAuthDisabled) | Queries whether fingerprint authentication is disabled. |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#isHdcDisabled) | Queries whether HDC is disabled. This API uses an asynchronous callback to return the result. |
| [isHdcDisabled](arkts-mdm-restrictions-ishdcdisabled-f-sys.md#isHdcDisabled-(System-API)) | Queries whether HDC is disabled. This API uses a promise to return the result. |
| [isMicrophoneDisabled](arkts-mdm-restrictions-ismicrophonedisabled-f-sys.md#isMicrophoneDisabled) | Queries whether the microphone is disabled. |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isPrinterDisabled) | Queries whether the printing capability of a device is disabled. This API uses an asynchronous callback to return the result. |
| [isPrinterDisabled](arkts-mdm-restrictions-isprinterdisabled-f-sys.md#isPrinterDisabled-(System-API)) | Queries whether the printing capability of a device is disabled. This API uses a promise to return the result. |
| [setFingerprintAuthDisabled](arkts-mdm-restrictions-setfingerprintauthdisabled-f-sys.md#setFingerprintAuthDisabled) | Enables or disables fingerprint authentication. |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#setHdcDisabled) | Enables or disables [HDC](../../../../device-dev/subsystems/subsys-toolchain-hdc-guide.md). This API uses an asynchronous callback to return the result. |
| [setHdcDisabled](arkts-mdm-restrictions-sethdcdisabled-f-sys.md#setHdcDisabled-(System-API)) | Enables or disables HDC on a device. This API uses a promise to return the result. |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setPrinterDisabled) | Enables or disables the printing capability of the device. This API uses an asynchronous callback to return the result. |
| [setPrinterDisabled](arkts-mdm-restrictions-setprinterdisabled-f-sys.md#setPrinterDisabled-(System-API)) | Enables or disables the printing capability of the device. This API uses a promise to return the result. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) | Enumerates the features that can be disabled or enabled for a specified user. |
| [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) | Enumerates device features. |
| [SettingsForAccount](arkts-mdm-restrictions-settingsforaccount-e.md) | Enumerates user setting items. |
| [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) | Enumerates device setting items. |

