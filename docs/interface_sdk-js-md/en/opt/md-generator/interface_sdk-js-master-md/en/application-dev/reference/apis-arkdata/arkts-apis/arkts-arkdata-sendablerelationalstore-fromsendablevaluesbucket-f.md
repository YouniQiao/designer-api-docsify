# fromSendableValuesBucket

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## fromSendableValuesBucket

```TypeScript
function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket
```

Converts a KV pair that can be passed across threads into the data that cannot be passed across threads.

**Since:** 12

<!--Device-sendableRelationalStore-function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket--><!--Device-sendableRelationalStore-function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| valuesBucket | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |

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
const asset2: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const u8 = new Uint8Array([1, 2, 3]);

const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket({
  age: 18,
  name: "hangman",
  salary: 100.5,
  passed: true,
  data1: asset1,
  blobType: u8,
  bigValue: BigInt("15822401018187971961171"),
  data2: [asset1, asset2]
});
const nonSendableBucket = sendableRelationalStore.fromSendableValuesBucket(sendableValuesBucket);
```
