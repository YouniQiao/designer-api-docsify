# DataObject

表示一个分布式数据对象。在使用以下接口前，需调用[create()](arkts-arkdata-distributeddataobject-create-f.md#create)获取DataObject对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-interface DataObject--><!--Device-distributedDataObject-interface DataObject-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void
```

绑定分布式对象中的单个资产与其对应的数据库信息，当前版本只支持分布式对象中的资产与关系型数据库的绑定。使用callback方式异步回调。

当分布式对象中包含的资产和关系型数据库中包含的资产指向同一个实体资产文件，即两个资产的Uri相同时，就会存在冲突，我们把这种资产称为融合资产。如果需要分布式数据管理进行融合资产的冲突解决，需要先进行资产的绑定。当应用退出session后，绑定关系随之消失。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void--><!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assetKey | string | Yes | 待绑定的融合资产在分布式对象中的键值。 |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | Yes | 待绑定的融合资产在数据库中的信息，包含库名、表名、主键、列名及在数据库中的资产名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 绑定数据库的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

## Examples

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>--><!--Device-DataObject-bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assetKey | string | Yes | 待绑定的融合资产在分布式对象中的键值。 |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | Yes | 待绑定的融合资产在数据库中的信息，包含库名、表名、主键、列名及在数据库中的资产名。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-DataObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void--><!--Device-DataObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定为'change'，表示数据变更。 |
| callback | (sessionId: string, fields: Array&lt;string&gt;) =&gt; void | No | 需要删除的数据变更回调，若不设置则删除该对象所有的数据变更回调。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;fields：标识对象变更的属性名。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

## Examples

```TypeScript
// Unregister the specified data change callback.
g_object.off('change', (sessionId: string, fields: Array<string>) => {
    console.info('change' + sessionId);
    if (g_object != null && fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info('changed !' + fields[index] + ' ' + g_object[fields[index]]);
        }
    }
});
// Unregister all data change callbacks.
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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-DataObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DataObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'status' | Yes | 事件类型，固定为'status'，表示对象上下线。 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) =&gt; void | No | 需要删除的上下线回调，若不设置则删除该对象所有的上下线回调。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;networkId：标识对象设备； &lt;br&gt;status：标识对象为'online'(上线)或'offline'(下线)的状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

## Examples

```TypeScript
// Unregister the specified status change callback.
g_object.off('status', (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info('status changed ' + sessionId + ' ' + status + ' ' + networkId);
});
// Unregister all status change callbacks.
g_object.off('status');
```

## off('change')

```TypeScript
off(type: 'change', callback?: DataObserver): void
```

当不再进行数据变更监听时，使用此接口删除分布式对象数据变更监听的回调实例。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DataObject-off(type: 'change', callback?: DataObserver): void--><!--Device-DataObject-off(type: 'change', callback?: DataObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定为'change'，表示数据变更。 |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | No | 需要删除的数据变更回调实例，若不设置则删除该对象所有的数据变更回调实例。 |

## Examples

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
  // Unregister a single data change callback function.
  g_object.on('change', changeCallback1);
  g_object.off('change', changeCallback1);

  // Unregister all data change callback functions.
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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DataObject-off(type: 'status', callback?: StatusObserver): void--><!--Device-DataObject-off(type: 'status', callback?: StatusObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'status' | Yes | 事件类型，固定为'status'，表示数据对象状态变更事件。 |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | No | 需要删除状态变更的回调实例，若不设置则删除该对象所有的状态变更回调实例。 |

## Examples

```TypeScript
const statusCallback1: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info('status callback1' + sessionId);
}

const statusCallback2: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info('status callback2' + sessionId);
}
try {
  // Unregister a single status change callback function.
  g_object.on('status', statusCallback1);
  g_object.off('status', statusCallback1);

  // Unregister all status change callback functions.
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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DataObject-off(type: 'progressChanged', callback?: ProgressObserver): void--><!--Device-DataObject-off(type: 'progressChanged', callback?: ProgressObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'progressChanged' | Yes | 事件类型，固定为'progressChanged'，表示资产传输进度变化事件。 |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | No | 需要取消监听的回调实例，若不设置，则取消对该事件的所有监听。 |

## Examples

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
  // Unsubscribes from the asset transfer progress changes.
  g_object.off('progressChanged', progressChangedCallback1);

  g_object.on('progressChanged', progressChangedCallback1);
  g_object.on('progressChanged', progressChangedCallback2);
  // Unsubscribes from all asset transfer progress changes.
  g_object.off('progressChanged');
} catch (error) {
  console.error(`Failed to execute. Code: ${error.code}, message: ${error.message}`);
}
```

## offChange

```TypeScript
offChange(callback?: DataObserver): void
```

当不再进行数据变更监听时，使用此接口删除分布式对象数据变更监听的回调实例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DataObject-offChange(callback?: DataObserver): void--><!--Device-DataObject-offChange(callback?: DataObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | No | 需要删除的数据变更回调实例，若不设置则删除该对象所有的数据变更回调实例。 |

## offProgressChanged

```TypeScript
offProgressChanged(callback?: ProgressObserver): void
```

当不再进行资产传输进度监听时，使用此接口取消监听。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DataObject-offProgressChanged(callback?: ProgressObserver): void--><!--Device-DataObject-offProgressChanged(callback?: ProgressObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | No | 需要取消监听的事件回调，若不设置，则取消对该事件的所有监听。 |

## offStatus

```TypeScript
offStatus(callback?: StatusObserver): void
```

当不再进行分布式对象状态变更监听时，使用此接口删除分布式对象状态变更的回调实例。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DataObject-offStatus(callback?: StatusObserver): void--><!--Device-DataObject-offStatus(callback?: StatusObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | No | 需要删除状态变更的回调实例，若不设置则删除该对象所有的状态变更回调实例。 |

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void
```

监听分布式数据对象的数据变更。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-DataObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void--><!--Device-DataObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定为'change'，表示数据变更。 |
| callback | (sessionId: string, fields: Array&lt;string&gt;) =&gt; void | Yes | 变更回调对象实例。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;fields：标识对象变更的属性名。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-DataObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DataObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'status' | Yes | 事件类型，固定为'status'，表示对象上下线。 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) =&gt; void | Yes | 监听上下线回调实例。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;networkId：标识对象设备； &lt;br&gt;status：标识对象为'online'(上线)或'offline'(下线)的状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DataObject-on(type: 'change', callback: DataObserver): void--><!--Device-DataObject-on(type: 'change', callback: DataObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定为'change'，表示数据变更。 |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | Yes | 表示分布式对象数据变更的回调实例。 |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DataObject-on(type: 'status', callback: StatusObserver): void--><!--Device-DataObject-on(type: 'status', callback: StatusObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'status' | Yes | 事件类型，固定为'status'，表示分布式对象状态变更事件。 |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | Yes | 表示分布式对象状态变更的回调实例。 |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DataObject-on(type: 'progressChanged', callback: ProgressObserver): void--><!--Device-DataObject-on(type: 'progressChanged', callback: ProgressObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'progressChanged' | Yes | 事件类型，固定为'progressChanged'，表示资产传输进度变化事件。 |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | Yes | 表示资产传输进度变化的回调实例。 |

## Examples

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

## onChange

```TypeScript
onChange(callback: DataObserver): void
```

监听分布式对象的数据变更。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DataObject-onChange(callback: DataObserver): void--><!--Device-DataObject-onChange(callback: DataObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | Yes | 表示分布式对象数据变更的回调实例。 |

## onProgressChanged

```TypeScript
onProgressChanged(callback: ProgressObserver): void
```

监听资产传输进度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DataObject-onProgressChanged(callback: ProgressObserver): void--><!--Device-DataObject-onProgressChanged(callback: ProgressObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | Yes |  |

## onStatus

```TypeScript
onStatus(callback: StatusObserver): void
```

监听分布式对象的状态变更。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataObject-onStatus(callback: StatusObserver): void--><!--Device-DataObject-onStatus(callback: StatusObserver): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | Yes | 表示分布式对象状态变更的回调实例。 |

## revokeSave

```TypeScript
revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void
```

撤回保存的分布式数据对象。使用callback方式作为异步方法。

如果对象保存在本地设备，那么将删除所有受信任设备上所保存的数据。

如果对象保存在其他设备，那么将删除本地设备上的数据。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DataObject-revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void--><!--Device-DataObject-revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RevokeSaveSuccessResponse&gt; | Yes | 回调函数。返回RevokeSaveSuccessResponse，包含sessionId。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Incorrect parameter types. |
| 801 | Capability not supported. |

## Examples

```TypeScript
g_object.setSessionId('123456');
// Save data for persistence. 
g_object.save('local', (err: BusinessError, result: distributedDataObject.SaveSuccessResponse) => {
    if (err) {
        console.error(`Failed to save. Code: ${err.code}, message: ${err.message}`);
    }
    console.info('save callback');
    console.info('save sessionId: ' + result.sessionId);
    console.info('save version: ' + result.version);
    console.info('save deviceId:  ' + result.deviceId);
});
// Delete the persistence data.
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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DataObject-revokeSave(): Promise<RevokeSaveSuccessResponse>--><!--Device-DataObject-revokeSave(): Promise<RevokeSaveSuccessResponse>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RevokeSaveSuccessResponse&gt; | Promise对象。返回RevokeSaveSuccessResponse，包含sessionId。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |

## Examples

```TypeScript
g_object.setSessionId('123456');
// Save data for persistence. 
g_object.save('local').then((result: distributedDataObject.SaveSuccessResponse) => {
    console.info('save callback');
    console.info('save sessionId ' + result.sessionId);
    console.info('save version ' + result.version);
    console.info('save deviceId ' + result.deviceId);
}).catch((err: BusinessError) => {
    console.error(`Failed to save. Code: ${err.code}, message: ${err.message}`);
});
// Delete the persistence data.
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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DataObject-save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void--><!--Device-DataObject-save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 存储数据的设备号，标识需要保存对象的设备。"local"表示本地设备，否则表示其他设备的设备号。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SaveSuccessResponse&gt; | Yes | 回调函数。返回SaveSuccessResponse，包含sessionId、version、deviceId等 信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-DataObject-save(deviceId: string): Promise<SaveSuccessResponse>--><!--Device-DataObject-save(deviceId: string): Promise<SaveSuccessResponse>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 存储数据的设备号，标识需要保存对象的设备。"local"表示本地设备，否则表示其他设备的设备号。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SaveSuccessResponse&gt; | Promise对象。返回SaveSuccessResponse，包含sessionId、version、deviceId等信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DataObject-setAsset(assetKey: string, uri: string): Promise<void>--><!--Device-DataObject-setAsset(assetKey: string, uri: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assetKey | string | Yes | 分布式对象中资产类型数据对应的属性名。&lt;br/&gt;**使用约束：** &lt;br/&gt;（1）提供的assetKey对应的文件必须已存在且类型为资产 [Asset](arkts-arkdata-commontype-asset-i.md)，才可进行正确的设置资产。若assetKey对应文件不存在或文件存在但类型不是资产类型，可能会出现资产设置错误。 &lt;br/&gt;（2）在协同或接续场景下需要双端满足assetKey对应的文件存在且为资产类型，才可将设置的资产同步到对端设备。 |
| uri | string | Yes | 待设置的新资产的uri，表示该资产的存放的分布式路径。必须为真实存在的资产对应的分布式路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15400002 | Parameter error. Possible causes: 1. The assetKey is invalid, such as ""; 2. The uri is invalid, such as "". |
| 15400003 | The sessionId of the distributed object has been set. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DataObject-setAssets(assetsKey: string, uris: Array<string>): Promise<void>--><!--Device-DataObject-setAssets(assetsKey: string, uris: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| assetsKey | string | Yes | 分布式对象中资产数组类型数据对应的属性名。&lt;br/&gt;**使用约束：** &lt;br/&gt;（1）提供的assetsKey对应的文件已存在且类型必须为资产 [Asset](arkts-arkdata-commontype-asset-i.md)，才可进行正确的设置资产。若assetsKey对应文件不存在或文件存在但类型不是资产类型，可能会出现资产设置错 误。&lt;br/&gt;（2）在协同或接续场景下需要双端满足assetsKey对应的文件存在且为资产类型，才可将设置的资产数组同步到对端设备。 |
| uris | Array&lt;string&gt; | Yes | 待设置的新资产数组的uri集合，表示资产数组内每个资产存放的分布式路径。数组中元素的数量为[1, 50]，元素uri必须为真实存在的资产对应的分布式路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15400002 | Parameter error. Possible causes: 1. The assetsKey is invalid, such as ""; 2. The uris is invalid, such as the length of uris is more than 50. |
| 15400003 | The sessionId of the distributed object has been set. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DataObject-setSessionId(sessionId: string, callback: AsyncCallback<void>): void--><!--Device-DataObject-setSessionId(sessionId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | 分布式数据对象在可信组网中的标识ID，长度不大于128字节，且只能包含字母数字或下划线_。当传入""、null时表示退出分布式组网。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 加入session的异步回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. The sessionId allows only letters, digits, and underscores(_), and cannot exceed 128 in length. |
| 201 | Permission verification failed. |
| 15400001 | Failed to create the in-memory database. |

## Examples

```TypeScript
// Add g_object to the distributed network.
g_object.setSessionId(distributedDataObject.genSessionId(), () => {
    console.info('join session');
});
// g_object exits the distributed network.
g_object.setSessionId('', () => {
    console.info('leave all session');
});
```

## setSessionId

```TypeScript
setSessionId(callback: AsyncCallback<void>): void
```

退出所有已加入的session，使用callback方式异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 9 - 19: ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DataObject-setSessionId(callback: AsyncCallback<void>): void--><!--Device-DataObject-setSessionId(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 退出所有已加入session的异步回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Incorrect parameter types. |
| 201 | Permission verification failed.<br>**Applicable version:** 9 - 19 |
| 15400001 | Failed to create the in-memory database. |

## Examples

```TypeScript
// Add g_object to the distributed network.
g_object.setSessionId(distributedDataObject.genSessionId(), () => {
    console.info('join session');
});
// Exit the distributed network.
g_object.setSessionId(() => {
    console.info('leave all session.');
});
```

## setSessionId

```TypeScript
setSessionId(sessionId?: string): Promise<void>
```

设置sessionId或退出分布式组网，使用Promise异步回调。当传入""、null或不传入参数时，表示退出分布式组网。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自动同步。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DataObject-setSessionId(sessionId?: string): Promise<void>--><!--Device-DataObject-setSessionId(sessionId?: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | No | 分布式数据对象在可信组网中的标识ID，长度不大于128字节，且只能包含字母数字或下划线_。当传入""、null或不传入参数时表示退出分布式组网。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. The sessionId allows only letters, digits, and underscores(_), and cannot exceed 128 in length. |
| 201 | Permission verification failed. |
| 15400001 | Failed to create the in-memory database. |

## Examples

```TypeScript
// Add g_object to the distributed network.
g_object.setSessionId(distributedDataObject.genSessionId()).then(() => {
    console.info('join session.');
}).catch((error: BusinessError) => {
    console.error(`Failed to set sessionId. Code: ${error.code}, message: ${error.message}`);
});
// Exit the distributed network.
g_object.setSessionId().then(() => {
    console.info('leave all session.');
}).catch((error: BusinessError) => {
    console.error(`Failed to set sessionId. Code: ${error.code}, message: ${error.message}`);
});
```

## [key: string]

```TypeScript
[key: string]: Object | null | undefined
```

Get and set value of property.

**Type:** Object \| null \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DataObject-[key: string]: Object | null | undefined--><!--Device-DataObject-[key: string]: Object | null | undefined-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

