# getRdbStore

## Modules to Import

```TypeScript
import { relationalStore } from '@kit.ArkData';
```

## getRdbStore

```TypeScript
function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void
```

Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform data operations. This API uses an asynchronous callback to return the result.

If no database file exists in the corresponding sandbox directory, a database file is created. For details, see   
[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig). If a database file exists in the corresponding directory, the existing database file is opened.

When creating a database, you should consider whether to configure the   
[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig) parameter. Once the database is created, you are not allowed to change this parameter.

| Encryption Type When the RDB Store Is Opened | Encryption Type When the RDB Store Is Created | [Result](arkts-arkdata-relationalstore-result-i.md) |
| ------- | -------------------------------- | ---- |
| Non-encryption| Encryption | The RDB store is opened in encrypted mode. |
| Encryption| Non-encryption |

Currently, **getRdbStore()** does not support multi-thread concurrent operations.

**Since:** 9

<!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void--><!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RdbStore&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-internal-error) |
| [14801001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14801001-stage-model-required) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800010-invalid-database-path) |
| [14801002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14801002-invalid-datagroupid-in-storeconfig) |
| [14800017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800017-key-configuration-changed) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800020](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800020-key-damaged-or-lost) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800030](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

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

Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform data operations. This API uses a promise to return the result.

If no database file exists in the corresponding sandbox directory, a database file is created. For details, see   
[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig). If a database file exists in the corresponding directory, the existing database file is opened.

When creating a database, you should consider whether to configure the   
[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md#StoreConfig) parameter. Once the database is created, you are not allowed to change this parameter.

| Encryption Type When the RDB Store Is Opened | Encryption Type When the RDB Store Is Created | [Result](arkts-arkdata-relationalstore-result-i.md) |
| ------- | -------------------------------- | ---- |
| Non-encryption| Encryption | The RDB store is opened in encrypted mode. |
| Encryption| Non-encryption |

Currently, **getRdbStore()** does not support multi-thread concurrent operations.

**Since:** 9

<!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>--><!--Device-relationalStore-function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;RdbStore & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800000-internal-error) |
| [14801001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14801001-stage-model-required) |
| [14800011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800011-database-file-corrupted) |
| [14800010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800010-invalid-database-path) |
| [14801002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14801002-invalid-datagroupid-in-storeconfig) |
| [14800017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800017-key-configuration-changed) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800021-sqlite-generic-error) |
| [14800020](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800020-key-damaged-or-lost) |
| [14800023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800023-sqlite-access-denied) |
| [14800022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800022-sqlite-asynchronous-callback-request-aborted) |
| [14800027](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800027-sqlite-attempt-to-write-a-readonly-database) |
| [14800029](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800029-sqlite-database-is-full) |
| [14800028](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800028-sqlite-io-error) |
| [14800030](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-data-rdb.md#14800030-sqlite-unable-to-open-the-database-file) |

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
