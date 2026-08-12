# getAdmins

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## getAdmins

```TypeScript
function getAdmins(): Promise<Array<Want>>
```

Queries all device administrator applications of the current user. This API uses a promise to return the result.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function getAdmins(): Promise<Array<Want>>--><!--Device-adminManager-function getAdmins(): Promise<Array<Want>>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

adminManager.getAdmins().then((result) => {
  console.info(`Succeeded in getting admins :${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get admins. Code: ${err.code}, message: ${err.message}`);
})
```
