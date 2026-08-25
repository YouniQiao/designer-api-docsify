# createDataProxyHandle

## 导入模块

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## createDataProxyHandle

```TypeScript
function createDataProxyHandle(): Promise<DataProxyHandle>
```

创建DataProxyHandle实例。使用Promise异步回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataProxyHandle](arkts-arkdata-datashare-dataproxyhandle-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |
