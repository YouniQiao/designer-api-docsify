# getAdmins (System API)

## Modules to Import

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## getAdmins

```TypeScript
function getAdmins(): Promise<Array<Want>>
```

Queries all device administrator applications of the current user. This API uses a promise to return the result.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
