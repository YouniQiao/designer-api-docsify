# getAllowedDistributeAbilityConnBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## getAllowedDistributeAbilityConnBundles

```TypeScript
function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>
```

Obtains the cross-device application trustlist for a specific distributed service under a specified user.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>--><!--Device-applicationManager-function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the. EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies that actually take effect on the device are returned. |
| serviceType | ServiceType | Yes | Distributed service type. |
| accountId | number | Yes | Account ID. The value is an integer greater than or equal to 0. <br> You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) of @ ohos.account.osAccount to obtain the ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Array of [unique identifiers]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

