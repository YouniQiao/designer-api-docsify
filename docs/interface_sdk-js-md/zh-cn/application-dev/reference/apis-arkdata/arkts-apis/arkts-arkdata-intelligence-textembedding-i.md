# TextEmbedding

描述文本嵌入模型的文本嵌入函数。下列接口都需先使用[intelligence.getTextEmbeddingModel](arkts-arkdata-intelligence-gettextembeddingmodel-f.md)获取到TextEmbedding实例，再通过此实例调用对 应接口。@interface TextEmbedding

**起始版本：** 15

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

## 导入模块

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getEmbedding

```TypeScript
getEmbedding(text: string): Promise<Array<number>>
```

获取给定文本的嵌入向量。使用Promise异步回调。该接口需先调用[loadModel](#loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**起始版本：** 15

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |

## getEmbedding

```TypeScript
getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>
```

获取给定批次文本的嵌入向量。批量处理可以提高性能，适用于需要同时处理多个文本的场景。使用Promise异步回调。该接口需先调用[loadModel](#loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**起始版本：** 15

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |

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

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |

## releaseModel

```TypeScript
releaseModel(): Promise<void>
```

释放文本嵌入模型。使用Promise异步回调。

**起始版本：** 15

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |
