# preQueryAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## preQueryAsUser

```TypeScript
function preQueryAsUser(userId: number, query: AssetMap): Promise<Uint8Array>
```

Performs preprocessing for the asset query in the specified user space. This API is used when user authentication is required for the access to an asset. After the user authentication is successful, call [asset.queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md) and [asset.postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md). This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000016](../errorcode-asset.md#24000016-cached-assets-reaches-the-limit) |
| [24000017](../errorcode-asset.md#24000017-function-not-supported) |
