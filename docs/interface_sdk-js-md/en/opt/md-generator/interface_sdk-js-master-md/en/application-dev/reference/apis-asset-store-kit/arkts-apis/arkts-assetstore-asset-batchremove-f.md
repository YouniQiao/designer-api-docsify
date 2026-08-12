# batchRemove

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## batchRemove

```TypeScript
function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>
```

Removes assets in batches based on an alias list.

Only assets with the same [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) can be removed in batches.

**Since:** 26.0.0

<!--Device-asset-function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>--><!--Device-asset-function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetsToBeRemoved | Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000008-database-operation-failed) |
| [24000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000007-asset-corrupted) |
| [24000019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000019-inconsistent-attribute-values) |
| [24000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000001-asset-store-service-unavailable) |
