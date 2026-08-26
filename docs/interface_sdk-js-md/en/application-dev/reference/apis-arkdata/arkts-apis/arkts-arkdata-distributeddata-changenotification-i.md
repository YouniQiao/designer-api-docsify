# ChangeNotification

Defines the content of data change notifications, including inserted data, updated data, deleted data, and device ID.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ChangeNotification

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import distributedDataObject from '@kit.ArkDataObject';
```

## deleteEntries

```TypeScript
deleteEntries: Entry[]
```

Data deleted.

**Type:** Entry[]

**Since:** 7

**Deprecated since:** 9

**Substitutes:** deleteEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId: string
```

UUID of the device.

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** deviceId

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Examples**

```TypeScript
try {
    let query = new distributedData.Query();
    query.deviceId("deviceId");
    console.log("query is " + query.getSqlLike());
} catch (e) {
    console.log("should be ok on Method Chaining : " + e);
}
```

## insertEntries

```TypeScript
insertEntries: Entry[]
```

Data inserted.

**Type:** Entry[]

**Since:** 7

**Deprecated since:** 9

**Substitutes:** insertEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## updateEntries

```TypeScript
updateEntries: Entry[]
```

Data updated.

**Type:** Entry[]

**Since:** 7

**Deprecated since:** 9

**Substitutes:** updateEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core
