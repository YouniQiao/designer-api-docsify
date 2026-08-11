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

<!--Device-dataShare-function createDataProxyHandle(): Promise<DataProxyHandle>--><!--Device-dataShare-function createDataProxyHandle(): Promise<DataProxyHandle>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;DataProxyHandle&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    dataShare.createDataProxyHandle().then((dataProxyHandle) => {
      console.info("createDataProxyHandle succeed");
    }).catch((err: BusinessError) => {
      console.error(`Failed to create DataProxyHandle. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
