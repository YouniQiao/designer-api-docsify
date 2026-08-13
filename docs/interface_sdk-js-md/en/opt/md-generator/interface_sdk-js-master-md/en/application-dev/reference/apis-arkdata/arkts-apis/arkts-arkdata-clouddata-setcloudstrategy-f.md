# setCloudStrategy

## Modules to Import

```TypeScript
import { cloudData } from '@kit.ArkData';
```

## setCloudStrategy

```TypeScript
function setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>
```

Sets the cloud sync strategy of an application. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-cloudData-function setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>--><!--Device-cloudData-function setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [StrategyType](arkts-arkdata-clouddata-strategytype-e.md) | Yes |
| param | Array & lt;commonType.ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Sync data over Wi-Fi only.
cloudData.setCloudStrategy(cloudData.StrategyType.NETWORK, [cloudData.NetWorkStrategy.WIFI]).then(() => {
  console.info('Succeeded in setting the cloud strategy');
}).catch((err: BusinessError) => {
  console.error(`Failed to set cloud strategy. Code: ${err.code}, message: ${err.message}`);
});
```
