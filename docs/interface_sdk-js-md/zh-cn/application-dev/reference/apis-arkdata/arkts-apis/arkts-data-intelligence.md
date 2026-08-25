# @ohos.data.intelligence(智慧数据平台)

智慧数据平台（ArkData Intelligence Platform，AIP）提供端侧数据智慧化构建，使应用数据向量化，通过嵌入模型将非结构化的文本、图像等多模态数据，转换成具有语义的向量。适用于智能检索、内容理解、相似度匹配等场 景，帮助开发者解决非结构化数据难以计算和比较的问题，提升应用在推荐系统、智能问答、图像识别等场景下的处理效率和准确性。@namespace intelligence

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

## 导入模块

```TypeScript
import { intelligence } from '@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getImageEmbeddingModel(智慧数据平台)](arkts-arkdata-intelligence-getimageembeddingmodel-f.md) |
| [getSupportedCloudModel(智慧数据平台)](arkts-arkdata-intelligence-getsupportedcloudmodel-f.md) |
| [getTextEmbeddingModel(智慧数据平台)](arkts-arkdata-intelligence-gettextembeddingmodel-f.md) |
| [splitText(智慧数据平台)](arkts-arkdata-intelligence-splittext-f.md) |

### 接口

| 名称 |
| --- |
| [CloudModelInfo(智慧数据平台)](arkts-arkdata-intelligence-cloudmodelinfo-i.md) |
| [ImageEmbedding(智慧数据平台)](arkts-arkdata-intelligence-imageembedding-i.md) |
| [ModelConfig(智慧数据平台)](arkts-arkdata-intelligence-modelconfig-i.md) |
| [SplitConfig(智慧数据平台)](arkts-arkdata-intelligence-splitconfig-i.md) |
| [TextEmbedding(智慧数据平台)](arkts-arkdata-intelligence-textembedding-i.md) |

### 枚举

| 名称 |
| --- |
| [ModelVersion(智慧数据平台)](arkts-arkdata-intelligence-modelversion-e.md) |
| [NetworkPolicy(智慧数据平台)](arkts-arkdata-intelligence-networkpolicy-e.md) |

### 类型

| 名称 |
| --- |
| [Image(智慧数据平台)](arkts-arkdata-intelligence-image-t.md) |
