# addAllowedNotificationBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addAllowedNotificationBundles

```TypeScript
function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void
```

Adds applications to the notification trustlist. After the notification trustlist is set, applications not in the trustlist cannot send notifications. &gt; **NOTE：**&gt; &gt; 1. If both the Kiosk mode and the notification trustlist policy are set, applications in the Kiosk mode and those &gt; in the notification trustlist can send notifications. &gt; 2. If the device notification capability has been disabled via &gt; [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md), calling this API to &gt; set the notification trustlist will trigger error code 9200010. &gt; 3. The notification trustlist does not apply to system services, which can always send notifications. System &gt; applications are controlled by the notification trustlist. &gt; 4. Cross-user settings are supported. The settings take effect immediately.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void--><!--Device-applicationManager-function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleNames | Array&lt;string&gt; | Yes | Application bundle name array, which specifies the applications that are allowed to send notifications. A maximum of 200 applications are supported. |
| accountId | number | Yes | Account ID, which must be greater than or equal to 0. <br>You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) of @ ohos.account.osAccount to obtain the ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) | A conflict policy has been configured. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

