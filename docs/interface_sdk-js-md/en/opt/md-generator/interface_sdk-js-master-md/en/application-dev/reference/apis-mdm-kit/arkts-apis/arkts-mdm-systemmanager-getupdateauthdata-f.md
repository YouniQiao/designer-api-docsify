# getUpdateAuthData

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## getUpdateAuthData

```TypeScript
function getUpdateAuthData(admin: Want): Promise<string>
```

Obtains the authentication data for system update verification. This API uses a promise to return the result. This API is applicable to intranet update scenarios. Enterprise administrators can use the authentication data to verify the validity and integrity of the system update package, preventing malicious update packages and improving system security.

**Since:** 19

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getUpdateAuthData(admin: Want): Promise<string>--><!--Device-systemManager-function getUpdateAuthData(admin: Want): Promise<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
systemManager.getUpdateAuthData(wantTemp).then((result: string) => {
  console.info(`Succeeded in getting update auth data: ${JSON.stringify(result)}`);
}).catch((error: BusinessError) => {
  console.error(`Get update auth data failed. Code is ${error.code},message is ${error.message}`);
});
```
