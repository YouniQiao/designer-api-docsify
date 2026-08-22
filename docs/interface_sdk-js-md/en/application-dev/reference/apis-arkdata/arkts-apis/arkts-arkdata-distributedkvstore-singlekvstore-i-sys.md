# SingleKVStore

Provides APIs for data management in a single KV store, such as adding data, deleting data, and subscribing to data changes or across-device data sync completion events. Before calling any method in **SingleKVStore**, you must use getKVStore to obtain a **SingleKVStore** instance.

**Since:** 23

<!--Device-distributedKVStore-interface SingleKVStore--><!--Device-distributedKVStore-interface SingleKVStore-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## delete

```TypeScript
delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void
```

Deletes the key-value pairs based on the dataSharePredicates.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the dataSharePredicates. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of delete. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.delete(KEY_TEST_STRING_ELEMENT, (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in deleting');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
    console.info(`Succeeded in putting data`);
    if (kvStore != null) {
      kvStore.delete(KEY_TEST_STRING_ELEMENT).then(() => {
        console.info('Succeeded in deleting');
      }).catch((err: BusinessError) => {
        console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

## delete

```TypeScript
delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>
```

Deletes the key-value pairs based on the dataSharePredicates.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>--><!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the dataSharePredicates. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

**Examples**

See [delete](#delete)

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

Obtains the KVStoreResultSet object matching the specified predicate object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the datasharePredicates. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | Yes | {KVStoreResultSet}: the {@code KVStoreResultSet} object matching the specified {@code dataSharePredicates.DataSharePredicates} object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [15100001](../errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) | Over max limits.<br>**Applicable version:** 10 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err :BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing result set');
          });
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing result set');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('localDeviceId', 'batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
    if (err != undefined) {
      console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet, (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in closing resultSet');
      })
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('localDeviceId', 'batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing resultSet');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSet('localDeviceId', query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting resultSet');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing resultSet');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  if (kvStore != null) {
    kvStore.getResultSet('localDeviceId', query).then((result: distributedKVStore.KVStoreResultSet) => {
      console.info('Succeeded in getting resultSet');
      resultSet = result;
      if (kvStore != null) {
        kvStore.closeResultSet(resultSet).then(() => {
          console.info('Succeeded in closing resultSet');
        }).catch((err: BusinessError) => {
          console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
        });
      }
    }).catch((err: BusinessError) => {
      console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
    });
  }
  query.deviceId('localDeviceId');
  console.info("GetResultSet " + query.getSqlLike());

} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting resultSet');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing resultSet');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet`);
}
```

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

Obtains the KVStoreResultSet object matching the specified predicate object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the datasharePredicates. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | {KVStoreResultSet}: the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [15100001](../errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) | Over max limits.<br>**Applicable version:** 10 and later |

**Examples**

See [getResultSet](#getresultset)

## putBatch

```TypeScript
putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void
```

Writes values of ValuesBucket type into the {@code SingleKVStore} database.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | Indicates the ValuesBucket array to be inserted. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of putBatch. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
        }
        console.info('Succeeded in getting Entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    } else {
      console.error('KvStore is null'); // The subsequent sample code is the same as the code here.
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
      }
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting Entries');
        console.info(`PutBatch ${entries}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

## putBatch

```TypeScript
putBatch(value: Array<ValuesBucket>): Promise<void>
```

Writes values of ValuesBucket type into the {@code SingleKVStore} database.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>): Promise<void>--><!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | Indicates the ValuesBucket array to be inserted. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

**Examples**

See [putBatch](#putbatch)

## putValuesBuckets

```TypeScript
putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void
```

Writes values of ValuesBucket type into the {@code SingleKVStore} database.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | Indicates the ValuesBucket array to be inserted. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of putBatch. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) | The WAL file size exceeds the default limit. |

## putValuesBuckets

```TypeScript
putValuesBuckets(value: Array<ValuesBucket>): Promise<void>
```

Writes values of ValuesBucket type into the {@code SingleKVStore} database.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>): Promise<void>--><!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | Indicates the ValuesBucket array to be inserted. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [14800047](../errorcode-data-rdb.md#14800047-wal-file-size-exceeds-the-default-limit) | The WAL file size exceeds the default limit. |

