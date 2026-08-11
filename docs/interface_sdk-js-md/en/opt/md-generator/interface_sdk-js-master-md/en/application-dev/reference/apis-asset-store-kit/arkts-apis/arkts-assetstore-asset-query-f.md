# query

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## query

```TypeScript
function query(query: AssetMap): Promise<Array<AssetMap>>
```

Queries one or more assets. If user authentication is required for the access to the asset,call [asset.preQuery](arkts-assetstore-asset-prequery-f.md#prequery) before this API and call [asset.postQuery](arkts-assetstore-asset-postquery-f.md#postquery)after this API. For details about the development procedure, see  
[Development Guidance](../../../security/AssetStoreKit/asset-js-query-auth.md).This API uses a promise to return the result.

If no asset is found, an exception indicating that no asset is found is thrown instead of returning an empty query result list.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function query(query: AssetMap): Promise<Array<AssetMap>>--><!--Device-asset-function query(query: AssetMap): Promise<Array<AssetMap>>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [query](#query) | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;AssetMap&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000004](../errorcode-asset.md#24000004-access-denied) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24000017](../errorcode-asset.md#24000017-function-not-supported) |

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
// If only the asset attributes need to be returned, set RETURN_TYPE to ATTRIBUTES. The attributes do not need to be decrypted, so the query takes a short time.
query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // Return all asset information, including the attributes and asset plaintext. The plaintext needs to be decrypted, so the query takes a long time.
asset.query(query).then((res: Array<asset.AssetMap>) => {
  for (let i = 0; i < res.length; i++) {
    // Parse the attributes.
    let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
    console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
  }
  console.info(`Succeeded in querying Asset.`);
});
```
