# @ohos.data.intelligence

/*
 Copyright (c) 2024 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

<!--Device-unnamed-declare namespace intelligence--><!--Device-unnamed-declare namespace intelligence-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## Modules to Import

```TypeScript
import { intelligence } from '@kit.ArkData';
import { intelligence } from '@kit.ArkData';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getImageEmbeddingModel](arkts-arkdata-intelligence-getimageembeddingmodel-f.md#getimageembeddingmodel) | Obtains an image embedding model. |
| [getSupportedCloudModel](arkts-arkdata-intelligence-getsupportedcloudmodel-f.md#getsupportedcloudmodel) | Obtains the supported cloud embedding models. |
| [getTextEmbeddingModel](arkts-arkdata-intelligence-gettextembeddingmodel-f.md#gettextembeddingmodel) | Obtains a text embedding model. |
| [splitText](arkts-arkdata-intelligence-splittext-f.md#splittext) | Splits text. |

### Interfaces

| Name | Description |
| --- | --- |
| [CloudModelInfo](arkts-arkdata-intelligence-cloudmodelinfo-i.md) | Indicates cloud embedding model information. |
| [ImageEmbedding](arkts-arkdata-intelligence-imageembedding-i.md) | Describes the image embedding functions of the multi-modal embedding model. |
| [ModelConfig](arkts-arkdata-intelligence-modelconfig-i.md) | Manages configurations of the embedding model. |
| [SplitConfig](arkts-arkdata-intelligence-splitconfig-i.md) | Manages text chunk process configurations. |
| [TextEmbedding](arkts-arkdata-intelligence-textembedding-i.md) | Describes the text embedding functions of the multi-modal embedding model. Chinese and English are supported. |

### Enums

| Name | Description |
| --- | --- |
| [ModelVersion](arkts-arkdata-intelligence-modelversion-e.md) | Version of the model. |
| [NetworkPolicy](arkts-arkdata-intelligence-networkpolicy-e.md) | Indicates network policy. |

### Types

| Name | Description |
| --- | --- |
| [Image](arkts-arkdata-intelligence-image-t.md) | The type of the image can be its URI. |

