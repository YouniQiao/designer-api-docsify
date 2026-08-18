# FieldNode

Represents a **Schema** instance, which provides the methods for defining the values stored in a KV store.

**Since:** 23

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-appendChild(child: FieldNode): boolean--><!--Device-FieldNode-appendChild(child: FieldNode): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | FieldNode | Yes | Child node to append. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |

**Examples**

```TypeScript
try {
  let node: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("root");
  let child1: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child1");
  let child2: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child2");
  let child3: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child3");
  node.appendChild(child1);
  node.appendChild(child2);
  node.appendChild(child3);
  console.info("appendNode " + JSON.stringify(node));
  child1 = null;
  child2 = null;
  child3 = null;
  node = null;
} catch (e) {
  console.error("AppendChild " + e);
}
```

## constructor

```TypeScript
constructor(name: string)
```

Defines a constructor used to create a **FieldNode** instance with a string field.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-constructor(name: string)--><!--Device-FieldNode-constructor(name: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Value of **FieldNode**, with a maximum of 64 characters. This parameter cannot be left blank. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Parameter verification failed. |

## default

```TypeScript
default: string
```

Indicates the default value of field node.

**Type:** string

**Since:** 9

<!--Device-FieldNode-default: string--><!--Device-FieldNode-default: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

