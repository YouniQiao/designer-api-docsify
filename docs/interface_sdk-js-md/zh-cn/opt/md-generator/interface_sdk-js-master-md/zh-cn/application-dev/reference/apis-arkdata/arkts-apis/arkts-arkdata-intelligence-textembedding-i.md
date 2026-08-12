# TextEmbedding

描述文本嵌入模型的文本嵌入函数。

下列接口都需先使用[intelligence.getTextEmbeddingModel](arkts-arkdata-intelligence-gettextembeddingmodel-f.md#getTextEmbeddingModel)获取到TextEmbedding实例，再通过此实例调用对应接口。

**起始版本：** 15

<!--Device-intelligence-interface TextEmbedding--><!--Device-intelligence-interface TextEmbedding-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

## getEmbedding

```TypeScript
getEmbedding(text: string): Promise<Array<number>>
```

获取给定文本的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](#loadModel)加载嵌入模型，加载成功后调用getEmbedding。

**起始版本：** 15

<!--Device-TextEmbedding-getEmbedding(text: string): Promise<Array<double>>--><!--Device-TextEmbedding-getEmbedding(text: string): Promise<Array<double>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-intelligence.md#31300000-服务内部异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// textEmbedding需先通过intelligence.getTextEmbeddingModel获取
textEmbedding.loadModel()
  .then(() => {
    let text = 'text';
    textEmbedding.getEmbedding(text)
      .then((data: Array<number>) => {
        console.info("Succeeded in getting Embedding");
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to get Embedding. Code: ${err.code}, message: ${err.message}`);
      })
  }).catch((err: BusinessError) => {
    console.error(`Failed to load Model. Code: ${err.code}, message: ${err.message}`);
  })
```

## getEmbedding

```TypeScript
getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>
```

获取给定批次文本的嵌入向量。批量处理可以提高性能，适用于需要同时处理多个文本的场景。使用Promise异步回调。

该接口需先调用[loadModel](#loadModel)加载嵌入模型，加载成功后调用getEmbedding。

**起始版本：** 15

<!--Device-TextEmbedding-getEmbedding(batchTexts: Array<string>): Promise<Array<Array<double>>>--><!--Device-TextEmbedding-getEmbedding(batchTexts: Array<string>): Promise<Array<Array<double>>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| batchTexts | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Array & lt;number & gt; & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-intelligence.md#31300000-服务内部异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// textEmbedding需先通过intelligence.getTextEmbeddingModel获取
textEmbedding.loadModel()
  .then(() => {
    let batchTexts = ['text1', 'text2'];
    textEmbedding.getEmbedding(batchTexts)
      .then((data: Array<Array<number>>) => {
        console.info("Succeeded in getting Embedding");
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to get Embedding. Code: ${err.code}, message: ${err.message}`);
      })
  }).catch((err: BusinessError) => {
    console.error(`Failed to load Model. Code: ${err.code}, message: ${err.message}`);
  })
```

## loadModel

```TypeScript
loadModel(): Promise<void>
```

加载文本嵌入模型。使用Promise异步回调。

**配对调用：**  
- 调用loadModel()后，必须在使用完毕后调用[releaseModel()](#releasemodel)释放模型资源。  
- 未调用releaseModel()会导致资源泄漏，影响系统性能。  
- 建议将releaseModel()放在finally块中确保资源被正确释放。

**起始版本：** 15

<!--Device-TextEmbedding-loadModel(): Promise<void>--><!--Device-TextEmbedding-loadModel(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-intelligence.md#31300000-服务内部异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// textEmbedding需先通过intelligence.getTextEmbeddingModel获取
textEmbedding.loadModel()
  .then(() => {
    console.info("Succeeded in loading Model");
  })
  .catch((err: BusinessError) => {
    console.error(`Failed to load Model. Code: ${err.code}, message: ${err.message}`);
  })
```

## releaseModel

```TypeScript
releaseModel(): Promise<void>
```

释放文本嵌入模型。使用Promise异步回调。

**起始版本：** 15

<!--Device-TextEmbedding-releaseModel(): Promise<void>--><!--Device-TextEmbedding-releaseModel(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkdata/errorcode-intelligence.md#31300000-服务内部异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// textEmbedding需先通过intelligence.getTextEmbeddingModel获取
textEmbedding.releaseModel()
  .then(() => {
    console.info("Succeeded in releasing Model");
  })
  .catch((err: BusinessError) => {
    console.error(`Failed to release Model. Code: ${err.code}, message: ${err.message}`);
  })
```
