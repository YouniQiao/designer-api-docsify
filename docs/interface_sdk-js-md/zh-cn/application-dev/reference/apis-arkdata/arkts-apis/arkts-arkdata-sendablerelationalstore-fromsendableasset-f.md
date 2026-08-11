# fromSendableAsset

## fromSendableAsset

```TypeScript
function fromSendableAsset(asset: Asset): NonSendableAsset
```

将可跨线程传递的附件数据，转换为不可跨线程传递的附件数据。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-sendableRelationalStore-function fromSendableAsset(asset: Asset): NonSendableAsset--><!--Device-sendableRelationalStore-function fromSendableAsset(asset: Asset): NonSendableAsset-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asset | [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) | 是 | 可跨线程传递的Asset数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) | 不可跨线程传递的Asset数据。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-参数检查失败) | Inner error. |

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
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
const normalAsset = sendableRelationalStore.fromSendableAsset(sendableAsset);
```

