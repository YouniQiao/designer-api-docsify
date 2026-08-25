# DataSharePredicates

Provides APIs for setting different **DataSharePredicates** objects. This type is not multi-thread safe. If a **DataSharePredicates** instance is operated by multiple threads at the same time in an application, use a lock for it.

**Since:** 10

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

## Modules to Import

```TypeScript
import { dataSharePredicates } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): DataSharePredicates
```

Creates a **DataSharePredicates** object to add the AND condition.Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## beginWrap

```TypeScript
beginWrap(): DataSharePredicates
```

Adds a left parenthesis to this **DataSharePredicates**. This API is similar to "(" in an SQL statement and must be used with the right parenthesis.Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is within the specified range, including the start and end values.Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## endWrap

```TypeScript
endWrap(): DataSharePredicates
```

Adds a right parenthesis to this **DataSharePredicates**. This API is similar to ")" in an SQL statement and must be used with the left parenthesis.Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to search for the records in the specified column that are equal to the given value.Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is greater than the specified value.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is greater than or equal to the specified value.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is within the specified range.Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is less than the specified value.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is less than or equal to the specified value.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## like

```TypeScript
like(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that matches the specified wildcard expression.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## limit

```TypeScript
limit(total: number, offset: number): DataSharePredicates
```

Creates a **DataSharePredicates** object to specify the number of records in the result and the start position.Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| total | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is out of the specified range, excluding the start and end values.Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is not equal to the specified value.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is not in the specified value.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | Array&lt;[ValueType](arkts-arkdata-valuetype-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## or

```TypeScript
or(): DataSharePredicates
```

Creates a **DataSharePredicates** object to add the OR condition.Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object that sorts records in ascending order.Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object that sorts data in descending order.Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |
