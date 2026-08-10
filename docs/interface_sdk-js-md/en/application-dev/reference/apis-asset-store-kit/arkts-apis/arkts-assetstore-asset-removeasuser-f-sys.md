# removeAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## removeAsUser

```TypeScript
function removeAsUser(userId: number, query: AssetMap): Promise<void>
```

从指定用户空间中删除符合条件的一条或多条关键资产。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function removeAsUser(userId: number, query: AssetMap): Promise<void>--><!--Device-asset-function removeAsUser(userId: number, query: AssetMap): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。取值范围大于等于100。 |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | 待删除关键资产的搜索条件，如别名、访问控制属性、自定义数据等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 24000015 | Getting the system time failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000008 | The database operation failed. |
| 24000006 | Insufficient memory. |
| 201 | The caller doesn't have the permission. |
| 24000007 | The asset is corrupted. |
| 202 | Non-system applications use system APIs. |
| 24000002 | The asset is not found. |
| 24000001 | The ASSET service is unavailable. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let userId: number = 100;
let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
asset.removeAsUser(userId, query).then(() => {
  console.info(`Succeeded in removing Asset from user space.`);
});
```

