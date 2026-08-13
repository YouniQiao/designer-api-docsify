# RdbStore

Provides APIs for managing data in an RDB store. Before using the APIs of this class, use [executeSql](#executeSql) to initialize the database table structure and related data.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [RdbStore](arkts-arkdata-relationalstore-rdbstore-i.md#RdbStore)

<!--Device-rdb-interface RdbStore--><!--Device-rdb-interface RdbStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

Inserts a batch of data into a table. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [batchInsert](arkts-arkdata-relationalstore-rdbstore-i.md#batchInsert)

<!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void--><!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);
const valueBucket1: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
const valueBucket2: ValuesBucket = {
  key1: value5,
  key2: value6,
  key3: value7,
  key4: value8,
};
const valueBucket3: ValuesBucket = {
  key1: value9,
  key2: value10,
  key3: value11,
  key4: value12,
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
rdbStore.batchInsert("EMPLOYEE", valueBuckets, (status: number, insertNum: number) => {
  if (status) {
    console.log("batchInsert is failed, status = " + status);
    return;
  }
  console.log("batchInsert is successful, the number of values that were inserted = " + insertNum);
})
```

## batchInsert

```TypeScript
batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>
```

Inserts a batch of data into a table. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [batchInsert](arkts-arkdata-relationalstore-rdbstore-i.md#batchInsert)

<!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>--><!--Device-RdbStore-batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array & lt;ValuesBucket & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);
const valueBucket1: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
const valueBucket2: ValuesBucket = {
  key1: value5,
  key2: value6,
  key3: value7,
  key4: value8,
};
const valueBucket3: ValuesBucket = {
  key1: value9,
  key2: value10,
  key3: value11,
  key4: value12,
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
let promise: void = rdbStore.batchInsert("EMPLOYEE", valueBuckets);
promise.then((insertNum: number) => {
  console.log("batchInsert is successful, the number of values that were inserted = " + insertNum);
}).catch((status: number) => {
  console.log("batchInsert is failed, status = " + status);
})
```

## beginTransaction

```TypeScript
beginTransaction(): void
```

Starts the transaction before executing an SQL statement.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [beginTransaction](arkts-arkdata-relationalstore-rdbstore-i.md#beginTransaction)

<!--Device-RdbStore-beginTransaction(): void--><!--Device-RdbStore-beginTransaction(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Examples

```TypeScript
import featureAbility from '@ohos.ability.featureAbility';
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "blobType";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

data_rdb.getRdbStore(this.context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
  rdbStore.beginTransaction()
  await rdbStore.insert("test", valueBucket)
  rdbStore.commit()
})
```

## commit

```TypeScript
commit(): void
```

Commits the executed SQL statements.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [commit](arkts-arkdata-relationalstore-rdbstore-i.md#commit)

<!--Device-RdbStore-commit(): void--><!--Device-RdbStore-commit(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';
import featureAbility from '@ohos.ability.featureAbility';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "blobType";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

data_rdb.getRdbStore(this.context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
  rdbStore.beginTransaction()
  await rdbStore.insert("test", valueBucket)
  rdbStore.commit()
})
```

## delete

```TypeScript
delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [delete](arkts-arkdata-relationalstore-rdbstore-i.md#delete)

<!--Device-RdbStore-delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void--><!--Device-RdbStore-delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
rdbStore.delete(predicates, (err: BusinessError, rows: number) => {
  if (err) {
    console.info("Delete failed, err: " + err)
    return
  }
  console.log("Delete rows: " + rows)
})
```

## delete

```TypeScript
delete(predicates: RdbPredicates): Promise<number>
```

Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [delete](arkts-arkdata-relationalstore-rdbstore-i.md#delete)

<!--Device-RdbStore-delete(predicates: RdbPredicates): Promise<number>--><!--Device-RdbStore-delete(predicates: RdbPredicates): Promise<number>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
let promise: void = rdbStore.delete(predicates)
promise.then((rows: number) => {
  console.log("Delete rows: " + rows)
}).catch((err: BusinessError) => {
  console.info("Delete failed, err: " + err)
})
```

## executeSql

```TypeScript
executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void
```

Executes an SQL statement that contains specified arguments but returns no value. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [executeSql](arkts-arkdata-relationalstore-rdbstore-i.md#executeSql)

<!--Device-RdbStore-executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void--><!--Device-RdbStore-executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = ?"
rdbStore.executeSql(SQL_DELETE_TABLE, ['zhangsan'], (err: BusinessError) => {
  if (err) {
    console.info("ExecuteSql failed, err: " + err)
    return
  }
  console.info('Delete table done.')
})
```

## executeSql

```TypeScript
executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>
```

Executes an SQL statement that contains specified arguments but returns no value. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [executeSql](arkts-arkdata-relationalstore-rdbstore-i.md#executeSql)

<!--Device-RdbStore-executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>--><!--Device-RdbStore-executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = 'zhangsan'"
let promise = rdbStore.executeSql(SQL_DELETE_TABLE)
promise.then(() => {
  console.info('Delete table done.')
}).catch((err: BusinessError) => {
  console.info("ExecuteSql failed, err: " + err)
})
```

## insert

```TypeScript
insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void
```

Inserts a row of data into a table. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [insert](arkts-arkdata-relationalstore-rdbstore-i.md#insert)

<!--Device-RdbStore-insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void--><!--Device-RdbStore-insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisi";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

rdbStore.insert("EMPLOYEE", valueBucket, (status: number, rowId: number) => {
  if (status) {
    console.log("Insert is failed");
    return;
  }
  console.log("Insert is successful, rowId = " + rowId);
})
```

## insert

```TypeScript
insert(table: string, values: ValuesBucket): Promise<number>
```

Inserts a row of data into a table. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [insert](arkts-arkdata-relationalstore-rdbstore-i.md#insert)

<!--Device-RdbStore-insert(table: string, values: ValuesBucket): Promise<number>--><!--Device-RdbStore-insert(table: string, values: ValuesBucket): Promise<number>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisi";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

let promise: void = rdbStore.insert("EMPLOYEE", valueBucket)
promise.then((rowId: BusinessError) => {
  console.log("Insert is successful, rowId = " + rowId);
}).catch((status: number) => {
  console.log("Insert is failed");
})
```

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void
```

Obtains the distributed table name of a remote device based on the local table name of the device. The distributed table name is required when the RDB store of a remote device is queried. This API uses an asynchronous callback to return the result. > **NOTE：**> The value of **device** can be obtained by &lt;!--RP1--&gt; > [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#getTrustedDeviceListSync) > . &lt;!--RP1End--&gt;The APIs of the **deviceManager** module are system interfaces and available only to system > applications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [obtainDistributedTableName](arkts-arkdata-relationalstore-rdbstore-i.md#obtainDistributedTableName)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void--><!--Device-RdbStore-obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |
| table | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  let deviceId: Array<string> = devices[0].deviceId;
})

rdbStore.obtainDistributedTableName(deviceId, "EMPLOYEE", (err: BusinessError, tableName: String) {
  if (err) {
    console.info('ObtainDistributedTableName failed, err: ' + err)
    return
  }
  console.info('ObtainDistributedTableName successfully, tableName=.' + tableName)
})
```

## obtainDistributedTableName

```TypeScript
obtainDistributedTableName(device: string, table: string): Promise<string>
```

Obtains the distributed table name of a remote device based on the local table name of the device. The distributed table name is required when the RDB store of a remote device is queried. This API uses a promise to return the result. > **NOTE：**> The value of **device** can be obtained by &lt;!--RP1--&gt; > [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#getTrustedDeviceListSync) > . &lt;!--RP1End--&gt;The APIs of the **deviceManager** module are system interfaces and available only to system > applications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [obtainDistributedTableName](arkts-arkdata-relationalstore-rdbstore-i.md#obtainDistributedTableName)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-obtainDistributedTableName(device: string, table: string): Promise<string>--><!--Device-RdbStore-obtainDistributedTableName(device: string, table: string): Promise<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| device | string | Yes |
| table | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## Examples

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  let deviceId: Array<string> = devices[0].deviceId;
})

let promise: void = rdbStore.obtainDistributedTableName(deviceId, "EMPLOYEE")
promise.then((tableName: String) => {
  console.info('ObtainDistributedTableName successfully, tableName= ' + tableName)
}).catch((err: BusinessError) => {
  console.info('ObtainDistributedTableName failed, err: ' + err)
})
```

## off_dataChange

```TypeScript
off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

Unregisters the observer of the specified type from the RDB store. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [off](arkts-arkdata-relationalstore-rdbstore-i.md#off_dataChange)

<!--Device-RdbStore-off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void--><!--Device-RdbStore-off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## Examples

```TypeScript
let devices: Array<string>;

try {
  rdbStore.off('dataChange', data_rdb.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (storeObserver: Array<string>) => {
    for (let i = 0; i < devices.length; i++) {
      console.log('device=' + devices[i] + ' data changed')
    }
  })
} catch (err) {
  console.log('Unregister observer failed')
}
```

## on_dataChange

```TypeScript
on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void
```

Registers an observer for this RDB store. When the data in the RDB store changes, a callback is invoked to return the data changes.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-arkdata-relationalstore-rdbstore-i.md#on_dataChange)

<!--Device-RdbStore-on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void--><!--Device-RdbStore-on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## Examples

```TypeScript
let devices: Array<string>;

try {
  rdbStore.on('dataChange', data_rdb.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (storeObserver: Array<string>) => {
    for (let i = 0; i < devices.length; i++) {
      console.log('device=' + devices[i] + ' data changed')
    }
  })
} catch (err) {
  console.log('Register observer failed')
}
```

## query

```TypeScript
query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void
```

Queries data from the RDB store based on specified conditions. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [query](arkts-arkdata-relationalstore-rdbstore-i.md#query)

<!--Device-RdbStore-query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose")
rdbStore.query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"], (err: BusinessError, resultSet: void) => {
  if (err) {
    console.info("Query failed, err: " + err)
    return
  }
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
})
```

## query

```TypeScript
query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>
```

Queries data from the RDB store based on specified conditions. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [query](arkts-arkdata-relationalstore-rdbstore-i.md#query)

<!--Device-RdbStore-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>--><!--Device-RdbStore-query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| columns | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

## Examples

```TypeScript
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Rose")
let promise: void = rdbStore.query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"])
promise.then((resultSet: void) => {
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
}).catch((err: BusinessError) => {
  console.info("Query failed, err: " + err)
})
```

## querySql

```TypeScript
querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void
```

Queries data using the specified SQL statement. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)

<!--Device-RdbStore-querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void--><!--Device-RdbStore-querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ResultSet&gt; | Yes |

## Examples

```TypeScript
rdbStore.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = ?", ['sanguo'], (err: BusinessError, resultSet: void) => {
  if (err) {
    console.info("Query failed, err: " + err)
    return
  }
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
})
```

## querySql

```TypeScript
querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>
```

Queries data using the specified SQL statement. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [querySql](arkts-arkdata-relationalstore-rdbstore-i.md#querySql)

<!--Device-RdbStore-querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>--><!--Device-RdbStore-querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sql | string | Yes |
| bindArgs | Array & lt;ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultSet & gt; |

## Examples

```TypeScript
let promise: void = rdbStore.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'")
promise.then((resultSet: void) => {
  console.log("ResultSet column names: " + resultSet.columnNames)
  console.log("ResultSet column count: " + resultSet.columnCount)
}).catch((err: BusinessError) => {
  console.info("Query failed, err: " + err)
})
```

## rollBack

```TypeScript
rollBack(): void
```

Rolls back the SQL statements that have been executed.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** rollBack

<!--Device-RdbStore-rollBack(): void--><!--Device-RdbStore-rollBack(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';
import featureAbility from '@ohos.ability.featureAbility';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "blobType";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};

const STORE_CONFIG = { name: "RdbTest.db"}
data_rdb.getRdbStore(this,context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
  try {
    rdbStore.beginTransaction()
    await rdbStore.insert("test", valueBucket)
    rdbStore.commit()
  } catch (e) {
    rdbStore.rollBack()
  }
})
```

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void
```

Sets distributed tables. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDistributedTables](arkts-arkdata-relationalstore-rdbstore-i.md#setDistributedTables)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void--><!--Device-RdbStore-setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
rdbStore.setDistributedTables(["EMPLOYEE"], (err: BusinessError) => {
  if (err) {
    console.info('SetDistributedTables failed, err: ' + err)
    return
  }
  console.info('SetDistributedTables successfully.')
})
```

## setDistributedTables

```TypeScript
setDistributedTables(tables: Array<string>): Promise<void>
```

Sets distributed tables. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDistributedTables](arkts-arkdata-relationalstore-rdbstore-i.md#setDistributedTables)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-setDistributedTables(tables: Array<string>): Promise<void>--><!--Device-RdbStore-setDistributedTables(tables: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tables](arkts-arkdata-cloudextension-database-i-sys.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
let promise: void = rdbStore.setDistributedTables(["EMPLOYEE"])
promise.then(() => {
  console.info("SetDistributedTables successfully.")
}).catch((err: BusinessError) => {
  console.info("SetDistributedTables failed, err: " + err)
})
```

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void
```

Synchronizes data across devices. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sync](arkts-arkdata-relationalstore-rdbstore-i.md#sync)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void--><!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | Yes |

## Examples

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    let deviceIds: Array<string> = devices[i].deviceId;
  }
})

let predicates = new data_rdb.RdbPredicates('EMPLOYEE')
predicates.inDevices(deviceIds)
rdbStore.sync(data_rdb.SyncMode.SYNC_MODE_PUSH, predicates, (err: BusinessError, result: void) {
  if (err) {
    console.log('Sync failed, err: ' + err)
    return
  }
  console.log('Sync done.')
  for (let i = 0; i < result.length; i++) {
    console.log('device=' + result[i][0] + ' status=' + result[i][1])
  }
})
```

## sync

```TypeScript
sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>
```

Synchronizes data across devices. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sync](arkts-arkdata-relationalstore-rdbstore-i.md#sync)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>--><!--Device-RdbStore-sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;[string, number] & gt; & gt; |

## Examples

```TypeScript
import deviceManager from '@ohos.distributedHardware.deviceManager';

let dmInstance: Array<string>;

deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
  if (err) {
    console.log("create device manager failed, err=" + err);
    return;
  }
  dmInstance = manager;
  let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    let deviceIds: Array<string> = devices[i].deviceId;
  }
})

let predicates = new data_rdb.RdbPredicates('EMPLOYEE')
predicates.inDevices(deviceIds)
let promise: void = rdbStore.sync(data_rdb.SyncMode.SYNC_MODE_PUSH, predicates)
promise.then((result: void) =>{
  console.log('Sync done.')
  for (let i = 0; i < result.length; i++) {
    console.log('device=' + result[i][0] + ' status=' + result[i][1])
  }
}).catch((err: BusinessError) => {
  console.log('Sync failed')
})
```

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void
```

Updates data in the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [update](arkts-arkdata-relationalstore-rdbstore-i.md#update)

<!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void--><!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
rdbStore.update(valueBucket, predicates, (err: BusinessError, rows: number) => {
  if (err) {
    console.info("Updated failed, err: " + err)
    return
  }
  console.log("Updated row count: " + rows)
})
```

## update

```TypeScript
update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>
```

Updates data based on the specified **RdbPredicates** object. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [update](arkts-arkdata-relationalstore-rdbstore-i.md#update)

<!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>--><!--Device-RdbStore-update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) | Yes |
| predicates | [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { ValuesBucket } from '@ohos.data.ValuesBucket';

let key1 = "NAME";
let key2 = "AGE";
let key3 = "SALARY";
let key4 = "CODES";
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
  key4: value4,
};
let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
predicates.equalTo("NAME", "Lisa")
let promise: void = rdbStore.update(valueBucket, predicates)
promise.then(async (rows: number) => {
  console.log("Updated row count: " + rows)
}).catch((err: BusinessError) => {
  console.info("Updated failed, err: " + err)
})
```
