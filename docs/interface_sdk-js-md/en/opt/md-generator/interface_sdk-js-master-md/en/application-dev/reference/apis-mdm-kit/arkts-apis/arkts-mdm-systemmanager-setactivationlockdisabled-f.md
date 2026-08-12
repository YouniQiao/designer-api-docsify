# setActivationLockDisabled

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## setActivationLockDisabled

```TypeScript
function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise<void>
```

Enables or disables the device activation lock. After the device activation lock is disabled, the Find Device function will no longer be available. This function is only available on certain devices.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise<void>--><!--Device-systemManager-function setActivationLockDisabled(admin: Want, isDisabled: boolean, credential?: string): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| isDisabled | boolean | Yes |
| credential | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [9201012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201012-failed-to-enable-or-disable-activation-lock) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9200016](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200016-service-timeout) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9201011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201011-invalid-activation-lock-credential) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let credential: string = "XXX";
let isDisabled: boolean = true;
systemManager.setActivationLockDisabled(wantTemp, isDisabled, credential).then(() => {
  console.info('Succeeded in setting activation lock status.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set activation lock status. Code: ${err.code}, message: ${err.message}`);
});
```
