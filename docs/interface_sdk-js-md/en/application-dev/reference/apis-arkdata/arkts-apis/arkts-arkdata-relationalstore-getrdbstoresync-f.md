# getRdbStoreSync

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## getRdbStoreSync

```TypeScript
function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore
```

创建或打开已有的关系型数据库。开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。这是一个同步方法，会阻塞线程直到获取到RdbStore。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-arkdata-relationalstore-storeconfig-i.md)，数据库创建后，禁止对该参数进行修改。如果有修改参数，则会报错误码。

| 当前打开数据库时配置的加密类型 | 本设备上创建该数据库时的加密类型 | 结果 |  
| ------- | -------------------------------- | ---- |  
| 非加密 | 加密 | 使用加密配置（encrypt=true）打开数据库。 |  
| 加密 | 非加密 | 使用非加密配置（encrypt=false）打开数据库。 |

getRdbStoreSync支持多线程并发操作。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-relationalStore-function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore--><!--Device-relationalStore-function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用的上下文。 &lt;br&gt;FA模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)。 &lt;br&gt;Stage模型的应用Context定义见[Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-t.md/arkts-ability-context-t.md)。 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | Yes | 与此RDB存储相关的数据库配置。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md) | 返回RdbStore对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid args. |
| 14800017 | Config changed. |
| 14800021 | SQLite: Generic error. |
| 14800020 | The secret key is corrupted or lost. |
| 14801001 | The operation is supported in the stage model only. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800010 | Invalid database path. |
| 14801002 | Invalid data group ID. |
| 14800029 | SQLite: The database is full. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800030 | SQLite: Unable to open the database file. |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S1
    };

    try {
      store = relationalStore.getRdbStoreSync(this.context, STORE_CONFIG);
      console.info('Get RdbStore successfully.');
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
  }
}
```

