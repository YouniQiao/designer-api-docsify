# isOtaUpdateNonceEnable

## Modules to Import

```TypeScript
import { systemManager } from 'systemManager';
```

## isOtaUpdateNonceEnable

```TypeScript
function isOtaUpdateNonceEnable(admin: Want): boolean
```

Checks whether nonce is enabled for OTA update. This API is applicable to scenarios where you need to verify the OTA update security configuration on the device. It helps enterprise administrators confirm the status of the nonce verification feature to ensure system update security.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function isOtaUpdateNonceEnable(admin: Want): boolean--><!--Device-systemManager-function isOtaUpdateNonceEnable(admin: Want): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** means that the nonce for OTA update is enabled, and the value **false** means that the nonce for OTA update is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

