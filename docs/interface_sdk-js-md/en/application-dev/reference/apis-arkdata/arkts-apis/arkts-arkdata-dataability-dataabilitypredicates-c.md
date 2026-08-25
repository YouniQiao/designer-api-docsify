# DataAbilityPredicates

Provides APIs for creating diverse query conditions.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

## Modules to Import

```TypeScript
import { dataAbility } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to add the AND condition.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## beginsWith

```TypeScript
beginsWith(field: string, value: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that begin with the given value.This API is similar to the percent sign (%) in SQL statements.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## beginWrap

```TypeScript
beginWrap(): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to add a left parenthesis. This API is similar to "(" in an SQL statement and must be used with **endWrap**.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are within the given range.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## contains

```TypeScript
contains(field: string, value: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that contain the given value.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## distinct

```TypeScript
distinct(): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to filter out duplicate records.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## endsWith

```TypeScript
endsWith(field: string, value: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that end with the given value.This API is similar to the percent sign (%) in SQL statements.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## endWrap

```TypeScript
endWrap(): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to add a right parenthesis. This API is similar to ")" in an SQL statement and must be used with **beginWrap**.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are equal to the given value.This API is similar to the SQL equal to (=) operator.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## glob

```TypeScript
glob(field: string, value: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that match the given string. Different from **like**, the input parameters of this API are case-sensitive.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are greater than the given value.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are greater than or equal to the given value.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## groupBy

```TypeScript
groupBy(fields: Array<string>): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to group the query results based on the specified columns.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are in the given range.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | Array & lt;ValueType & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## indexedBy

```TypeScript
indexedBy(field: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to specify the index column. Before calling this API, you need to create an index column.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## isNotNull

```TypeScript
isNotNull(field: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are not **null**.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## isNull

```TypeScript
isNull(field: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are **null**.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are less than the given value.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are less than or equal to the given value.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## like

```TypeScript
like(field: string, value: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are similar to the given value.This API is similar to the SQL **like** statement.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## limitAs

```TypeScript
limitAs(value: number): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to limit the number of records.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are out of the given range.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are not equal to the given value.This API is similar to the SQL not equal (!=) operator.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to search for the records in the specified column that are out of the given range.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | Array & lt;ValueType & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## offsetAs

```TypeScript
offsetAs(rowOffset: number): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to set the start position of the query result. This API must be used together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in **-1** in **limitAs**.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rowOffset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## or

```TypeScript
or(): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to add the OR condition.This API is similar to the SQL **or** operator.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to sort the records in the specified column in ascending order. When there are multiple **orderByAsc**s, the first **orderByAsc** used has the highest priority.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): DataAbilityPredicates
```

Creates a **DataAbilityPredicates** object to sort the records in the specified column in descending order. When there are multiple **orderByDesc**s, the first **orderByDesc** used has the highest priority.

**Since:** 7

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |
