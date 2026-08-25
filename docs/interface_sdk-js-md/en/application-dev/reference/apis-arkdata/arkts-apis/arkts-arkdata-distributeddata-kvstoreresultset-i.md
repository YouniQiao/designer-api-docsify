# KvStoreResultSet

Provides APIs to obtain the KV store result sets, and query and move the data read position. Before calling any method in **KvStoreResultSet**, you must use getKVStore to obtain a **KVStore** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
```

## getCount

```TypeScript
getCount(): number
```

Obtains the total number of rows in the result set.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getCount

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getEntry

```TypeScript
getEntry(): Entry
```

Obtains the KV pair from the current position.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntry

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Entry](arkts-arkdata-distributeddata-entry-i.md) |

## getPosition

```TypeScript
getPosition(): number
```

Obtains the current data read position (position from which data is read) in the result set.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getPosition

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

Checks whether the data read position is after the last row.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** isAfterLast

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isBeforeFirst

```TypeScript
isBeforeFirst(): boolean
```

Checks whether the data read position is before the first row.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** isBeforeFirst

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFirst

```TypeScript
isFirst(): boolean
```

Checks whether the data read position is the first row.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** isFirst

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isLast

```TypeScript
isLast(): boolean
```

Checks whether the data read position is the last row.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** isLast

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## move

```TypeScript
move(offset: number): boolean
```

Moves the data read position with the specified offset from the current position.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** move

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## moveToFirst

```TypeScript
moveToFirst(): boolean
```

Moves the data read position to the first row. If the result set is empty, **false** will be returned.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** moveToFirst

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## moveToLast

```TypeScript
moveToLast(): boolean
```

Moves the data read position to the last row. If the result set is empty, **false** will be returned.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** moveToLast

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## moveToNext

```TypeScript
moveToNext(): boolean
```

Moves the data read position to the next row. If the result set is empty, **false** will be returned.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** moveToNext

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## moveToPosition

```TypeScript
moveToPosition(position: number): boolean
```

Moves the data read position from 0 to an absolute position.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** moveToPosition

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## moveToPrevious

```TypeScript
moveToPrevious(): boolean
```

Moves the data read position to the previous row. If the result set is empty, **false** will be returned.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** moveToPrevious

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
