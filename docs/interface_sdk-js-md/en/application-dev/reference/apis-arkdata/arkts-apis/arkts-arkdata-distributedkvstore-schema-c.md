# Schema

Defines the schema of a KV store. You can create a **Schema** object and pass it in [Options](arkts-arkdata-distributedkvstore-options-i.md#Options) when creating or opening a KV store.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-distributedKVStore-class Schema--><!--Device-distributedKVStore-class Schema-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## constructor

```TypeScript
constructor()
```

Defines a constructor used to create a **Schema** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Schema-constructor()--><!--Device-Schema-constructor()-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Examples

```TypeScript
let child1 = new distributedKVStore.FieldNode('id');
child1.type = distributedKVStore.ValueType.INTEGER;
child1.nullable = false;
child1.default = '1';
let child2 = new distributedKVStore.FieldNode('name');
child2.type = distributedKVStore.ValueType.STRING;
child2.nullable = false;
child2.default = 'zhangsan';

let schema = new distributedKVStore.Schema();
schema.root.appendChild(child1);
schema.root.appendChild(child2);
schema.indexes = ['$.id', '$.name'];
schema.mode = 1;
schema.skip = 0;
```

