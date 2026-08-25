# FieldNode

Represents a **Schema** instance, which provides the APIs for defining the values stored in a KV store.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** FieldNode

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
```

## appendChild

```TypeScript
appendChild(child: FieldNode): boolean
```

Appends a child node to this **FieldNode**.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** appendChild

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [child](../../apis-arkui/arkts-components/arkts-arkui-nestedscrollinfo-i.md) | [FieldNode](arkts-arkdata-distributeddata-fieldnode-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## constructor

```TypeScript
constructor(name: string)
```

A constructor used to create a **FieldNode** instance with a string field.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** constructor

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

## default

```TypeScript
default: string
```

Default value of a **FieldNode**.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** default

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## nullable

```TypeScript
nullable: boolean
```

Whether the database field can be null.

**Type:** boolean

**Since:** 8

**Deprecated since:** 9

**Substitutes:** nullable

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## type

```TypeScript
type: number
```

Value of the data type corresponding to the specified node.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** type

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
