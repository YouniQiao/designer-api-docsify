# DistributedObject

Provides APIs for managing a distributed data object. Before using any API of this class, use createDistributedObject() to create a DistributedObject object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void
```

Unsubscribes from data changes of this distributed data object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** off(type: 'change', callback?: (sessionId: string, fields: Array&lt;string&gt;) =&gt; void )

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | No |

## off('status')

```TypeScript
off(
      type: 'status',
      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

Unsubscribes from the status change of this distributed data object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** off( type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) =&gt; void )

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'status' | Yes |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | No |

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void
```

Subscribes to data changes of this distributed data object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** on(type: 'change', callback: (sessionId: string, fields: Array&lt;string&gt;) =&gt; void )

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | Yes |

## on('status')

```TypeScript
on(
      type: 'status',
      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

Subscribes to status changes of this distributed data object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** on( type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) =&gt; void )

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'status' | Yes |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | Yes |

## setSessionId

```TypeScript
setSessionId(sessionId?: string): boolean
```

Sets a session ID. For the devices in the collaboration state in a trusted network, data of the distributed objects with the same session ID can be automatically synced across devices.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setSessionId](arkts-arkdata-distributeddataobject-dataobject-i.md#setsessionid)(sessionId: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
