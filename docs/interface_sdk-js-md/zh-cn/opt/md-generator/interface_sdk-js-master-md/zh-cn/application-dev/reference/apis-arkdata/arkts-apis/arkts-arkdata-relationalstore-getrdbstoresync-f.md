# getRdbStoreSync

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
| 加密 | 非加密 |

getRdbStoreSync支持多线程并发操作。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-relationalStore-function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore--><!--Device-relationalStore-function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [14800017](../errorcode-data-rdb.md#14800017-关键配置已被更改) |
| [14800021](../errorcode-data-rdb.md#14800021-sqlite通用错误) |
| [14800020](../errorcode-data-rdb.md#14800020-密钥损坏或丢失) |
| [14801001](../errorcode-data-rdb.md#14801001-上下文环境非stage模型) |
| [14800011](../errorcode-data-rdb.md#14800011-数据库文件异常) |
| [14800027](../errorcode-data-rdb.md#14800027-sqlite尝试写入只读数据库) |
| [14800010](../../apis-basic-services-kit/errorcode-settings.md#14800010-上下文参数不是uiability类型) |
| [14801002](../errorcode-data-rdb.md#14801002-storeconfig中传入的datagroupid参数非法) |
| [14800029](../errorcode-data-rdb.md#14800029-sqlite数据库已满) |
| [14800028](../errorcode-data-rdb.md#14800028-sqlite发生了某种磁盘io错误) |
| [14800030](../errorcode-data-rdb.md#14800030-sqlite无法打开数据库文件) |

## 示例

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
