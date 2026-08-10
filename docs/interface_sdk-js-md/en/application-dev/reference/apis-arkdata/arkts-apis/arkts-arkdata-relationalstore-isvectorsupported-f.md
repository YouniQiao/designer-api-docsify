# isVectorSupported

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## isVectorSupported

```TypeScript
function isVectorSupported(): boolean
```

判断系统是否提供向量数据库能力。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-relationalStore-function isVectorSupported(): boolean--><!--Device-relationalStore-function isVectorSupported(): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 系统具备向量数据库能力时返回true，否则返回false。 |

## Examples

```TypeScript
import { contextConstant, UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { relationalStore } from '@kit.ArkData';

let store: relationalStore.RdbStore | undefined = undefined;
export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let supported = relationalStore.isVectorSupported();
    if (supported) {
      // Vector stores are supported.
      console.info("Vector database supported on current platform.");
      const STORE_CONFIG: relationalStore.StoreConfig = {
        name: "VectorTest.db",
        securityLevel: relationalStore.SecurityLevel.S3,
        vector: true
      };
      try {
        const context = this.context.getApplicationContext().createAreaModeContext(contextConstant.AreaMode.EL3);
        const rdbStore = await relationalStore.getRdbStore(context, STORE_CONFIG);
        console.info('Get RdbStore successfully.');
        store = rdbStore;
        // Perform subsequent operations after the rdbStore instance is successfully obtained.
      } catch (error) {
        const err = error as BusinessError;
        console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
      }
    } else {
      console.info("Vector database not supported on current platform.");
    }
  }
}
```

