# FieldNode

Represents a **Schema** instance, which provides the methods for defining the values stored in a KV store.

**Since:** 23

**Deprecated since:** -1

<!--Device-distributedKVStore-class FieldNode--><!--Device-distributedKVStore-class FieldNode-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## appendChild

```TypeScript
appendChild(child: FieldNode): boolean
```

Appends a child node to this **FieldNode**.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-appendChild(child: FieldNode): boolean--><!--Device-FieldNode-appendChild(child: FieldNode): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| child | [FieldNode](arkts-arkdata-distributedkvstore-fieldnode-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
try {
  let node: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode('root');
  let child1: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode('child1');
  let child2: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode('child2');
  let child3: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode('child3');
  node.appendChild(child1);
  node.appendChild(child2);
  node.appendChild(child3);
  console.info('appendNode ' + JSON.stringify(node));
  child1 = null;
  child2 = null;
  child3 = null;
  node = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to append child. Code: ${error.code}, message: ${error.message}`);
}
```

## constructor

```TypeScript
constructor(name: string)
```

Defines a constructor used to create a **FieldNode** instance with a string field.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-constructor(name: string)--><!--Device-FieldNode-constructor(name: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## default

```TypeScript
default: string
```

Indicates the default value of field node.

**Type:** string

**Since:** 9

**Deprecated since:** -1

<!--Device-FieldNode-default: string--><!--Device-FieldNode-default: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
