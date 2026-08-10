# postQuery

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## postQuery

```TypeScript
function postQuery(handle: AssetMap): Promise<void>
```

查询的后置处理，用于需要用户认证的关键资产（与[asset.preQuery](arkts-assetstore-asset-prequery-f.md#prequery)函数成对出现）。使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function postQuery(handle: AssetMap): Promise<void>--><!--Device-asset-function postQuery(handle: AssetMap): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | 待处理的查询句柄，包含[asset.preQuery](arkts-assetstore-asset-prequery-f.md#prequery)执行成功返回的挑战值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000006 | Insufficient memory. |
| 24000001 | The ASSET service is unavailable. |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';

let handle: asset.AssetMap = new Map();
// The new Uint8Array(32) is only an example. Pass in the challenge value returned by asset.preQuery.
handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
asset.postQuery(handle).then(() => {
  console.info(`Succeeded in post-querying Asset.`);
});
```

