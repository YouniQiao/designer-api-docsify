# DataObject

表示一个分布式数据对象。在使用以下接口前，需调用[create()](arkts-arkdata-distributeddataobject-create-f.md#create)获取DataObject对象。

**起始版本：** 9

<!--Device-distributedDataObject-interface DataObject--><!--Device-distributedDataObject-interface DataObject-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void
```

绑定分布式对象中的单个资产与其对应的数据库信息，当前版本只支持分布式对象中的资产与关系型数据库的绑定。使用callback方式异步回调。

当分布式对象中包含的资产和关系型数据库中包含的资产指向同一个实体资产文件，即两个资产的Uri相同时，就会存在冲突，我们把这种资产称为融合资产。如果需要分布式数据管理进行融合资产的冲突解决，需要先进行资产的绑定。当应用退出session后，绑定关系随之消失。

**起始版本：** 11

<!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void--><!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetKey | string | 是 |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { commonType } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test_img.jpg',
      path: '/dir/test_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);
    g_object.setSessionId('123456');

    const bindInfo: distributedDataObject.BindInfo = {
      storeName: 'notepad',
      tableName: 'note_t',
      primaryKey: {
        'uuid': '00000000-0000-0000-0000-000000000000'
      },
      field: 'attachment',
      assetName: attachment.name as string
    }

    g_object.bindAssetStore('attachment', bindInfo, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to bind asset store. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('bindAssetStore success.');
    });
  }
}
```

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>
```

绑定分布式对象中的单个资产与其对应的数据库信息，当前版本只支持分布式对象中的资产与关系型数据库的绑定。使用Promise方式作为异步回调。

当分布式对象中包含的资产和关系型数据库中包含的资产指向同一个实体资产文件，即两个资产的Uri相同时，就会存在冲突，我们把这种资产称为融合资产。如果需要分布式数据管理进行融合资产的冲突解决，需要先进行资产的绑定。当应用退出session后，绑定关系随之消失。

**起始版本：** 11

<!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>--><!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetKey | string | 是 |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { commonType } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test_img.jpg',
      path: '/dir/test_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);
    g_object.setSessionId('123456');

    const bindInfo: distributedDataObject.BindInfo = {
      storeName: 'notepad',
      tableName: 'note_t',
      primaryKey: {
        'uuid': '00000000-0000-0000-0000-000000000000'
      },
      field: 'attachment',
      assetName: attachment.name as string
    }

    g_object.bindAssetStore('attachment', bindInfo).then(() => {
      console.info('bindAssetStore success.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to bind asset store. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void
```

当不再进行数据变更监听时，使用此接口删除对象的变更监听。

**起始版本：** 9

<!--Device-DataObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void--><!--Device-DataObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array&lt;string&gt;) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
// 删除数据变更回调
g_object.off('change', (sessionId: string, fields: Array<string>) => {
    console.info('change' + sessionId);
    if (g_object != null && fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info('changed !' + fields[index] + ' ' + g_object[fields[index]]);
        }
    }
});
// 删除所有的数据变更回调
g_object.off('change');
```

## off('status')

```TypeScript
off(
      type: 'status',
      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

当不再进行对象上下线监听时，使用此接口删除对象的上下线监听。

**起始版本：** 9

<!--Device-DataObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DataObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) =&gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
// 删除上下线回调
g_object.off('status', (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info('status changed ' + sessionId + ' ' + status + ' ' + networkId);
});
// 删除所有的上下线回调
g_object.off('status');
```

## off('change')

```TypeScript
off(type: 'change', callback?: DataObserver): void
```

当不再进行数据变更监听时，使用此接口删除分布式对象数据变更监听的回调实例。

**起始版本：** 20

<!--Device-DataObject-off(type: 'change', callback?: DataObserver): void--><!--Device-DataObject-off(type: 'change', callback?: DataObserver): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | 否 |

## 示例

```TypeScript
const changeCallback1: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
  console.info('change callback1 ' + sessionId);
  if (fields != null && fields != undefined) {
      for (let index: number = 0; index < fields.length; index++) {
          console.info('change !' + fields[index]);
      }
  }
}

const changeCallback2: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
  console.info('change callback2 ' + sessionId);
  if (fields != null && fields != undefined) {
      for (let index: number = 0; index < fields.length; index++) {
          console.info('change !' + fields[index]);
      }
  }
}

try {
  // 删除单个数据变更回调函数
  g_object.on('change', changeCallback1);
  g_object.off('change', changeCallback1);

  // 删除所有数据变更回调函数
  g_object.on('change', changeCallback1);
  g_object.on('change', changeCallback2);
  g_object.off('change');
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## off('status')

```TypeScript
off(type: 'status', callback?: StatusObserver): void
```

当不再进行分布式对象状态变更监听时，使用此接口删除分布式对象状态变更的回调实例。

**起始版本：** 20

<!--Device-DataObject-off(type: 'status', callback?: StatusObserver): void--><!--Device-DataObject-off(type: 'status', callback?: StatusObserver): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | 否 |

## 示例

```TypeScript
const statusCallback1: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info('status callback1' + sessionId);
}

const statusCallback2: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info('status callback2' + sessionId);
}
try {
  // 删除单个状态变更回调函数
  g_object.on('status', statusCallback1);
  g_object.off('status', statusCallback1);

  // 删除所有状态变更回调函数
  g_object.on('status', statusCallback1);
  g_object.on('status', statusCallback2);
  g_object.off('status');
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## off('progressChanged')

```TypeScript
off(type: 'progressChanged', callback?: ProgressObserver): void
```

当不再进行资产传输进度监听时，使用此接口删除资产传输进度监听的回调实例。

**起始版本：** 20

<!--Device-DataObject-off(type: 'progressChanged', callback?: ProgressObserver): void--><!--Device-DataObject-off(type: 'progressChanged', callback?: ProgressObserver): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progressChanged' | 是 |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | 否 |

## 示例

```TypeScript
const progressChangedCallback1: distributedDataObject.ProgressObserver = (sessionId: string, progress: number) => {
  console.info('progressChanged callback1' + sessionId);
  console.info('progressChanged callback1' + progress);
}

const progressChangedCallback2: distributedDataObject.ProgressObserver = (sessionId: string, progress: number) => {
  console.info('progressChanged callback2' + sessionId);
  console.info('progressChanged callback2' + progress);
}
try {
  g_object.on('progressChanged', progressChangedCallback1);
  // 取消对资产传输进度的监听
  g_object.off('progressChanged', progressChangedCallback1);

  g_object.on('progressChanged', progressChangedCallback1);
  g_object.on('progressChanged', progressChangedCallback2);
  // 取消对资产传输进度的所有监听
  g_object.off('progressChanged');
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void
```

监听分布式数据对象的数据变更。

**起始版本：** 9

<!--Device-DataObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void--><!--Device-DataObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array&lt;string&gt;) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
g_object.on('change', (sessionId: string, fields: Array<string>) => {
    console.info('change' + sessionId);
    if (g_object != null && fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info('changed !' + fields[index] + ' ' + g_object[fields[index]]);
        }
    }
});
```

## on('status')

```TypeScript
on(
      type: 'status',
      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

监听分布式数据对象的上下线。

**起始版本：** 9

<!--Device-DataObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DataObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
g_object.on('status', (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info('status changed ' + sessionId + ' ' + status + ' ' + networkId);
});
```

## on('change')

```TypeScript
on(type: 'change', callback: DataObserver): void
```

监听分布式对象的数据变更。

**起始版本：** 20

<!--Device-DataObject-on(type: 'change', callback: DataObserver): void--><!--Device-DataObject-on(type: 'change', callback: DataObserver): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | 是 |

## 示例

```TypeScript
const changeCallback1: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
  console.info('change callback1 ' + sessionId);
  if (fields != null && fields != undefined) {
      for (let index: number = 0; index < fields.length; index++) {
          console.info('change !' + fields[index]);
      }
  }
}
try {
  g_object.on('change', changeCallback1);
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## on('status')

```TypeScript
on(type: 'status', callback: StatusObserver): void
```

监听分布式对象的状态变更。

**起始版本：** 20

<!--Device-DataObject-on(type: 'status', callback: StatusObserver): void--><!--Device-DataObject-on(type: 'status', callback: StatusObserver): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | 是 |

## 示例

```TypeScript
const statusCallback1: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info('status callback ' + sessionId);
}
try {
  g_object.on('status', statusCallback1);
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## on('progressChanged')

```TypeScript
on(type: 'progressChanged', callback: ProgressObserver): void
```

监听资产传输进度。

**起始版本：** 20

<!--Device-DataObject-on(type: 'progressChanged', callback: ProgressObserver): void--><!--Device-DataObject-on(type: 'progressChanged', callback: ProgressObserver): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'progressChanged' | 是 |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | 是 |

## 示例

```TypeScript
const progressChangedCallback: distributedDataObject.ProgressObserver = (sessionId: string, progress: number) => {
  console.info('progressChanged callback' + sessionId);
  console.info('progressChanged callback' + progress);
}
try {
  g_object.on('progressChanged', progressChangedCallback);
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## revokeSave

```TypeScript
revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void
```

撤回保存的分布式数据对象。使用callback方式作为异步方法。

如果对象保存在本地设备，那么将删除所有受信任设备上所保存的数据。

如果对象保存在其他设备，那么将删除本地设备上的数据。

**起始版本：** 9

<!--Device-DataObject-revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void--><!--Device-DataObject-revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RevokeSaveSuccessResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
g_object.setSessionId('123456');
// 持久化数据
g_object.save('local', (err: BusinessError, result: distributedDataObject.SaveSuccessResponse) => {
    if (err) {
        console.error(`Failed to save. Code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info('save callback');
    console.info('save sessionId: ' + result.sessionId);
    console.info('save version: ' + result.version);
    console.info('save deviceId:  ' + result.deviceId);
});
// 删除持久化保存的数据
g_object.revokeSave((err: BusinessError, result: distributedDataObject.RevokeSaveSuccessResponse) => {
    if (err) {
      console.error(`Failed to revoke save. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('revokeSave callback');
    console.info('revokeSave sessionId ' + result.sessionId);
});
```

## revokeSave

```TypeScript
revokeSave(): Promise<RevokeSaveSuccessResponse>
```

撤回保存的分布式数据对象。使用Promise方式作为异步方法。

如果对象保存在本地设备，那么将删除所有受信任设备上所保存的数据。

如果对象保存在其他设备，那么将删除本地设备上的数据。

**起始版本：** 9

<!--Device-DataObject-revokeSave(): Promise<RevokeSaveSuccessResponse>--><!--Device-DataObject-revokeSave(): Promise<RevokeSaveSuccessResponse>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**返回值：**

| 类型 |
| --- |
| Promise&lt;RevokeSaveSuccessResponse&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
g_object.setSessionId('123456');
// 持久化数据
g_object.save('local').then((result: distributedDataObject.SaveSuccessResponse) => {
    console.info('save callback');
    console.info('save sessionId ' + result.sessionId);
    console.info('save version ' + result.version);
    console.info('save deviceId ' + result.deviceId);
}).catch((err: BusinessError) => {
    console.error(`Failed to save. Code: ${err.code}, message: ${err.message}`);
});
// 删除持久化保存的数据
g_object.revokeSave().then((result: distributedDataObject.RevokeSaveSuccessResponse) => {
    console.info('revokeSave callback');
    console.info('sessionId' + result.sessionId);
}).catch((err: BusinessError) => {
    console.error(`Failed to revoke save. Code: ${err.code}, message: ${err.message}`);
});
```

## save

```TypeScript
save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void
```

保存分布式数据对象。使用callback方式异步回调。

对象数据保存成功后，当应用存在时不会释放对象数据，当应用退出后，重新进入应用时，恢复保存在设备上的数据。

有以下几种情况时，保存的数据将会被释放：

- 存储时间超过24小时。  
- 应用卸载。  
- 成功恢复数据之后。

**起始版本：** 9

<!--Device-DataObject-save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void--><!--Device-DataObject-save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SaveSuccessResponse&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
g_object.setSessionId('123456');
g_object.save('local', (err: BusinessError, result:distributedDataObject.SaveSuccessResponse) => {
    if (err) {
        console.error(`Failed to save. Code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info('save callback');
    console.info('save sessionId: ' + result.sessionId);
    console.info('save version: ' + result.version);
    console.info('save deviceId:  ' + result.deviceId);
});
```

## save

```TypeScript
save(deviceId: string): Promise<SaveSuccessResponse>
```

保存分布式数据对象。使用Promise方式作为异步回调。

对象数据保存成功后，当应用存在时不会释放对象数据，当应用退出后，重新进入应用时，恢复保存在设备上的数据。

有以下几种情况时，保存的数据将会被释放：

- 存储时间超过24小时。  
- 应用卸载。  
- 成功恢复数据之后。

**起始版本：** 9

<!--Device-DataObject-save(deviceId: string): Promise<SaveSuccessResponse>--><!--Device-DataObject-save(deviceId: string): Promise<SaveSuccessResponse>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;SaveSuccessResponse&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
g_object.setSessionId('123456');
g_object.save('local').then((callbackInfo: distributedDataObject.SaveSuccessResponse) => {
    console.info('save callback');
    console.info('save sessionId ' + callbackInfo.sessionId);
    console.info('save version ' + callbackInfo.version);
    console.info('save deviceId ' + callbackInfo.deviceId);
}).catch((err: BusinessError) => {
    console.error(`Failed to save. Code: ${err.code}, message: ${err.message}`);
});
```

## setAsset

```TypeScript
setAsset(assetKey: string, uri: string): Promise<void>
```

设置分布式对象中的单个资产的属性信息，该接口必须在[setSessionId](arkts-arkdata-distributeddataobject-dataobject-i.md#setsessionid)接口调用前使用。使用Promise异步回调。

**起始版本：** 20

<!--Device-DataObject-setAsset(assetKey: string, uri: string): Promise<void>--><!--Device-DataObject-setAsset(assetKey: string, uri: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetKey | string | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15400002](../errorcode-distributed-dataObject.md#15400002-参数错误) |
| [15400003](../errorcode-distributed-dataObject.md#15400003-已设置分布式对象的sessionid) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { commonType, distributedDataObject } from '@kit.ArkData';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test_img.jpg',
      path: '/dir/test_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);

    let uri = 'file://test/test.img';
    g_object.setAsset('attachment', uri).then(() => {
      console.info('setAsset success.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set asset. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## setAssets

```TypeScript
setAssets(assetsKey: string, uris: Array<string>): Promise<void>
```

设置分布式对象中的多个资产的属性信息，该接口必须在[setSessionId](arkts-arkdata-distributeddataobject-dataobject-i.md#setsessionid)接口调用前使用。使用Promise异步回调。

**起始版本：** 20

<!--Device-DataObject-setAssets(assetsKey: string, uris: Array<string>): Promise<void>--><!--Device-DataObject-setAssets(assetsKey: string, uris: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetsKey | string | 是 |
| uris | Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15400002](../errorcode-distributed-dataObject.md#15400002-参数错误) |
| [15400003](../errorcode-distributed-dataObject.md#15400003-已设置分布式对象的sessionid) |

## 示例

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { commonType, distributedDataObject } from '@kit.ArkData';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test_img.jpg',
      path: '/dir/test_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);

    let uris: Array<string> = ['file://test/test_1.txt', 'file://test/test_2.txt'];
    g_object.setAssets('attachment', uris).then(() => {
      console.info('setAssets success.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to set assets. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## setSessionId

```TypeScript
setSessionId(sessionId: string, callback: AsyncCallback<void>): void
```

设置sessionId，使用callback方式异步回调。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自动同步。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DataObject-setSessionId(sessionId: string, callback: AsyncCallback<void>): void--><!--Device-DataObject-setSessionId(sessionId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-创建内存数据库失败) |

## 示例

```TypeScript
// g_object加入分布式组网
g_object.setSessionId(distributedDataObject.genSessionId(), () => {
    console.info('join session');
});
// g_object退出分布式组网
g_object.setSessionId('', () => {
    console.info('leave all session');
});
```

## setSessionId

```TypeScript
setSessionId(callback: AsyncCallback<void>): void
```

退出所有已加入的session，使用callback方式异步回调。

**起始版本：** 9

**需要权限：** 
- API版本9 - 19：ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DataObject-setSessionId(callback: AsyncCallback<void>): void--><!--Device-DataObject-setSessionId(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-创建内存数据库失败) |

## 示例

```TypeScript
// g_object加入分布式组网
g_object.setSessionId(distributedDataObject.genSessionId(), () => {
    console.info('join session');
});
// 退出分布式组网
g_object.setSessionId(() => {
    console.info('leave all session.');
});
```

## setSessionId

```TypeScript
setSessionId(sessionId?: string): Promise<void>
```

设置sessionId或退出分布式组网，使用Promise异步回调。当传入""、null或不传入参数时，表示退出分布式组网。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自动同步。

**起始版本：** 9

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DataObject-setSessionId(sessionId?: string): Promise<void>--><!--Device-DataObject-setSessionId(sessionId?: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-创建内存数据库失败) |

## 示例

```TypeScript
// g_object加入分布式组网
g_object.setSessionId(distributedDataObject.genSessionId()).then(() => {
    console.info('join session.');
}).catch((error: BusinessError) => {
    console.error(`Failed to set sessionId. Code: ${error.code}, message: ${error.message}`);
});
// 退出分布式组网
g_object.setSessionId().then(() => {
    console.info('leave all session.');
}).catch((error: BusinessError) => {
    console.error(`Failed to set sessionId. Code: ${error.code}, message: ${error.message}`);
});
```
