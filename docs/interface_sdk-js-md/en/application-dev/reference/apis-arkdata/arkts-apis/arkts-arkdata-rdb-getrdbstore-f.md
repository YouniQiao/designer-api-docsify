# getRdbStore

## Modules to Import

```TypeScript
```

## getRdbStore

```TypeScript
function getRdbStore(context: Context, config: StoreConfig, version: number, callback: AsyncCallback<RdbStore>): void
```

Obtains an RDB store. This API uses an asynchronous callback to return the result. You can set parameters for the RDB store based on service requirements and call APIs to perform data operations.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getRdbStore](arkts-arkdata-relationalstore-getrdbstore-f.md)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes | Application context. For details about the application context of the FA model, see Context. For details about the application context of the stage model, see Context. |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes | Configuration of the RDB store. |
| version | number | Yes | RDB store version.Currently, automatic RDB upgrades and downgrades performed based on **version** is not supported. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RdbStore&gt; | Yes | Callback used to return the RDB store obtained. |

**Examples**

FA model:

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';
import relationalStore from '@ohos.data.relationalStore';
import window from '@ohos.window';
import { BusinessError } from '@ohos.base';

const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
data_rdb.getRdbStore(this.context, STORE_CONFIG, 1, (err, rdbStore) => {
  if (err) {
    console.info("Get RdbStore failed, err: " + err)
    return
  }
  console.log("Get RdbStore successfully.")
})
```

Stage model:

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import { BusinessError } from "@ohos.base";
import window from '@ohos.window';

const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage){
    data_rdb.getRdbStore(this.context, STORE_CONFIG, 1, (err: BusinessError, rdbStore: data_rdb.RdbStore) => {
      if (err) {
        console.info("Get RdbStore failed, err: " + err)
        return
      }
      console.log("Get RdbStore successfully.")
    })
  }
}
```


## getRdbStore

```TypeScript
function getRdbStore(context: Context, config: StoreConfig, version: number): Promise<RdbStore>
```

Obtains an RDB store. This API uses a promise to return the result. You can set parameters for the RDB store based on service requirements and call APIs to perform data operations.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes | Application context.For details about the application context of the FA model, see Context. For details about the application context of the stage model, see Context. |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes | Configuration of the RDB store. |
| version | number | Yes | RDB store version.Currently, automatic RDB upgrades and downgrades performed based on **version** is not supported. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;RdbStore & gt; | Promise used to return the **RdbStore** object. |

**Examples**

FA model:

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';

const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
let promise = data_rdb.getRdbStore(this.context, STORE_CONFIG, 1);
promise.then(async (rdbStore) => {
  console.log("Get RdbStore successfully.")
}).catch((err: BusinessError) => {
  console.log("Get RdbStore failed, err: " + err)
})
```

Stage model:

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import { BusinessError } from "@ohos.base";
import window from '@ohos.window';

const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage){
    context = this.context
  }
}

// Call getRdbStore.
let promise = data_rdb.getRdbStore(this.context, STORE_CONFIG, 1);
promise.then(async (rdbStore: data_rdb.RdbStore) => {
  console.log("Get RdbStore successfully.")
}).catch((err: BusinessError) => {
  console.log("Get RdbStore failed, err: " + err)
})
```
