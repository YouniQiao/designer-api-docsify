# getTextEmbeddingModel

## 导入模块

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getTextEmbeddingModel

```TypeScript
function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>
```

获取文本嵌入模型。使用Promise异步回调。

**起始版本：** 15

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ModelConfig](arkts-arkdata-intelligence-modelconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[TextEmbedding](arkts-arkdata-intelligence-textembedding-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |
