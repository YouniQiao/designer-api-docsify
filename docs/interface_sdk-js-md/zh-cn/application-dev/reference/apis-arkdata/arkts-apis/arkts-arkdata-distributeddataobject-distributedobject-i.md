# DistributedObject

表示一个分布式数据对象。在使用以下接口前，需调用[createDistributedObject()](arkts-arkdata-distributeddataobject-createdistributedobject-f.md)获取 DistributedObject对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## 导入模块

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void
```

当不再进行数据变更监听时，使用此接口删除对象的变更监听。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** off(type: 'change', callback?: (sessionId: string, fields: Array&lt;string&gt;) =&gt; void )

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | 否 |

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

**替代接口：** off( type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) =&gt; void )

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | 否 |

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void
```

监听分布式数据对象的变更。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'change', callback: (sessionId: string, fields: Array&lt;string&gt;) =&gt; void )

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | 是 |

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

**替代接口：** on( type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) =&gt; void )

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'status' | 是 |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | 是 |

## setSessionId

```TypeScript
setSessionId(sessionId?: string): boolean
```

设置sessionId。当可信组网中有多个设备处于协同状态时，如果多个设备间的分布式对象设置为同一个sessionId，就能自动同步。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setSessionId](arkts-arkdata-distributeddataobject-dataobject-i.md#setsessionid)(sessionId: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |
