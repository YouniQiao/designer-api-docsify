# createDataProxyHandle

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## createDataProxyHandle

```TypeScript
function createDataProxyHandle(): Promise<DataProxyHandle>
```

Creates a **DataProxyHandle** instance. This API uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataProxyHandle](arkts-arkdata-datashare-dataproxyhandle-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
