# getImageEmbeddingModel

## getImageEmbeddingModel

```TypeScript
function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>
```

获取图像嵌入模型。使用Promise异步回调。

**起始版本：** 15

<!--Device-intelligence-function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>--><!--Device-intelligence-function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ModelConfig](arkts-arkdata-intelligence-modelconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;ImageEmbedding&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let imageConfig: intelligence.ModelConfig = {
  version: intelligence.ModelVersion.BASIC_MODEL,
  isNpuAvailable: false,
  cachePath: "/data"
}
let imageEmbedding: intelligence.ImageEmbedding;

intelligence.getImageEmbeddingModel(imageConfig)
  .then((data: intelligence.ImageEmbedding) => {
    console.info("Succeeded in getting ImageModel");
    // 保存图像嵌入模型对象供后续使用
    imageEmbedding = data;
  })
  .catch((err: BusinessError) => {
    console.error(`Failed to get ImageModel. Code: ${err.code}, message: ${err.message}`);
  })
```
