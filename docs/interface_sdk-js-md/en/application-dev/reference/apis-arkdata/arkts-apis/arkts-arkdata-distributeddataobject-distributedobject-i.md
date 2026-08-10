# DistributedObject

表示一个分布式数据对象。在使用以下接口前，需调用[createDistributedObject()](arkts-arkdata-distributeddataobject-createdistributedobject-f.md#createdistributedobject)获取DistributedObject对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [null]

<!--Device-distributedDataObject-interface DistributedObject--><!--Device-distributedDataObject-interface DistributedObject-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void
```

当不再进行数据变更监听时，使用此接口删除对象的变更监听。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** distributedDataObject.DataObject.off(type:

<!--Device-DistributedObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void--><!--Device-DistributedObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定为'change'，表示数据变更。 |
| callback | (sessionId: string, fields: Array&lt;string&gt;) =&gt; void | No | 需要删除的数据变更回调，若不设置则删除该对象所有的数据变更回调。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;fields：标识对象变更的属性名。 |

## Examples

```TypeScript
class SourceObject {
  name: string
  age: number
  isVis: boolean

  constructor(name: string, age: number, isVis: boolean) {
    this.name = name;
    this.age = age;
    this.isVis = isVis;
  }
}

let source: SourceObject = new SourceObject('jack', 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
// Unregister the specified data change callback.
g_object.off('change', (sessionId: string, fields: Array<string>) => {
    console.info('change' + sessionId);
    if (fields != null && fields != undefined) {
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

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** distributedDataObject.DataObject.off(

<!--Device-DistributedObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DistributedObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'status' | Yes | 事件类型，固定为'status'，表示对象上下线。 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) =&gt; void | No | 需要删除的上下线回调，若不设置则删除该对象所有的上下线回调。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;networkId：标识对象设备； &lt;br&gt;status：标识对象为'online'(上线)或'offline'(下线)的状态。 |

## Examples

```TypeScript
class SourceObject {
  name: string
  age: number
  isVis: boolean

  constructor(name: string, age: number, isVis: boolean) {
    this.name = name;
    this.age = age;
    this.isVis = isVis;
  }
}

let source: SourceObject = new SourceObject('jack', 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
// Unregister the specified status change callback.
g_object.off('status', (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info('status changed ' + sessionId + ' ' + status + ' ' + networkId);
});
// Unregister all status change callbacks.
g_object.off('status');
```

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void
```

监听分布式数据对象的变更。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** distributedDataObject.DataObject.on(type:

<!--Device-DistributedObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void--><!--Device-DistributedObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'change' | Yes | 事件类型，固定为'change'，表示数据变更。 |
| callback | (sessionId: string, fields: Array&lt;string&gt;) =&gt; void | Yes | 变更回调对象实例。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;fields：标识对象变更的属性名。 |

## Examples

```TypeScript
class SourceObject {
  name: string
  age: number
  isVis: boolean

  constructor(name: string, age: number, isVis: boolean) {
    this.name = name;
    this.age = age;
    this.isVis = isVis;
  }
}

let source: SourceObject = new SourceObject('jack', 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
g_object.on('change', (sessionId: string, fields: Array<string>) => {
    console.info('change' + sessionId);
    if (fields != null && fields != undefined) {
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

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** distributedDataObject.DataObject.on(

<!--Device-DistributedObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DistributedObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'status' | Yes | 事件类型，固定为'status'，表示对象上下线。 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) =&gt; void | Yes | 监听上下线回调实例。 &lt;br&gt;sessionId：标识变更对象的sessionId； &lt;br&gt;networkId：标识对象设备； &lt;br&gt;status：标识对象为'online'(上线)或'offline'(下线)的状态。 |

## Examples

```TypeScript
class SourceObject {
  name: string
  age: number
  isVis: boolean

  constructor(name: string, age: number, isVis: boolean) {
    this.name = name;
    this.age = age;
    this.isVis = isVis;
  }
}

let source: SourceObject = new SourceObject('jack', 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);

g_object.on('status', (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info('status changed ' + sessionId + ' ' + status + ' ' + networkId);
});
```

## setSessionId

```TypeScript
setSessionId(sessionId?: string): boolean
```

设置sessionId。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自动同步。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [distributedDataObject.DataObject.setSessionId](arkts-arkdata-distributeddataobject-dataobject-i.md#setsessionid)(sessionId:

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DistributedObject-setSessionId(sessionId?: string): boolean--><!--Device-DistributedObject-setSessionId(sessionId?: string): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | No | 分布式数据对象在可信组网中的标识ID。如果要退出分布式组网，设置为""或不设置均可。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：标识设置sessionId成功。 &lt;br&gt;false：标识设置sessionId失败。 |

## Examples

```TypeScript
class SourceObject {
  name: string
  age: number
  isVis: boolean

  constructor(name: string, age: number, isVis: boolean) {
    this.name = name;
    this.age = age;
    this.isVis = isVis;
  }
}

let source: SourceObject = new SourceObject('jack', 18, false);
let g_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
// Add g_object to the distributed network.
g_object.setSessionId(distributedDataObject.genSessionId());
// Remove g_object from the distributed network.
g_object.setSessionId('');
```

