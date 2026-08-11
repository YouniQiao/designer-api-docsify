# getInstallLocalEnterpriseAppEnabledForAccount

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getInstallLocalEnterpriseAppEnabledForAccount

```TypeScript
function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want | null, accountId: number): boolean
```

Checks whether local installation of enterprise applications is supported for a specified user. This API is applicable to scenarios where there is a need to verify whether local installation of enterprise applications is enabled for a specific user, helping enterprise administrators confirm the policy configuration status and ensure that users can normally install enterprise applications.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want | null, accountId: number): boolean--><!--Device-systemManager-function getInstallLocalEnterpriseAppEnabledForAccount(admin: Want | null, accountId: number): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. &lt;br&gt;If the device has multiple MDM applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies that actually take effect on the device are returned. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. &lt;br&gt;**accountId** can be obtained via APIs such as [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid). |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether local installation of enterprise applications is supported. The value **true** indicates that local installation is supported, and the value **false** indicates the opposite. When **admin** is set to **null**, this API checks whether local installation of enterprise applications is supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

