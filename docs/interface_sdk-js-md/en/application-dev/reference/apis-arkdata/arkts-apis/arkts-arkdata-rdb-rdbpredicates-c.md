# RdbPredicates

Defines predicates for an RDB store. This class determines whether the conditional expression for the RDB store is true or false.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
```

## and

```TypeScript
and(): RdbPredicates
```

Creates an **RdbPredicates** object to add the AND condition.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [and](arkts-arkdata-relationalstore-rdbpredicates-c.md#and)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## beginsWith

```TypeScript
beginsWith(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that start with the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [beginsWith](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginswith)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## beginWrap

```TypeScript
beginWrap(): RdbPredicates
```

Creates an **RdbPredicates** object to add a left parenthesis.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [beginWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginwrap)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are within the specified range.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [between](arkts-arkdata-relationalstore-rdbpredicates-c.md#between)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## constructor

```TypeScript
constructor(name: string)
```

A constructor used to create an **RdbPredicates** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

## contains

```TypeScript
contains(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that contain the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [contains](arkts-arkdata-relationalstore-rdbpredicates-c.md#contains)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## distinct

```TypeScript
distinct(): RdbPredicates
```

Creates an **RdbPredicates** object to filter out duplicate records.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [distinct](arkts-arkdata-relationalstore-rdbpredicates-c.md#distinct)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## endsWith

```TypeScript
endsWith(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that end with the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [endsWith](arkts-arkdata-relationalstore-rdbpredicates-c.md#endswith)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## endWrap

```TypeScript
endWrap(): RdbPredicates
```

Creates an **RdbPredicates** object to add a right parenthesis.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [endWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#endwrap)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are equal to the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## glob

```TypeScript
glob(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that match the given string.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [glob](arkts-arkdata-relationalstore-rdbpredicates-c.md#glob)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are greater than the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [greaterThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterthan)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are greater than or equal to the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [greaterThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterthanorequalto)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## groupBy

```TypeScript
groupBy(fields: Array<string>): RdbPredicates
```

Creates an **RdbPredicates** object to group the query results based on the specified columns.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [groupBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#groupby)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are within the specified range.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [in](arkts-arkdata-relationalstore-rdbpredicates-c.md#in)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | Array & lt;ValueType & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## inAllDevices

```TypeScript
inAllDevices(): RdbPredicates
```

Creates an **RdbPredicates** object to specify all remote devices on the network to connect during distributed database sync.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inAllDevices](arkts-arkdata-relationalstore-rdbpredicates-c.md#inalldevices)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## inDevices

```TypeScript
inDevices(devices: Array<string>): RdbPredicates
```

Creates an **RdbPredicates** object to specify the remote devices to connect on the network during distributed database sync.

> **NOTE：**

> The value of **devices** can be obtained by using <!--RP2-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> . <!--RP2End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inDevices](arkts-arkdata-relationalstore-rdbpredicates-c.md#indevices)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| devices | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## indexedBy

```TypeScript
indexedBy(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to specify the index column.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [indexedBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#indexedby)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## isNotNull

```TypeScript
isNotNull(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are not **null**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isNotNull](arkts-arkdata-relationalstore-rdbpredicates-c.md#isnotnull)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isNull

```TypeScript
isNull(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are **null**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isNull](arkts-arkdata-relationalstore-rdbpredicates-c.md#isnull)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are less than the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [lessThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessthan)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are less than or equal to the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [lessThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessthanorequalto)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## like

```TypeScript
like(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are similar to the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [like](arkts-arkdata-relationalstore-rdbpredicates-c.md#like)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## limitAs

```TypeScript
limitAs(value: number): RdbPredicates
```

Creates an **RdbPredicates** object to limit the number of records.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [limitAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#limitas)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are out of the specified range.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notBetween](arkts-arkdata-relationalstore-rdbpredicates-c.md#notbetween)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are not equal to the given value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#notequalto)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are out of the specified range.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notIn](arkts-arkdata-relationalstore-rdbpredicates-c.md#notin)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |
| value | Array & lt;ValueType & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## offsetAs

```TypeScript
offsetAs(rowOffset: number): RdbPredicates
```

Creates an **RdbPredicates** object to specify the start position of the returned result. This API must be used together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in **-1** in **limitAs**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [offsetAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#offsetas)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rowOffset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## or

```TypeScript
or(): RdbPredicates
```

Creates an **RdbPredicates** object to add the OR condition.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [or](arkts-arkdata-relationalstore-rdbpredicates-c.md#or)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to sort the records in the specified column in ascending order.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [orderByAsc](arkts-arkdata-relationalstore-rdbpredicates-c.md#orderbyasc)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to sort the records in the specified column in descending order.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [orderByDesc](arkts-arkdata-relationalstore-rdbpredicates-c.md#orderbydesc)

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| field | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |
