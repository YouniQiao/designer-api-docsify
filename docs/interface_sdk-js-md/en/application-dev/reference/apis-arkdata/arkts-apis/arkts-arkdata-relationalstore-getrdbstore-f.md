# getRdbStore

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## getRdbStore

```TypeScript
function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void
```

创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用callback异步回调。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。

| 当前打开数据库时配置的加密类型 | 本设备上创建该数据库时的加密类型 | 结果 |  
| ------- | -------------------------------- | ---- |  
| 非加密 | 加密 | 使用加密配置（encrypt=true）打开数据库。 |  
| 加密 | 非加密 | 使用非加密配置（encrypt=false）打开数据库。 |

getRdbStore支持多线程并发操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void--><!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用的上下文。 &lt;br&gt;FA模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)。 &lt;br&gt;Stage模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)。 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes | 与此RDB存储相关的数据库配置。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RdbStore&gt; | Yes | 回调函数。当获取RdbStore成功，err为undefined，data为RdbStore对象；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800000 | Inner error. |
| 14801001 | The operation is supported in the stage model only.<br>**Applicable version:** 10 and later |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14801002 | Invalid data group ID.<br>**Applicable version:** 10 and later |
| 14800017 | StoreConfig is changed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800020 | The secret key is corrupted or lost.<br>**Applicable version:** 14 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 12 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 12 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## Examples

FA model:

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;
let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(context, STORE_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
  if (err) {
    console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info('Get RdbStore successfully.');
  store = rdbStore;
  // Perform subsequent operations after the rdbStore instance is successfully obtained.
});
```

Stage model:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };

    relationalStore.getRdbStore(this.context, STORE_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
      if (err) {
        console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      console.info('Get RdbStore successfully.');
      store = rdbStore;
      // Perform subsequent operations after the rdbStore instance is successfully obtained.
    });
  }
}
```


## getRdbStore

```TypeScript
function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>
```

创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用Promise异步回调。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。

| 当前打开数据库时配置的加密类型 | 本设备上创建该数据库时的加密类型 | 结果 |  
| ------- | -------------------------------- | ---- |  
| 非加密 | 加密 | 使用加密配置（encrypt=true）打开数据库。 |  
| 加密 | 非加密 | 使用非加密配置（encrypt=false）打开数据库。 |

getRdbStore支持多线程并发操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>--><!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用的上下文。 &lt;br&gt;FA模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)。 &lt;br&gt;Stage模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)。 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes | 与此RDB存储相关的数据库配置。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RdbStore&gt; | Promise对象。返回RdbStore对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800000 | Inner error. |
| 14801001 | The operation is supported in the stage model only.<br>**Applicable version:** 10 and later |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14801002 | Invalid data group ID.<br>**Applicable version:** 10 and later |
| 14800017 | StoreConfig is changed.<br>**Applicable version:** 12 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800021 | SQLite: Generic error.<br>**Applicable version:** 12 and later |
| 14800020 | The secret key is corrupted or lost.<br>**Applicable version:** 14 and later |
| 14800023 | SQLite: Access permission denied.<br>**Applicable version:** 14 and later |
| 14800022 | SQLite: Callback routine requested an abort.<br>**Applicable version:** 14 and later |
| 14800027 | SQLite: Attempt to write a readonly database.<br>**Applicable version:** 12 and later |
| 14800029 | SQLite: The database is full.<br>**Applicable version:** 12 and later |
| 14800028 | SQLite: Some kind of disk I/O error occurred.<br>**Applicable version:** 12 and later |
| 14800030 | SQLite: Unable to open the database file.<br>**Applicable version:** 12 and later |

## Examples

FA model:

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;
let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
  store = rdbStore;
  console.info('Get RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

Stage model:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };

    relationalStore.getRdbStore(this.context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
  }
}
```

