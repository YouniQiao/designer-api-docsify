# toSendableValuesBucket

## Modules to Import

```TypeScript
import { sendableRelationalStore } from '@kit.ArkData';
```

## toSendableValuesBucket

```TypeScript
function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket
```

Converts a key-value (KV) pair that cannot be passed across threads into the data that can be passed across threads.

**Since:** 12

**Deprecated since:** -1

<!--Device-sendableRelationalStore-function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket--><!--Device-sendableRelationalStore-function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [valuesBucket](../../apis-ability-kit/arkts-apis/arkts-ability-dataabilityoperation-dataabilityoperation-i.md) | [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |

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
const valuesBucket: sendableRelationalStore.NonSendableBucket = {
  age: 18,
  name: "hangman",
  salary: 100.5,
  passed: true,
  data1: asset1,
  blobType: u8,
  bigValue: BigInt("15822401018187971961171"),
  data2: [asset1, asset2]
};

const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);
```
