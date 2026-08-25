# batchAdd

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## batchAdd

```TypeScript
function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>
```

Adds assets in batches based on an attributes array. To set [IS_PERSISTENT](arkts-assetstore-asset-tag-e.md#is_persistent), the application must have the ohos.permission.STORE_PERSISTENT_DATA permission.Only assets with the same [GROUP_ID](arkts-assetstore-asset-tag-e.md#group_id) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#require_attr_encrypted) can be added in batches.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| attributesArray | Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[BatchResult](arkts-assetstore-asset-batchresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000014](../errorcode-asset.md#24000014-file-operation-failed) |
| [24000015](../errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000019](../errorcode-asset.md#24000019-inconsistent-attribute-values) |
