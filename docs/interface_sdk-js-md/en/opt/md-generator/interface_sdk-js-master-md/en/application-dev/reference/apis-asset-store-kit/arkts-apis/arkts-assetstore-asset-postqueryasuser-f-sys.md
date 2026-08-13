# postQueryAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## postQueryAsUser

```TypeScript
function postQueryAsUser(userId:number, handle: AssetMap): Promise<void>
```

Performs postprocessing for the asset query in the specified user space. This API is used when user authentication is required for the access to an asset. This API must be used with [asset.preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#preQueryAsUser-(System-API)) together. This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function postQueryAsUser(userId:number, handle: AssetMap): Promise<void>--><!--Device-asset-function postQueryAsUser(userId:number, handle: AssetMap): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| handle | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';

let userId: number = 100;
let handle: asset.AssetMap = new Map();
// The new Uint8Array(32) is only an example. Pass in the challenge value returned by asset.preQueryAsUser.
handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
asset.postQueryAsUser(userId, handle).then(() => {
  console.info(`Succeeded in post-querying Asset from user space.`);
});
```
