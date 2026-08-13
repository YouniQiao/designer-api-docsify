# getSuperAdmin (System API)

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## getSuperAdmin

```TypeScript
function getSuperAdmin(): Promise<Want>
```

Queries the super device administrator application of this first user (u100). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function getSuperAdmin(): Promise<Want>--><!--Device-adminManager-function getSuperAdmin(): Promise<Want>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { adminManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

adminManager.getSuperAdmin().then((result) => {
  console.info(`Succeeded in getting super admin :${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get super admin. Code: ${err.code}, message: ${err.message}`);
})
```
