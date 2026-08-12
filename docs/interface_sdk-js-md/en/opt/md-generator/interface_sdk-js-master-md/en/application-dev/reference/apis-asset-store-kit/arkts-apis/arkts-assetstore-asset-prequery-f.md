# preQuery

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## preQuery

```TypeScript
function preQuery(query: AssetMap): Promise<Uint8Array>
```

Performs preprocessing for the asset query. This API is used when user authentication is required for the access to the asset. After the user authentication is successful, call [asset.query](arkts-assetstore-asset-query-f.md#query) and  
[asset.postQuery](arkts-assetstore-asset-postquery-f.md#postQuery). This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function preQuery(query: AssetMap): Promise<Uint8Array>--><!--Device-asset-function preQuery(query: AssetMap): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000007-asset-corrupted) |
| [24000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000002-asset-not-found) |
| [24000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24000016](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000016-cached-assets-reaches-the-limit) |
| [24000017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000017-function-not-supported) |

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
asset.preQuery(query).then((challenge: Uint8Array) => {
  console.info(`Succeeded in pre-querying Asset.`);
});
```
