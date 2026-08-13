# insertData

## insertData

```TypeScript
function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void
```

将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用callback异步回调。 **实现机制：** 系统接收UnifiedData对象后，验证数据完整性并序列化存储。根据intention值路由到对应存储空间，生成唯一标识符key。数据在公共数据通路中由系统管理有效期，默认策略为应用退出后自动清理。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unifiedDataChannel-function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void--><!--Device-unifiedDataChannel-function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let plainText: uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent: 'This is a plain text example',
  abstract: 'This is abstract'
};
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
};
try {
  unifiedDataChannel.insertData(options, unifiedData, (err, key) => {
    if (err === undefined) {
      console.info(`Succeeded in inserting data. key = ${key}`);
    } else {
      console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
    }
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message}`);
}
```


## insertData

```TypeScript
function insertData(options: Options, data: UnifiedData): Promise<string>
```

将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unifiedDataChannel-function insertData(options: Options, data: UnifiedData): Promise<string>--><!--Device-unifiedDataChannel-function insertData(options: Options, data: UnifiedData): Promise<string>-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 是 |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let plainText: uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent: 'This is a plain text example',
  abstract: 'This is abstract'
};
let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let unifiedData = new unifiedDataChannel.UnifiedData(text);

let options: unifiedDataChannel.Options = {
  intention: unifiedDataChannel.Intention.DATA_HUB
};
try {
  unifiedDataChannel.insertData(options, unifiedData).then((key) => {
    console.info(`Succeeded in inserting data. key = ${key}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to insert data. code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message}`);
}
```
