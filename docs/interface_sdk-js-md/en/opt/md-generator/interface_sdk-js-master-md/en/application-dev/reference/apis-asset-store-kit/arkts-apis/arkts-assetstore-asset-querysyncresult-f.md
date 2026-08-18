# querySyncResult

## Modules to Import

```TypeScript
```

## querySyncResult

```TypeScript
function querySyncResult(query: AssetMap): Promise<SyncResult>
```

Queries the result of the sync operation. This API uses a promise to return the result.

**Since:** 20

<!--Device-asset-function querySyncResult(query: AssetMap): Promise<SyncResult>--><!--Device-asset-function querySyncResult(query: AssetMap): Promise<SyncResult>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SyncResult & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000014](../errorcode-asset.md#24000014-file-operation-failed) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000018](../errorcode-asset.md#24000018-parameter-check-failed) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |

**Examples**

```TypeScript
import { asset } from '@kit.AssetStoreKit';

let query: asset.AssetMap = new Map();
asset.querySyncResult(query).then((res: asset.SyncResult) => {
  console.info(`Succeeded in querying sync result: ${JSON.stringify(res)}`);
});
```
