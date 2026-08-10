# preQuerySync

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## preQuerySync

```TypeScript
function preQuerySync(query: AssetMap): Uint8Array
```

查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[asset.querySync](arkts-assetstore-asset-querysync-f.md#querysync)、  
[asset.postQuerySync](arkts-assetstore-asset-postquerysync-f.md#postquerysync)。使用同步方式返回结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function preQuerySync(query: AssetMap): Uint8Array--><!--Device-asset-function preQuerySync(query: AssetMap): Uint8Array-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | 关键资产的查询条件，如别名、访问控制属性、自定义数据等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 挑战值。 &lt;br&gt;**说明：** 挑战值用于后续用户认证。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
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
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| 24000016 | The cache exceeds the limit. |
| 24000017 | The capability is not supported. |

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
let challenge: Uint8Array = asset.preQuerySync(query);
console.info(`Succeeded in pre-querying with sync, the challenge is: `, challenge);
```

