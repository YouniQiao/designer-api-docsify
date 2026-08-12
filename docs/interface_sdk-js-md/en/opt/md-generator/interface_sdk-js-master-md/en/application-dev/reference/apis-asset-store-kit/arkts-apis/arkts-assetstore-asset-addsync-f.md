# addSync

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## addSync

```TypeScript
function addSync(attributes: AssetMap): void
```

Adds an asset. This API returns the result synchronously.

To set [IS_PERSISTENT](arkts-assetstore-asset-tag-e.md#IS_PERSISTENT), the application must have the ohos.permission.STORE_PERSISTENT_DATA permission.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function addSync(attributes: AssetMap): void--><!--Device-asset-function addSync(attributes: AssetMap): void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| attributes | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24000014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000014-file-operation-failed) |
| [24000015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000006-insufficient-memory) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [24000007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000007-asset-corrupted) |
| [24000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000003-asset-already-exists) |
| [24000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
asset.addSync(attr);
```
