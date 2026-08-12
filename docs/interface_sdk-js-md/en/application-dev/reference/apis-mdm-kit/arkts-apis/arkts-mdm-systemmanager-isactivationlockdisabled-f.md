# isActivationLockDisabled

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## isActivationLockDisabled

```TypeScript
function isActivationLockDisabled(admin: Want): Promise<boolean>
```

Checks whether the device activation lock is disabled. This API is applicable to scenarios where you need to verify the device activation lock status. It helps enterprise administrators confirm the device's security configuration,especially when understanding the activation lock state is necessary for device transfer or recycling.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function isActivationLockDisabled(admin: Want): Promise<boolean>--><!--Device-systemManager-function isActivationLockDisabled(admin: Want): Promise<boolean>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return whether the device activation lock is disabled. The value **true** indicates that the device activation lock is disabled and the Find Device function cannot be used. The value **false** indicates that the device activation lock is enabled and the Find Device function is available. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200016](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

