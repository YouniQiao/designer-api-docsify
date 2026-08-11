# deleteRdbStore

## deleteRdbStore

```TypeScript
function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void
```

删除数据库文件，使用callback异步回调。

删除成功后，建议将数据库对象置为null。建立数据库时，若在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置了自定义路径，则调用此接口进行删库无效，必须使用   
[deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleterdbstore) 接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**起始版本：** 9

<!--Device-relationalStore-function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void--><!--Device-relationalStore-function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-参数检查失败) |
| [14800010](../../apis-basic-services-kit/errorcode-settings.md#14800010-上下文参数不是uiability类型) |

## 示例

FA模型示例：

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

relationalStore.deleteRdbStore(context, "RdbTest.db", (err: BusinessError) => {
  if (err) {
    console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
});
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    relationalStore.deleteRdbStore(this.context, "RdbTest.db", (err: BusinessError) => {
      if (err) {
        console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    });
  }
}
```


## deleteRdbStore

```TypeScript
function deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void
```

使用指定的数据库文件配置删除数据库，使用callback异步回调。

删除成功后，建议将数据库对象置为null。若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口，当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在  
[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**起始版本：** 10

<!--Device-relationalStore-function deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void--><!--Device-relationalStore-function deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-参数检查失败) |
| [14801001](../errorcode-data-rdb.md#14801001-上下文环境非stage模型) |
| [14800010](../../apis-basic-services-kit/errorcode-settings.md#14800010-上下文参数不是uiability类型) |
| [14801002](../errorcode-data-rdb.md#14801002-storeconfig中传入的datagroupid参数非法) |

## 示例

FA模型示例：

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.deleteRdbStore(context, STORE_CONFIG, (err: BusinessError) => {
  if (err) {
    console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
});
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    relationalStore.deleteRdbStore(this.context, STORE_CONFIG, (err: BusinessError) => {
      if (err) {
        console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    });
  }
}
```


## deleteRdbStore

```TypeScript
function deleteRdbStore(context: Context, name: string): Promise<void>
```

删除数据库文件，使用Promise异步回调。

删除成功后，建议将数据库对象置为null。建立数据库时，若在[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置了自定义路径，则调用此接口进行删库无效，必须使用   
[deleteRdbStore](arkts-arkdata-relationalstore-deleterdbstore-f.md#deleterdbstore) 接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**起始版本：** 9

<!--Device-relationalStore-function deleteRdbStore(context: Context, name: string): Promise<void>--><!--Device-relationalStore-function deleteRdbStore(context: Context, name: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-参数检查失败) |
| [14800010](../../apis-basic-services-kit/errorcode-settings.md#14800010-上下文参数不是uiability类型) |

## 示例

FA模型示例：

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

relationalStore.deleteRdbStore(context, "RdbTest.db").then(() => {
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    relationalStore.deleteRdbStore(this.context, "RdbTest.db").then(() => {
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
  }
}
```


## deleteRdbStore

```TypeScript
function deleteRdbStore(context: Context, config: StoreConfig): Promise<void>
```

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

删除成功后，建议将数据库对象置为null。若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口，当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在  
[StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**起始版本：** 10

<!--Device-relationalStore-function deleteRdbStore(context: Context, config: StoreConfig): Promise<void>--><!--Device-relationalStore-function deleteRdbStore(context: Context, config: StoreConfig): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| config | [StoreConfig](arkts-arkdata-relationalstore-storeconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14801001](../errorcode-data-rdb.md#14801001-上下文环境非stage模型) |
| [14800010](../../apis-basic-services-kit/errorcode-settings.md#14800010-上下文参数不是uiability类型) |
| [14801002](../errorcode-data-rdb.md#14801002-storeconfig中传入的datagroupid参数非法) |

## 示例

FA模型示例：

```TypeScript
import { featureAbility } from "@kit.AbilityKit";
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.deleteRdbStore(context, STORE_CONFIG).then(() => {
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    relationalStore.deleteRdbStore(this.context, STORE_CONFIG).then(() => {
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
  }
}
```
