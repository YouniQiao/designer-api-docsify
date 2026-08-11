# addAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## addAsUser

```TypeScript
function addAsUser(userId: number, attributes: AssetMap): Promise<void>
```

Adds an asset in the specified user space. This API uses a promise to return the result.

To set {@link Tag.IS_PERSISTENT}, the application must have the ohos.permission.STORE_PERSISTENT_DATA permission.

**Since:** 12

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function addAsUser(userId: number, attributes: AssetMap): Promise<void>--><!--Device-asset-function addAsUser(userId: number, attributes: AssetMap): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| attributes | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000014](../errorcode-asset.md#24000014-file-operation-failed) |
| [24000015](../errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000003](../errorcode-asset.md#24000003-asset-already-exists) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let userId: number = 100;
let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
asset.addAsUser(userId, attr).then(() => {
  console.info(`Succeeded in adding Asset to user space.`);
});
```
