# getSupportedCloudModel

## 导入模块

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getSupportedCloudModel

```TypeScript
function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>
```

获取支持的云侧模型信息。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[CloudModelInfo](arkts-arkdata-intelligence-cloudmodelinfo-i.md)&gt;&gt; |
