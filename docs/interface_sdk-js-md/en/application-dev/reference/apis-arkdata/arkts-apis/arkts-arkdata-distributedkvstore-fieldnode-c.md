# FieldNode

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-class FieldNode--><!--Device-distributedKVStore-class FieldNode-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## appendChild

```TypeScript
appendChild(child: FieldNode): boolean
```

在当前 FieldNode 中添加一个子节点。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-appendChild(child: FieldNode): boolean--><!--Device-FieldNode-appendChild(child: FieldNode): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| child | [FieldNode](arkts-arkdata-distributedkvstore-fieldnode-c.md) | Yes | 要附加的子节点。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示子节点成功添加到FieldNode；返回false则表示操作失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. |

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

用于创建带有string字段FieldNode实例的构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-constructor(name: string)--><!--Device-FieldNode-constructor(name: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | FieldNode的值，不能为空，长度范围为1-64个字符。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Parameter verification failed. |

## default

```TypeScript
default: string
```

表示FieldNode的默认值。default需传入type对应类型可解析的字符串字面量，确保内容类型与type字段类型一致。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-FieldNode-default: string--><!--Device-FieldNode-default: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## defaultValue

```TypeScript
set defaultValue(defaultValue: string)
```

设置FieldNode的默认值.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-set defaultValue(defaultValue: string)--><!--Device-FieldNode-set defaultValue(defaultValue: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## nullable

```TypeScript
set nullable(isnullable: boolean)
```

设置数据库字段是否为空.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-set nullable(isnullable: boolean)--><!--Device-FieldNode-set nullable(isnullable: boolean)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## type

```TypeScript
set type(type: int)
```

设置节点对应的数据类型。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FieldNode-set type(type: int)--><!--Device-FieldNode-set type(type: int)-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

