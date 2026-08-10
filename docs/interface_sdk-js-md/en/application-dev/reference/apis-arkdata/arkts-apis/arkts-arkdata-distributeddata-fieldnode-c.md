# FieldNode

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.FieldNode

<!--Device-distributedData-class FieldNode--><!--Device-distributedData-class FieldNode-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## appendChild

```TypeScript
appendChild(child: FieldNode): boolean
```

在当前 FieldNode 中添加一个子节点。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.FieldNode#appendChild

<!--Device-FieldNode-appendChild(child: FieldNode): boolean--><!--Device-FieldNode-appendChild(child: FieldNode): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | [FieldNode](arkts-arkdata-distributedkvstore-fieldnode-c.md) | Yes | 要附加的域节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示子节点成功添加到FieldNode；返回false则表示操作失败。 |

## Examples

```TypeScript
import ddm from '@ohos.data.distributedData';
try {
    let node = new ddm.FieldNode("root");
    let child1 = new ddm.FieldNode("child1");
    let child2 = new ddm.FieldNode("child2");
    let child3 = new ddm.FieldNode("child3");
    node.appendChild(child1);
    node.appendChild(child2);
    node.appendChild(child3);
    console.log("appendNode " + JSON.stringify(node));
    child1 = null;
    child2 = null;
    child3 = null;
    node = null;
} catch (e) {
    console.log("AppendChild " + e);
}
```

## constructor

```TypeScript
constructor(name: string)
```

用于创建带有string字段FieldNode实例的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.FieldNode#constructor

<!--Device-FieldNode-constructor(name: string)--><!--Device-FieldNode-constructor(name: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | FieldNode的值。 |

## default

```TypeScript
default: string
```

表示Fieldnode的默认值。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.FieldNode#default

<!--Device-FieldNode-default: string--><!--Device-FieldNode-default: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## nullable

```TypeScript
nullable: boolean
```

表示数据库字段是否可以为空。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.FieldNode#nullable

<!--Device-FieldNode-nullable: boolean--><!--Device-FieldNode-nullable: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## type

```TypeScript
type: number
```

表示指定节点对应数据类型的值。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.FieldNode#type

<!--Device-FieldNode-type: number--><!--Device-FieldNode-type: number-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

