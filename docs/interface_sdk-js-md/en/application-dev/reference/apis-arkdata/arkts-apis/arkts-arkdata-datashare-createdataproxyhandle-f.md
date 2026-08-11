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

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataShare-function createDataProxyHandle(): Promise<DataProxyHandle>--><!--Device-dataShare-function createDataProxyHandle(): Promise<DataProxyHandle>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DataProxyHandle&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    dataShare.createDataProxyHandle().then((dataProxyHandle) => {
      console.info("createDataProxyHandle succeed");
    }).catch((err: BusinessError) => {
      console.error(`createDataProxyHandle error: code: ${err.code}, message: ${err.message}`);
    });
  };
};
```

