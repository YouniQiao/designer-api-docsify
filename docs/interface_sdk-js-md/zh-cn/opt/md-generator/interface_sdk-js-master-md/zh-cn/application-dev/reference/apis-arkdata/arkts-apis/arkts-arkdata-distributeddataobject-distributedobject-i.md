# DistributedObject

表示一个分布式数据对象。在使用以下接口前，需调用[createDistributedObject()](arkts-arkdata-distributeddataobject-createdistributedobject-f.md#createDistributedObject)获取DistributedObject对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [null](null)

<!--Device-distributedDataObject-interface DistributedObject--><!--Device-distributedDataObject-interface DistributedObject-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void
```

当不再进行数据变更监听时，使用此接口删除对象的变更监听。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](distributedDataObject.DataObject.off(type:)

<!--Device-DistributedObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void--><!--Device-DistributedObject-off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | 否 |

## 示例

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
// 删除数据变更回调
g_object.off('change', (sessionId: string, fields: Array<string>) => {
    console.info('change' + sessionId);
    if (fields != null && fields != undefined) {
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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](distributedDataObject.DataObject.off()

<!--Device-DistributedObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DistributedObject-off(      type: 'status',      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | 否 |

## 示例

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
// 删除上下线回调
g_object.off('status', (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info('status changed ' + sessionId + ' ' + status + ' ' + networkId);
});
// 删除所有的上下线回调
g_object.off('status');
```

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void
```

监听分布式数据对象的变更。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [on](distributedDataObject.DataObject.on(type:)

<!--Device-DistributedObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void--><!--Device-DistributedObject-on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | 是 |

## 示例

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [on](distributedDataObject.DataObject.on()

<!--Device-DistributedObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void--><!--Device-DistributedObject-on(      type: 'status',      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | 是 |

## 示例

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setSessionId](distributedDataObject.DataObject.setSessionId(sessionId:)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DistributedObject-setSessionId(sessionId?: string): boolean--><!--Device-DistributedObject-setSessionId(sessionId?: string): boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

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
// g_object加入分布式组网
g_object.setSessionId(distributedDataObject.genSessionId());
// 设置为""退出分布式组网
g_object.setSessionId('');
```
