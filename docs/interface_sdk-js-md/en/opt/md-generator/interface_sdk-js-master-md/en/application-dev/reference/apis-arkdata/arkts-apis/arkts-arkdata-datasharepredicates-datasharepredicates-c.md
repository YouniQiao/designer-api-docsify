# DataSharePredicates

Provides APIs for setting different **DataSharePredicates** objects. This type is not multi-thread safe. If a  
**DataSharePredicates** instance is operated by multiple threads at the same time in an application, use a lock for it.

**Since:** 10

<!--Device-dataSharePredicates-class DataSharePredicates--><!--Device-dataSharePredicates-class DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

## Modules to Import

```TypeScript
import { dataSharePredicates } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): DataSharePredicates
```

Creates a **DataSharePredicates** object to add the AND condition.

Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-and(): DataSharePredicates--><!--Device-DataSharePredicates-and(): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "lisi")
    .and()
    .equalTo("SALARY", 200.5);
```

## beginWrap

```TypeScript
beginWrap(): DataSharePredicates
```

Adds a left parenthesis to this **DataSharePredicates**. This API is similar to "(" in an SQL statement and must be used with the right parenthesis.

Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-beginWrap(): DataSharePredicates--><!--Device-DataSharePredicates-beginWrap(): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap();
```

## beginsWith

```TypeScript
beginsWith(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that begins with the specified value.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-beginsWith(field: string, value: string): DataSharePredicates--><!--Device-DataSharePredicates-beginsWith(field: string, value: string): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.beginsWith("NAME", "os");
```

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is within the specified range, including the start and end values.

Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-between(field: string, low: ValueType, high: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-between(field: string, low: ValueType, high: ValueType): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| low | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |
| high | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.between("AGE", 10, 50);
```

## contains

```TypeScript
contains(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that contains the specified value.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-contains(field: string, value: string): DataSharePredicates--><!--Device-DataSharePredicates-contains(field: string, value: string): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.contains("NAME", "os");
```

## distinct

```TypeScript
distinct(): DataSharePredicates
```

Creates a **DataSharePredicates** object to filter out duplicate data records.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-distinct(): DataSharePredicates--><!--Device-DataSharePredicates-distinct(): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose").distinct();
```

## endWrap

```TypeScript
endWrap(): DataSharePredicates
```

Adds a right parenthesis to this **DataSharePredicates**. This API is similar to ")" in an SQL statement and must be used with the left parenthesis.

Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-endWrap(): DataSharePredicates--><!--Device-DataSharePredicates-endWrap(): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap();
```

## endsWith

```TypeScript
endsWith(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that ends with the specified value.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-endsWith(field: string, value: string): DataSharePredicates--><!--Device-DataSharePredicates-endsWith(field: string, value: string): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.endsWith("NAME", "os");
```

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to search for the records in the specified column that are equal to the given value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-equalTo(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-equalTo(field: string, value: ValueType): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose");
```

## glob

```TypeScript
glob(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that matches the specified wildcard expression.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-glob(field: string, value: string): DataSharePredicates--><!--Device-DataSharePredicates-glob(field: string, value: string): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.glob("NAME", "?h*g");
```

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is greater than the specified value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-greaterThan(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-greaterThan(field: string, value: ValueType): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.greaterThan("AGE", 10);
```

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is greater than or equal to the specified value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.greaterThanOrEqualTo("AGE", 10);
```

## groupBy

```TypeScript
groupBy(fields: Array<string>): DataSharePredicates
```

Creates a **DataSharePredicates** object group the records according to the specified fields.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-groupBy(fields: Array<string>): DataSharePredicates--><!--Device-DataSharePredicates-groupBy(fields: Array<string>): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fields | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.groupBy(["AGE", "NAME"]);
```

## in

```TypeScript
in(field: string, value: Array<ValueType>): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is within the specified range.

Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-in(field: string, value: Array<ValueType>): DataSharePredicates--><!--Device-DataSharePredicates-in(field: string, value: Array<ValueType>): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.in("AGE", [18, 20]);
```

## inKeys

```TypeScript
inKeys(keys: Array<string>): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data whose keys are within the given range.

Currently, only the KVDB supports this **DataSharePredicates** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-inKeys(keys: Array<string>): DataSharePredicates--><!--Device-DataSharePredicates-inKeys(keys: Array<string>): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keys | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.inKeys(["Lisa", "Rose"]);
```

## indexedBy

```TypeScript
indexedBy(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to list data by the specified index. Before using this API, ensure that the index column exists.

Currently, only RDB store supports this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-indexedBy(field: string): DataSharePredicates--><!--Device-DataSharePredicates-indexedBy(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.indexedBy("SALARY_INDEX");
```

## isNotNull

```TypeScript
isNotNull(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data whose value is not null.

Currently, both the RDB store and KV store support this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-isNotNull(field: string): DataSharePredicates--><!--Device-DataSharePredicates-isNotNull(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.isNotNull("NAME");
```

## isNull

```TypeScript
isNull(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data whose value is null.

Currently, both the RDB store and KV store support this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-isNull(field: string): DataSharePredicates--><!--Device-DataSharePredicates-isNull(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.isNull("NAME");
```

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is less than the specified value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-lessThan(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-lessThan(field: string, value: ValueType): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.lessThan("AGE", 50);
```

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is less than or equal to the specified value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.lessThanOrEqualTo("AGE", 50);
```

## like

```TypeScript
like(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that matches the specified wildcard expression.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-like(field: string, value: string): DataSharePredicates--><!--Device-DataSharePredicates-like(field: string, value: string): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.like("NAME", "%os%");
```

## limit

```TypeScript
limit(total: number, offset: number): DataSharePredicates
```

Creates a **DataSharePredicates** object to specify the number of records in the result and the start position.

Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-limit(total: int, offset: int): DataSharePredicates--><!--Device-DataSharePredicates-limit(total: int, offset: int): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose").limit(10, 3);
```

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is out of the specified range, excluding the start and end values.

Currently, only RDB store supports this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| low | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |
| high | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.notBetween("AGE", 10, 50);
```

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is not equal to the specified value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-notEqualTo(field: string, value: ValueType): DataSharePredicates--><!--Device-DataSharePredicates-notEqualTo(field: string, value: ValueType): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.notEqualTo("NAME", "Rose");
```

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that is not in the specified value.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-notIn(field: string, value: Array<ValueType>): DataSharePredicates--><!--Device-DataSharePredicates-notIn(field: string, value: Array<ValueType>): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.notIn("NAME", ["Lisa", "Rose"]);
```

## or

```TypeScript
or(): DataSharePredicates
```

Creates a **DataSharePredicates** object to add the OR condition.

Currently, both the RDB store and KV store support this predicate.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-or(): DataSharePredicates--><!--Device-DataSharePredicates-or(): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates()
predicates.equalTo("NAME", "lisi")
    .or()
    .equalTo("NAME", "Rose");
```

## orderByAsc

```TypeScript
orderByAsc(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object that sorts records in ascending order.

Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-orderByAsc(field: string): DataSharePredicates--><!--Device-DataSharePredicates-orderByAsc(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByAsc("AGE");
```

## orderByDesc

```TypeScript
orderByDesc(field: string): DataSharePredicates
```

Creates a **DataSharePredicates** object that sorts data in descending order.

Currently, both the RDB store and KV store support this predicate.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataSharePredicates-orderByDesc(field: string): DataSharePredicates--><!--Device-DataSharePredicates-orderByDesc(field: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByDesc("AGE");
```

## prefixKey

```TypeScript
prefixKey(prefix: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data with the specified key prefix.

Currently, only the KVDB supports this **DataSharePredicates** object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-prefixKey(prefix: string): DataSharePredicates--><!--Device-DataSharePredicates-prefixKey(prefix: string): DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| prefix | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.prefixKey("NAME");
```

## unlike

```TypeScript
unlike(field: string, value: string): DataSharePredicates
```

Creates a **DataSharePredicates** object to match the data that does not match the specified wildcard expression.

Currently, both the RDB store and KV store support this predicate.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataSharePredicates-unlike(field: string, value: string): DataSharePredicates--><!--Device-DataSharePredicates-unlike(field: string, value: string): DataSharePredicates-End-->

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

## Examples

```TypeScript
let predicates = new dataSharePredicates.DataSharePredicates();
predicates.unlike("NAME", "%os%");
```
