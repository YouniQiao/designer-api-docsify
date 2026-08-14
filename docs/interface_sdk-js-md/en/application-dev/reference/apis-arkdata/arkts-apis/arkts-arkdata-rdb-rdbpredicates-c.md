# RdbPredicates

Defines predicates for an RDB store. This class determines whether the conditional expression for the RDB store is true or false.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md#RdbPredicates)

<!--Device-rdb-class RdbPredicates--><!--Device-rdb-class RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## and

```TypeScript
and(): RdbPredicates
```

Creates an **RdbPredicates** object to add the AND condition.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [and](arkts-arkdata-relationalstore-rdbpredicates-c.md#and)

<!--Device-RdbPredicates-and(): RdbPredicates--><!--Device-RdbPredicates-and(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
    .and()
    .equalTo("SALARY", 200.5)
```

## beginWrap

```TypeScript
beginWrap(): RdbPredicates
```

Creates an **RdbPredicates** object to add a left parenthesis.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [beginWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginWrap)

<!--Device-RdbPredicates-beginWrap(): RdbPredicates--><!--Device-RdbPredicates-beginWrap(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap()
```

## beginsWith

```TypeScript
beginsWith(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that start with the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [beginsWith](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginsWith)

<!--Device-RdbPredicates-beginsWith(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-beginsWith(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.beginsWith("NAME", "os")
```

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are within the specified range.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [between](arkts-arkdata-relationalstore-rdbpredicates-c.md#between)

<!--Device-RdbPredicates-between(field: string, low: ValueType, high: ValueType): RdbPredicates--><!--Device-RdbPredicates-between(field: string, low: ValueType, high: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| low | ValueType | Yes | Minimum value of the range to set. |
| high | ValueType | Yes | Maximum value of the range to set. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.between("AGE", 10, 50)
```

## constructor

```TypeScript
constructor(name: string)
```

A constructor used to create an **RdbPredicates** object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md#RdbPredicates)

<!--Device-RdbPredicates-constructor(name: string)--><!--Device-RdbPredicates-constructor(name: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Database table name. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
```

## contains

```TypeScript
contains(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that contain the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [contains](arkts-arkdata-relationalstore-rdbpredicates-c.md#contains)

<!--Device-RdbPredicates-contains(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-contains(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.contains("NAME", "os")
```

## distinct

```TypeScript
distinct(): RdbPredicates
```

Creates an **RdbPredicates** object to filter out duplicate records.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [distinct](arkts-arkdata-relationalstore-rdbpredicates-c.md#distinct)

<!--Device-RdbPredicates-distinct(): RdbPredicates--><!--Device-RdbPredicates-distinct(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose").distinct()
```

## endWrap

```TypeScript
endWrap(): RdbPredicates
```

Creates an **RdbPredicates** object to add a right parenthesis.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [endWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#endWrap)

<!--Device-RdbPredicates-endWrap(): RdbPredicates--><!--Device-RdbPredicates-endWrap(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "lisi")
    .beginWrap()
    .equalTo("AGE", 18)
    .or()
    .equalTo("SALARY", 200.5)
    .endWrap()
```

## endsWith

```TypeScript
endsWith(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that end with the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [endsWith](arkts-arkdata-relationalstore-rdbpredicates-c.md#endsWith)

<!--Device-RdbPredicates-endsWith(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-endsWith(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.endsWith("NAME", "se")
```

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are equal to the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalTo)

<!--Device-RdbPredicates-equalTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-equalTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | ValueType | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "lisi")
```

## glob

```TypeScript
glob(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that match the given string.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [glob](arkts-arkdata-relationalstore-rdbpredicates-c.md#glob)

<!--Device-RdbPredicates-glob(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-glob(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match.<br>Wildcards are supported. An asterisk (*) indicates zero, one, or multiple digits or characters, and a question mark (?) indicates a single digit or character. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.glob("NAME", "?h*g")
```

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are greater than the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [greaterThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterThan)

<!--Device-RdbPredicates-greaterThan(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-greaterThan(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | ValueType | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.greaterThan("AGE", 18)
```

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are greater than or equal to the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [greaterThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterThanOrEqualTo)

<!--Device-RdbPredicates-greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | ValueType | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.greaterThanOrEqualTo("AGE", 18)
```

## groupBy

```TypeScript
groupBy(fields: Array<string>): RdbPredicates
```

Creates an **RdbPredicates** object to group the query results based on the specified columns.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [groupBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#groupBy)

<!--Device-RdbPredicates-groupBy(fields: Array<string>): RdbPredicates--><!--Device-RdbPredicates-groupBy(fields: Array<string>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fields | Array&lt;string&gt; | Yes | Names of columns to group. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.groupBy(["AGE", "NAME"])
```

## in

```TypeScript
in(field: string, value: Array<ValueType>): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are within the specified range.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [in](arkts-arkdata-relationalstore-rdbpredicates-c.md#in)

<!--Device-RdbPredicates-in(field: string, value: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-in(field: string, value: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | Array&lt;ValueType&gt; | Yes | Array of **ValueType**s to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.in("AGE", [18, 20])
```

## inAllDevices

```TypeScript
inAllDevices(): RdbPredicates
```

Creates an **RdbPredicates** object to specify all remote devices on the network to connect during distributed database sync.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inAllDevices](arkts-arkdata-relationalstore-rdbpredicates-c.md#inAllDevices)

<!--Device-RdbPredicates-inAllDevices(): RdbPredicates--><!--Device-RdbPredicates-inAllDevices(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.inAllDevices()
```

## inDevices

```TypeScript
inDevices(devices: Array<string>): RdbPredicates
```

Creates an **RdbPredicates** object to specify the remote devices to connect on the network during distributed database sync. > **NOTE：**> The value of **devices** can be obtained by using &lt;!--RP2--&gt; > [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#getTrustedDeviceListSync) > . &lt;!--RP2End--&gt;The APIs of the **deviceManager** module are system interfaces and available only to system > applications.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [inDevices](arkts-arkdata-relationalstore-rdbpredicates-c.md#inDevices)

<!--Device-RdbPredicates-inDevices(devices: Array<string>): RdbPredicates--><!--Device-RdbPredicates-inDevices(devices: Array<string>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| devices | Array&lt;string&gt; | Yes | IDs of the remote devices in the same network. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: deviceManager.DeviceManager;
let deviceIds: Array<string> = [];
let devices: Array<string> = [];

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  devices = dmInstance.getTrustedDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds[i] = devices[i].deviceId;
  }
})

let predicates = new data_rdb.RdbPredicates("EMPLOYEE");
predicates.inDevices(deviceIds);
                                  
let predicates = new data_rdb.RdbPredicates("EMPLOYEE");
predicates.inDevices(deviceIds);
```

## indexedBy

```TypeScript
indexedBy(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to specify the index column.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [indexedBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#indexedBy)

<!--Device-RdbPredicates-indexedBy(field: string): RdbPredicates--><!--Device-RdbPredicates-indexedBy(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Name of the index column. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.indexedBy("SALARY_INDEX")
```

## isNotNull

```TypeScript
isNotNull(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are not **null**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [isNotNull](arkts-arkdata-relationalstore-rdbpredicates-c.md#isNotNull)

<!--Device-RdbPredicates-isNotNull(field: string): RdbPredicates--><!--Device-RdbPredicates-isNotNull(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2 . Incorrect parameter types. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.isNotNull("NAME")
```

## isNull

```TypeScript
isNull(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are **null**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [isNull](arkts-arkdata-relationalstore-rdbpredicates-c.md#isNull)

<!--Device-RdbPredicates-isNull(field: string): RdbPredicates--><!--Device-RdbPredicates-isNull(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.isNull("NAME")
```

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are less than the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [lessThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessThan)

<!--Device-RdbPredicates-lessThan(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-lessThan(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | ValueType | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.lessThan("AGE", 20)
```

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are less than or equal to the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [lessThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessThanOrEqualTo)

<!--Device-RdbPredicates-lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | ValueType | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.lessThanOrEqualTo("AGE", 20)
```

## like

```TypeScript
like(field: string, value: string): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are similar to the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [like](arkts-arkdata-relationalstore-rdbpredicates-c.md#like)

<!--Device-RdbPredicates-like(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-like(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | string | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.like("NAME", "%os%")
```

## limitAs

```TypeScript
limitAs(value: number): RdbPredicates
```

Creates an **RdbPredicates** object to limit the number of records.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [limitAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#limitAs)

<!--Device-RdbPredicates-limitAs(value: number): RdbPredicates--><!--Device-RdbPredicates-limitAs(value: number): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Maximum number of records. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose").limitAs(3)
```

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are out of the specified range.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [notBetween](arkts-arkdata-relationalstore-rdbpredicates-c.md#notBetween)

<!--Device-RdbPredicates-notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates--><!--Device-RdbPredicates-notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| low | ValueType | Yes | Minimum value of the range to set. |
| high | ValueType | Yes | Maximum value of the range to set. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.notBetween("AGE", 10, 50)
```

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are not equal to the given value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [notEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#notEqualTo)

<!--Device-RdbPredicates-notEqualTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-notEqualTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | ValueType | Yes | Value to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.notEqualTo("NAME", "lisi")
```

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): RdbPredicates
```

Creates an **RdbPredicates** object to search for the records in the specified column that are out of the specified range.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [notIn](arkts-arkdata-relationalstore-rdbpredicates-c.md#notIn)

<!--Device-RdbPredicates-notIn(field: string, value: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-notIn(field: string, value: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |
| value | Array&lt;ValueType&gt; | Yes | Array of **ValueType**s to match. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.notIn("NAME", ["Lisa", "Rose"])
```

## offsetAs

```TypeScript
offsetAs(rowOffset: number): RdbPredicates
```

Creates an **RdbPredicates** object to specify the start position of the returned result. This API must be used together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in **-1** in **limitAs**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [offsetAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#offsetAs)

<!--Device-RdbPredicates-offsetAs(rowOffset: number): RdbPredicates--><!--Device-RdbPredicates-offsetAs(rowOffset: number): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rowOffset | number | Yes | Start position, which is a positive integer. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose").limitAs(-1).offsetAs(3)
```

## or

```TypeScript
or(): RdbPredicates
```

Creates an **RdbPredicates** object to add the OR condition.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [or](arkts-arkdata-relationalstore-rdbpredicates-c.md#or)

<!--Device-RdbPredicates-or(): RdbPredicates--><!--Device-RdbPredicates-or(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
    .or()
    .equalTo("NAME", "Rose")
```

## orderByAsc

```TypeScript
orderByAsc(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to sort the records in the specified column in ascending order.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [orderByAsc](arkts-arkdata-relationalstore-rdbpredicates-c.md#orderByAsc)

<!--Device-RdbPredicates-orderByAsc(field: string): RdbPredicates--><!--Device-RdbPredicates-orderByAsc(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.orderByAsc("NAME")
```

## orderByDesc

```TypeScript
orderByDesc(field: string): RdbPredicates
```

Creates an **RdbPredicates** object to sort the records in the specified column in descending order.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [orderByDesc](arkts-arkdata-relationalstore-rdbpredicates-c.md#orderByDesc)

<!--Device-RdbPredicates-orderByDesc(field: string): RdbPredicates--><!--Device-RdbPredicates-orderByDesc(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | Column name in the database table. |

**Return value:**

| Type | Description |
| --- | --- |
| RdbPredicates | RdbPredicates** object created. |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.orderByDesc("AGE")
```

