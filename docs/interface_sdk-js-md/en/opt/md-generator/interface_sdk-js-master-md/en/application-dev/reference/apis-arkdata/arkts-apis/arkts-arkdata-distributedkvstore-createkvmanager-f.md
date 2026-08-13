# createKVManager

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig): KVManager
```

Creates a **KVManager** instance for KV store management.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedKVStore-function createKVManager(config: KVManagerConfig): KVManager--><!--Device-distributedKVStore-function createKVManager(config: KVManagerConfig): KVManager-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KVManager](arkts-arkdata-distributeddata-kvmanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

Stage model:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let kvManager: distributedKVStore.KVManager;
let appId: string = 'com.example.datamanagertest';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbilityStage onCreate');
    let context = this.context;
    const kvManagerConfig: distributedKVStore.KVManagerConfig = {
      context: context,
      bundleName: appId
    }
    try {
      kvManager = distributedKVStore.createKVManager(kvManagerConfig);
      console.info('Succeeded in creating KVManager');
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to create KVManager. Code: ${error.code}, message: ${error.message}`);
    }
    if (kvManager !== undefined) {
      // Perform subsequent operations such as creating a KV store.
      // ...
    }
  }
}
```

FA model:

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let kvManager: distributedKVStore.KVManager;
let appId: string = 'com.example.datamanagertest';
let context = featureAbility.getContext();
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
  context: context,
  bundleName: appId
}
try {
  kvManager = distributedKVStore.createKVManager(kvManagerConfig);
  console.info('Succeeded in creating KVManager');
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to create KVManager. Code: ${error.code}, message: ${error.message}`);
}
if (kvManager !== undefined) {
  kvManager = kvManager as distributedKVStore.KVManager;
  // Perform subsequent operations such as creating a KV store.
  // ...
}
```
