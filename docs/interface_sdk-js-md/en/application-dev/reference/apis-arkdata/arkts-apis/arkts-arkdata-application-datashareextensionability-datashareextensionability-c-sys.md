# DataShareExtensionAbility (System API)

This module provides data sharing and expansion capabilities.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class DataShareExtensionAbility--><!--Device-unnamed-declare class DataShareExtensionAbility-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { DataShareExtensionAbility } from 'DataShareExtensionAbility';
```

## batchInsert

```TypeScript
batchInsert?(uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

Batch inserts data into the database. This API is called by the server and can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-batchInsert?(uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<number>): void--><!--Device-DataShareExtensionAbility-batchInsert?(uri: string, valueBuckets: Array<ValuesBucket>, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the data to insert. |
| valueBuckets | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | Data to insert. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the number of inserted data records. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore, ValuesBucket } from '@kit.ArkData';

let TBL_NAME = 'TBL00';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  batchInsert(uri: string, valueBuckets: Array<ValuesBucket>, callback: Function) {
    if (valueBuckets === null || valueBuckets.length <= 0) {
      console.error('invalid valueBuckets');
      return;
    }
    rdbStore.batchInsert(TBL_NAME, valueBuckets, (err, ret) => {
      if (callback !== undefined) {
        callback(err, ret);
      }
    });
  };
};
```

## batchUpdate

```TypeScript
batchUpdate?(
    operations: Record<string, Array<UpdateOperation>>,
    callback: AsyncCallback<Record<string, Array<number>>>
  ): void
```

Batch updates data into the database. This API is called by the server and can be overridden as required.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-batchUpdate?(    operations: Record<string, Array<UpdateOperation>>,    callback: AsyncCallback<Record<string, Array<number>>>  ): void--><!--Device-DataShareExtensionAbility-batchUpdate?(    operations: Record<string, Array<UpdateOperation>>,    callback: AsyncCallback<Record<string, Array<number>>>  ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operations | Record&lt;string, Array&lt;[UpdateOperation](arkts-arkdata-updateoperation-t-sys.md)&gt;&gt; | Yes | Collection of the path of the data to update, update conditions, and new data. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Record&lt;string, Array&lt;number&gt;&gt;&gt; | Yes | Callback used to return an array of updated data records. The value **-1** means the update operation fails. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore, dataShare } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit'

let TBL_NAME = 'TBL00';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  batchUpdate(operations:Record<string, Array<dataShare.UpdateOperation>>, callback:Function) {
    let recordOps : Record<string, Array<dataShare.UpdateOperation>> = operations;
    let results : Record<string, Array<number>> = {};
    let a = Object.entries(recordOps);
    for (let i = 0; i < a.length; i++) {
      let key = a[i][0];
      let values = a[i][1];
      let result : number[] = [];
      for (const value of values) {
        rdbStore.update(TBL_NAME, value.values, value.predicates).then(async (rows) => {
          console.info('Update row count is ' + rows);
          result.push(rows);
        }).catch((err:BusinessError) => {
          console.info('Update failed, err is ' + JSON.stringify(err));
          result.push(-1)
        })
      }
      results[key] = result;
    }
    callback(null, results);
  }
};
```

## delete

```TypeScript
delete?(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

Deletes data from the database. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-delete?(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void--><!--Device-DataShareExtensionAbility-delete?(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the data to delete. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Filter criteria for deleting data. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the number of deleted data records. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore, dataSharePredicates } from '@kit.ArkData';

let TBL_NAME = 'TBL00';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: Function) {
    if (predicates === null || predicates === undefined) {
      return;
    }
    rdbStore.delete(TBL_NAME, predicates, (err, ret) => {
      if (callback !== undefined) {
        callback(err, ret);
      }
    });
  }
};
```

## denormalizeUri

```TypeScript
denormalizeUri?(uri: string, callback: AsyncCallback<string>): void
```

Denormalizes a URI. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-denormalizeUri?(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareExtensionAbility-denormalizeUri?(uri: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | [URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md#URI) to denormalize. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, the denormalized URI is returned. If the URI passed in is returned, denormalization is not required. If denormalization is not supported, **null** is returned. |

## Examples

```TypeScript
import { DataShareExtensionAbility } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit'

export default class DataShareExtAbility extends DataShareExtensionAbility {
  denormalizeUri(uri: string, callback: Function) {
    let key = 'code';
    let value = 0;
    let err: BusinessError = {
      code: value,
      name: key,
      message: key
    };
      let ret = `denormalize ${uri}`;
      callback(err, ret);
  }
};
```

## insert

```TypeScript
insert?(uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<number>): void
```

Inserts data into the database. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-insert?(uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<number>): void--><!--Device-DataShareExtensionAbility-insert?(uri: string, valueBucket: ValuesBucket, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the data to insert. |
| valueBucket | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | Data to insert. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the index of the inserted data record. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore, ValuesBucket } from '@kit.ArkData';

let TBL_NAME = 'TBL00';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  insert(uri: string, valueBucket: ValuesBucket, callback: Function) {
    if (valueBucket === null) {
      console.error('invalid valueBuckets');
      return;
    }
    rdbStore.insert(TBL_NAME, valueBucket, (err, ret) => {
      console.info(`callback ret: ${ret}`);
      if (callback !== undefined) {
        callback(err, ret);
      }
    });
  }
};
```

## normalizeUri

```TypeScript
normalizeUri?(uri: string, callback: AsyncCallback<string>): void
```

Normalizes a URI. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-normalizeUri?(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareExtensionAbility-normalizeUri?(uri: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | [URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md#URI) to normalize. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, the normalized URI is returned. Otherwise, **null** is returned. |

## Examples

```TypeScript
import { DataShareExtensionAbility } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit'

export default class DataShareExtAbility extends DataShareExtensionAbility {
  normalizeUri(uri: string, callback: Function) {
    let key = 'code';
    let value = 0;
    let err: BusinessError = {
      code: value,
      name: key,
      message: key
    };
    let ret: string = `normalize: ${uri}`;
    callback(err, ret);
  }
};
```

## onCreate

```TypeScript
onCreate?(want: Want, callback: AsyncCallback<void>): void
```

Called by the server to initialize service logic when the DataShare client connects to the DataShareExtensionAbility server. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-onCreate?(want: Want, callback: AsyncCallback<void>): void--><!--Device-DataShareExtensionAbility-onCreate?(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want information, including the ability name and bundle name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback that returns no value. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore } from '@kit.ArkData';
import { Want } from '@kit.AbilityKit';

let DB_NAME = 'DB00.db';
let TBL_NAME = 'TBL00';
let DDL_TBL_CREATE = 'CREATE TABLE IF NOT EXISTS '
  + TBL_NAME
  + ' (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, phoneNumber DOUBLE, isStudent BOOLEAN, Binary BINARY)';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  onCreate(want: Want, callback: Function) {
    relationalStore.getRdbStore(this.context, {
      name: DB_NAME,
      securityLevel: relationalStore.SecurityLevel.S3
    }, (err, data) => {
      console.info(`getRdbStore done, data : ${data}`);
      rdbStore = data;
      rdbStore.executeSql(DDL_TBL_CREATE, [], (err) => {
        console.error(`executeSql done, error message : ${err}`);
      });
      if (callback) {
        callback();
      }
    });
  }
};
```

## query

```TypeScript
query?(
    uri: string,
    predicates: dataSharePredicates.DataSharePredicates,
    columns: Array<string>,
    callback: AsyncCallback<Object>
  ): void
```

Queries data from the database. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-query?(    uri: string,    predicates: dataSharePredicates.DataSharePredicates,    columns: Array<string>,    callback: AsyncCallback<Object>  ): void--><!--Device-DataShareExtensionAbility-query?(    uri: string,    predicates: dataSharePredicates.DataSharePredicates,    columns: Array<string>,    callback: AsyncCallback<Object>  ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the data to query. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Filter criteria for querying data. |
| columns | Array&lt;string&gt; | Yes | Columns to query. If this parameter is empty, all columns will be queried. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Object&gt; | Yes | Callback used to return the result set obtained. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore, dataSharePredicates } from '@kit.ArkData';

let TBL_NAME = 'TBL00';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  query(uri: string, predicates: dataSharePredicates.DataSharePredicates, columns: Array<string>, callback: Function) {
    if (predicates === null || predicates === undefined) {
      return;
    }
    rdbStore.query(TBL_NAME, predicates, columns, (err, resultSet) => {
      if (resultSet !== undefined) {
        console.info(`resultSet.rowCount: ${resultSet.rowCount}`);
      }
      if (callback !== undefined) {
        callback(err, resultSet);
      }
    });
  }
};
```

## update

```TypeScript
update?(
    uri: string,
    predicates: dataSharePredicates.DataSharePredicates,
    valueBucket: ValuesBucket,
    callback: AsyncCallback<number>
  ): void
```

Updates data in the database. This API can be overridden as required.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-update?(    uri: string,    predicates: dataSharePredicates.DataSharePredicates,    valueBucket: ValuesBucket,    callback: AsyncCallback<number>  ): void--><!--Device-DataShareExtensionAbility-update?(    uri: string,    predicates: dataSharePredicates.DataSharePredicates,    valueBucket: ValuesBucket,    callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the data to update. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Filter criteria for updating data. |
| valueBucket | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | New data. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the number of data records updated. |

## Examples

```TypeScript
import { DataShareExtensionAbility, relationalStore, dataSharePredicates, ValuesBucket } from '@kit.ArkData';

let TBL_NAME = 'TBL00';
let rdbStore: relationalStore.RdbStore;

export default class DataShareExtAbility extends DataShareExtensionAbility {
  update(uri: string, predicates: dataSharePredicates.DataSharePredicates, valueBucket: ValuesBucket, callback: Function) {
    if (predicates === null || predicates === undefined) {
      return;
    }
    rdbStore.update(TBL_NAME, valueBucket, predicates, (err, ret) => {
      if (callback !== undefined) {
        callback(err, ret);
      }
    });
  }
};
```

## batchInsert

```TypeScript
batchInsert?: BatchInsertFn
```

Inserts multiple data records into the database. This method should be implemented by a data share.

**Type:** [BatchInsertFn](arkts-arkdata-batchinsertfn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-batchInsert?: BatchInsertFn--><!--Device-DataShareExtensionAbility-batchInsert?: BatchInsertFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## batchUpdate

```TypeScript
batchUpdate?: BatchUpdateFn
```

Updates multiple data records in the database. This method should be implemented by a data share.

**Type:** [BatchUpdateFn](arkts-arkdata-batchupdatefn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-batchUpdate?: BatchUpdateFn--><!--Device-DataShareExtensionAbility-batchUpdate?: BatchUpdateFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## context

```TypeScript
context: ExtensionContext
```

Context of the DataShare ExtensionAbility.

**Type:** [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-context: ExtensionContext--><!--Device-DataShareExtensionAbility-context: ExtensionContext-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## delete

```TypeScript
delete?: DeleteFn
```

Deletes one or more data records. This method should be implemented by a data share.

**Type:** [DeleteFn](arkts-arkdata-deletefn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-delete?: DeleteFn--><!--Device-DataShareExtensionAbility-delete?: DeleteFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## denormalizeUri

```TypeScript
denormalizeUri?: DenormalizeUriFn
```

Converts the given normalized {@code uri} generated by normalizeUri into a denormalized one. The default implementation of this method returns the original uri passed to it.

**Type:** [DenormalizeUriFn](arkts-arkdata-denormalizeurifn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-denormalizeUri?: DenormalizeUriFn--><!--Device-DataShareExtensionAbility-denormalizeUri?: DenormalizeUriFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## insert

```TypeScript
insert?: InsertFn
```

Inserts a data record into the database. This method should be implemented by a data share.

**Type:** [InsertFn](arkts-arkdata-insertfn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-insert?: InsertFn--><!--Device-DataShareExtensionAbility-insert?: InsertFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## normalizeUri

```TypeScript
normalizeUri?: NormalizeUriFn
```

Converts the given {@code uri} that refer to the data share into a normalized URI. A normalized URI can be used across devices, persisted, backed up, and restored. It can refer to the same item in the data share even if the context has changed.

**Type:** [NormalizeUriFn](arkts-arkdata-normalizeurifn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-normalizeUri?: NormalizeUriFn--><!--Device-DataShareExtensionAbility-normalizeUri?: NormalizeUriFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## onCreate

```TypeScript
onCreate?: OnCreateFn
```

Called back when a datashare extension ability is started for initialization.

**Type:** [OnCreateFn](arkts-arkdata-oncreatefn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-onCreate?: OnCreateFn--><!--Device-DataShareExtensionAbility-onCreate?: OnCreateFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## query

```TypeScript
query?: QueryFn
```

Queries one or more data records in the database. This method should be implemented by a data share. Only RDB and distributed KVDB resultsets are supported. The current version does not support custom resultsets.

**Type:** [QueryFn](arkts-arkdata-queryfn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-query?: QueryFn--><!--Device-DataShareExtensionAbility-query?: QueryFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

## update

```TypeScript
update?: UpdateFn
```

Updates one or more data records in the database. This method should be implemented by a data share.

**Type:** [UpdateFn](arkts-arkdata-updatefn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareExtensionAbility-update?: UpdateFn--><!--Device-DataShareExtensionAbility-update?: UpdateFn-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

