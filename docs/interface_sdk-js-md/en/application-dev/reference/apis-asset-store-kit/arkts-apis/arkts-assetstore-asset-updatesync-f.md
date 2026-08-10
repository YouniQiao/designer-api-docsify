# updateSync

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## updateSync

```TypeScript
function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void
```

更新符合条件的一条关键资产，使用同步方式返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void--><!--Device-asset-function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | 待更新关键资产的搜索条件，如关键资产别名、访问控制属性、自定义数据等。 |
| attributesToUpdate | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | 待更新关键资产的属性集合，如关键资产明文、自定义数据等。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 24000015 | Getting the system time failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000005 | The screen lock status does not match. |
| 24000002 | The asset is not found. |
| 24000001 | The ASSET service is unavailable. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
asset.updateSync(query, attrsToUpdate);
```

