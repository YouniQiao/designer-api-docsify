# Schema

Defines the schema of a KV store. You can create a **Schema** object and pass it in [Options](arkts-arkdata-distributedkvstore-options-i.md) when creating or opening a KV store.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## constructor

```TypeScript
constructor()
```

Defines a constructor used to create a **Schema** instance.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## indexes

```TypeScript
set indexes(indexes: Array<string>)
```

Set the string array of json.

**Type:** Array&lt;string&gt;

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## mode

```TypeScript
set mode(mode: number)
```

Set the mode of schema.

**Type:** number

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## root

```TypeScript
set root(root: FieldNode)
```

Set the root json object.

**Type:** FieldNode

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## skip

```TypeScript
set skip(skip: number)
```

Set the skip size of schema.

**Type:** number

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
