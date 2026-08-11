# toSendableValuesBucket

## toSendableValuesBucket

```TypeScript
function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket
```

将不能用于跨线程传递的键值对数据，转换为可用于跨线程传递的键值对数据。

**起始版本：** 12

<!--Device-sendableRelationalStore-function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket--><!--Device-sendableRelationalStore-function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| valuesBucket | [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-参数检查失败) |

## 示例

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
