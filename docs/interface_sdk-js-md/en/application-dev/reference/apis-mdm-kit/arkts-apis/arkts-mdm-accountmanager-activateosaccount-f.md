# activateOsAccount

## Modules to Import

```TypeScript
import { accountManager } from '@kit.MDMKit';
```

## activateOsAccount

```TypeScript
function activateOsAccount(admin: Want, accountId: number): Promise<void>
```

Switches the system account. Currently, this API is supported only on phones and tablets, and can only switch between normal system accounts created via [createNormalOsAccount](arkts-mdm-accountmanager-createnormalosaccount-f.md#createnormalosaccount) and the default system account (ID: 100).

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function activateOsAccount(admin: Want, accountId: number): Promise<void>--><!--Device-accountManager-function activateOsAccount(admin: Want, accountId: number): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| accountId | number | Yes | System account ID. If you switch to a system account that does not exist, error code 9200012 is reported. If you switch to a restricted system account, for example, a system account created via [addOsAccountAsync](arkts-mdm-accountmanager-addosaccountasync-f.md#addosaccountasync), error code 9201041 is reported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. If the operation fails., an error object is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9201046](../errorcode-enterpriseDeviceManager.md#9201046-signedin-system-account-count-reached-the-upper-limit) | The number of signed-in accounts reaches the upper limit. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9201041](../errorcode-enterpriseDeviceManager.md#9201041-system-account-type-restricted) | Restricted account. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

