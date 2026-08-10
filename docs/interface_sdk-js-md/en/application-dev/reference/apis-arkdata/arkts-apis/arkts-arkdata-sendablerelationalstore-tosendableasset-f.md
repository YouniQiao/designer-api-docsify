# toSendableAsset

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## toSendableAsset

```TypeScript
function toSendableAsset(asset: NonSendableAsset): Asset
```

将不可跨线程传递的附件数据，转换为可跨线程传递的附件数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-sendableRelationalStore-function toSendableAsset(asset: NonSendableAsset): Asset--><!--Device-sendableRelationalStore-function toSendableAsset(asset: NonSendableAsset): Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) | Yes | 不可跨线程传递的Asset数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Asset](arkts-arkdata-commontype-asset-i.md) | 可跨线程传递的Asset数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 14800000 | Inner error. |

## Examples

```TypeScript
const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
```

