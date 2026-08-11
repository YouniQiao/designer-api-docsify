# setDisallowedPolicyForAccount

## Modules to Import

```TypeScript
import { restrictions } from 'kits/@kit.MDMKit';
```

## setDisallowedPolicyForAccount

```TypeScript
function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void
```

Disallows a feature for a specified user.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** 26.0.0

**Substitutes:** [restrictions.setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void--><!--Device-restrictions-function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | string | Yes | Feature to set. &lt;br&gt;- **fingerprint**: device fingerprint authentication capability. Currently, this feature is supported only on PCs/2-in-1 devices. The rules for using this parameter are as follows: &lt;br&gt;1. If the device fingerprint authentication capability has been disabled through the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) API, calling this API with this parameter passed will throw a policy conflict. &lt;br&gt;2. After the device fingerprint authentication capability is enabled or disabled via this API for a specified user, any subsequent action via the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) API will override the previous setting. If [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) enables the capability, all users gain access to the device fingerprint authentication. &lt;br&gt;- **print**&lt;sup&gt;20+&lt;/sup&gt;: device printing capability, which is supported only on PCs/2-in-1 devices for API versions earlier than 23, and on PCs/2-in-1 devices, smartphones, and tablets for API version 23 and later versions. If the device printing capability is disabled via this API, it remains disabled for specific users even if the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) API is used to enable it for those users. &lt;br&gt;- **mtpClient**&lt;sup&gt;20+&lt;/sup&gt;: Media Transfer Protocol (MTP) client capability (write only). Currently, this feature is supported only on PCs/2-in-1 devices. MTP allows users to linearly access media files on mobile devices. A policy conflict error will occur if this API is used to disable the MTP client capability after MTP client write has been disabled for specific users via the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) API. &lt;br&gt;- **usbStorageDeviceWrite**&lt;sup&gt;20+&lt;/sup&gt;: USB storage device write capability. Currently, this feature is supported only on enterprise PCs/2-in-1 devices. &lt;br&gt; If the USB storage device write permission of a user is disabled via this API in any of the following situations, a policy conflict will be reported: &lt;br&gt; 1. The device USB capability has been disabled via the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) API. &lt;br&gt; 2. USB storage device access policy has been set to read-only or disabled via the [setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md#setusbstoragedeviceaccesspolicy) API. &lt;br&gt; 3. Storage USB devices have been disabled via the [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md#adddisallowedusbdevices) API. &lt;br&gt;- **diskRecoveryKey**&lt;sup&gt;20+&lt;/sup&gt;: recovery [key export](../../../security/UniversalKeystoreKit/huks-export-key-arkts.md) capability. Currently, this feature is supported only on PCs/2-in-1 devices. &lt;br&gt;- **sudo**&lt;sup&gt;20+&lt;/sup&gt;: superuser do (execution with superuser privileges). Currently, this feature is supported only on PCs/2-in-1 devices. If this feature is disabled, neither enterprise spaces nor personal spaces can perform operations with superuser privileges. &lt;br&gt;- **distributedTransmissionOutgoing**&lt;sup&gt;20+&lt;/sup&gt;: distributed one-way data transmission between devices (only data transmission to other devices is supported). A policy conflict occurs if this API is used to disable distributed one-way data transmission between devices after the distributed service has already been disabled via the [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) API. &lt;br&gt;- **openFileBoost**&lt;sup&gt;23+&lt;/sup&gt;: file opening acceleration capability, which provides the file opening acceleration status awareness capability for apps. By integrating the corresponding APIs, apps can detect the acceleration status of files, and further implement features such as displaying unique UI identifiers for accelerated files, thereby optimizing user experience of file opening. Currently, this feature is supported only on PCs/2-in-1 devices. |
| disallow | boolean | Yes | Whether to disallow the feature. The value **true** means to disallow the feature; the value **false** means the opposite. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. &lt;br&gt;**accountId** can be obtained via APIs such as [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) | A conflict policy has been configured. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  restrictions.setDisallowedPolicyForAccount(wantTemp, 'fingerprint', true, 100);
  console.info('Succeeded in setting fingerprint disabled');
} catch (err) {
  console.error(`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}`);
}
```


## setDisallowedPolicyForAccount

```TypeScript
function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void
```

Disallows a feature for a specified user.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void--><!--Device-restrictions-function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| feature | [FeatureForAccount](arkts-mdm-restrictions-featureforaccount-e.md) | Yes | User feature to be disabled or enabled. &lt;br&gt;If SuperHub has been added to the user's list of non-disableable applications through the [addUserNonStopApps](arkts-mdm-applicationmanager-addusernonstopapps-f.md#addusernonstopapps) API, setting this parameter to **SUPER_HUB** will cause a policy conflict and error code 9200010 will be reported. In this case, call the [removeUserNonStopApps](arkts-mdm-applicationmanager-removeusernonstopapps-f.md#removeusernonstopapps) API to remove SuperHub from the user's list of non-disableable applications to resolve the conflict. &lt;br&gt;When **feature** is **DISTRIBUTED_TRANSMISSION**, if the capability of distributed one-way data transmission between devices has been disabled via the [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) API, calling this API to disable the distributed management service will result in a policy conflict and error code 9200010 will be reported. You can call the [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) API to enable distributed one-way data transmission between devices to resolve the conflict. |
| disallow | boolean | Yes | Whether to disallow the feature. The value **true** means to disallow the feature; the value **false** means the opposite. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. &lt;br&gt;**accountId** can be obtained via APIs such as [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid). &lt;br&gt;When **feature** is set to **SUPER_HUB**, this parameter can only be set to the ID of the current user. Otherwise, error code 9200012 will be reported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) | A conflict policy has been configured. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

