# ImageEmbedding

描述多模态嵌入模型的图像嵌入函数。下列接口都需先使用[intelligence.getImageEmbeddingModel](arkts-arkdata-intelligence-getimageembeddingmodel-f.md)获取到ImageEmbedding实例，再通过此实例 调用对应接口。@interface ImageEmbedding

**起始版本：** 15

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

## 导入模块

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getEmbedding

```TypeScript
getEmbedding(image: Image): Promise<Array<number>>
```

获取给定图像的嵌入向量。使用Promise异步回调。该接口需先调用[loadModel](arkts-arkdata-intelligence-textembedding-i.md#loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**起始版本：** 15

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| image | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | 是 |

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

## loadModel

```TypeScript
loadModel(): Promise<void>
```

加载图像嵌入模型。使用Promise异步回调。  
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

释放图像嵌入模型。使用Promise异步回调。

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
