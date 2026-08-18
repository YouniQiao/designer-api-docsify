# DataShareHelper (System API)

Provides a **DataShareHelper** instance to access or manage data on the server. Before calling an API provided by **DataShareHelper**, you must create a **DataShareHelper** instance using [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f-sys.md#createdatasharehelper-system-api) .

**Since:** 23

<!--Device-dataShare-interface DataShareHelper--><!--Device-dataShare-interface DataShareHelper-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## addTemplate

```TypeScript
addTemplate(uri: string, subscriberId: string, template: Template): void
```

Adds a data template with the specified subscriber. Only silent access is supported. In silent scenarios, the total size of the **uri**, **subscriberId**, and **template** parameters passed in this API cannot exceed 200 KB. If the size exceeds the limit, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-addTemplate(uri: string, subscriberId: string, template: Template): void--><!--Device-DataShareHelper-addTemplate(uri: string, subscriberId: string, template: Template): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| subscriberId | string | Yes |
| template | [Template](arkts-arkdata-datashare-template-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let uri = "datashareproxy://com.samples.datasharetest.DataShare";
let subscriberId = '11';
let key1: string = "p1";
let value1: string = "select cityColumn as city_1, visitedColumn as visited_1 from citys where like = true";
let key2: string = "p2";
let value2: string = "select cityColumn as city_2, visitedColumn as visited_2 from citys where like = false";
let template: dataShare.Template = {
  predicates : {
    key1 : value1,
    key2 : value2,
  },
  scheduler : "select remindTimer(time) from TBL00",
  update : "update TBL00 set cityColumn = 'visited' where cityColumn = 'someCity'"
};
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).addTemplate(uri, subscriberId, template);
}
```

## batchInsert

```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

Batch inserts data into the database. This API uses an asynchronous callback to return the result. Silent access is not supported currently. In non-silent scenarios, the size of the **values** parameter and the **uri** parameter passed in this API cannot exceed 128 MB and 900 KB, respectively. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let vbs: ValuesBucket[] = [
  { "name": "roe11", "age": 21, "salary": 20.5 }
]

try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).batchInsert(uri, vbs, (err, data) => {
      if (err !== undefined) {
        console.error(`Failed to batch insert. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info("batchInsert succeed, data : " + data);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to batch insert. Code: ${code}, message: ${message}`);
}
```

## batchInsert

```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>): Promise<number>
```

Batch inserts data into the database. This API uses a promise to return the result. Silent access is not supported currently. In non-silent scenarios, the size of the **values** parameter and the **uri** parameter passed in this API cannot exceed 128 MB and 900 KB, respectively. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>--><!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let vbs: ValuesBucket[] = [
  { "name": "roe11", "age": 21, "salary": 20.5 }
]

try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).batchInsert(uri, vbs).then((data: number) => {
      console.info("batchInsert succeed, data : " + data);
    }).catch((err: BusinessError) => {
      console.error(`Failed to batch insert. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to batch insert. Code: ${code}, message: ${message}`);
}
```

## batchUpdate

```TypeScript
batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<number>>>
```

Batch updates data in the database. The total number of objects for operations (that is, KV pairs of the objects) cannot exceed 4000. If the number exceeds 4000, the update will fail. The transaction of this API depends on the data provider. This API uses a promise to return the result. Silent access is not supported currently. In non-silent scenarios, the size of the **operations** parameter passed in this API called cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>--><!--Device-DataShareHelper-batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operations | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Array&lt;UpdateOperation&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Array&lt;number&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |

**Examples**

```TypeScript
import { dataSharePredicates, ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let record: Record<string, Array<dataShare.UpdateOperation>> = {};
let operations1: Array<dataShare.UpdateOperation> = [];
let operations2: Array<dataShare.UpdateOperation> = [];

let pre1: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
pre1.equalTo("name", "ZhangSan");
let vb1: ValuesBucket = {
  "name": "ZhangSan1",
};
let operation1: dataShare.UpdateOperation = {
  values: vb1,
  predicates: pre1
};
operations1.push(operation1);

let pre2: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
pre2.equalTo("name", "ZhangSan2");
let vb2: ValuesBucket = {
  "name": "ZhangSan3",
};
let operation2: dataShare.UpdateOperation = {
  values: vb2,
  predicates: pre2
};
operations2.push(operation2);
record["uri1"] = operations1;
record["uri2"] = operations2;

try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).batchUpdate(record).then((data: Record<string, Array<number>>) => {
      // Traverse data to obtain the update result of each data record. value indicates the number of data records that are successfully updated. If value is less than 0, the update fails.
      let a = Object.entries(data);
      for (let i = 0; i < a.length; i++) {
        let key = a[i][0];
        let values = a[i][1];
        console.info(`Update uri:${key}`);
        for (const value of values) {
          console.info(`Update result:${value}`);
        }
      }
    }).catch((err: BusinessError) => {
      console.error(`Failed to batch update. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to batch update. Code: ${code}, message: ${message}`);
}
```

## close

```TypeScript
close(): Promise<void>
```

Closes the **DataShareHelper** instance. After this API is called, the instance becomes invalid. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-close(): Promise<void>--><!--Device-DataShareHelper-close(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |

**Examples**

```TypeScript
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).close();
}
```

## delTemplate

```TypeScript
delTemplate(uri: string, subscriberId: string): void
```

Deletes a data template based on the specified subscriber. Only silent access is supported. In silent scenarios, the total size of the **uri** and **subscriberId** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-delTemplate(uri: string, subscriberId: string): void--><!--Device-DataShareHelper-delTemplate(uri: string, subscriberId: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| subscriberId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let uri = "datashareproxy://com.samples.datasharetest.DataShare";
let subscriberId = '11';
let key1: string = "p1";
let value1: string = "select cityColumn as city_1, visitedColumn as visited_1 from citys where like = true";
let key2: string = "p2";
let value2: string = "select cityColumn as city_2, visitedColumn as visited_2 from citys where like = false";
let template: dataShare.Template = {
  predicates : {
    key1 : value1,
    key2 : value2,
  },
  scheduler : "select remindTimer(time) from TBL00"
};
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).addTemplate(uri, subscriberId, template);
  (dataShareHelper as dataShare.DataShareHelper).delTemplate(uri, subscriberId);
}
```

## delete

```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

Deletes one or more data records from the database. This API uses an asynchronous callback to return the result. In non-silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).delete(uri, da, (err: BusinessError, data: number) => {
      if (err !== undefined) {
        console.error(`Failed to delete. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info("delete succeed, data : " + data);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to delete. Code: ${code}, message: ${message}`);
}
```

## delete

```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

Deletes one or more data records from the database. This API uses a promise to return the result. In non-silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>--><!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).delete(uri, da).then((data: number) => {
      console.info("delete succeed, data : " + data);
    }).catch((err: BusinessError) => {
      console.error(`Failed to delete. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to delete. Code: ${code}, message: ${message}`);
}
```

## denormalizeUri

```TypeScript
denormalizeUri(uri: string, callback: AsyncCallback<string>): void
```

Denormalizes a URI. This API uses an asynchronous callback to return the result. Silent access is not supported currently.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).denormalizeUri(uri, (err: BusinessError, data: string) => {
    if (err !== undefined) {
      console.error(`Failed to denormalize URI. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info("denormalizeUri = " + data);
    }
  });
}
```

## denormalizeUri

```TypeScript
denormalizeUri(uri: string): Promise<string>
```

Denormalizes a URI. This API uses a promise to return the result. Silent access is not supported currently.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-denormalizeUri(uri: string): Promise<string>--><!--Device-DataShareHelper-denormalizeUri(uri: string): Promise<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).denormalizeUri(uri).then((data: string) => {
    console.info("denormalizeUri = " + data);
  }).catch((err: BusinessError) => {
    console.error(`Failed to denormalize URI. Code: ${err.code}, message: ${err.message}`);
  });
}
```

## getPublishedData

```TypeScript
getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void
```

Obtains the published data of an application. Only silent access is supported. This API uses an asynchronous callback to return the result. In silent scenarios, the size of the **bundleName** parameter passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void--><!--Device-DataShareHelper-getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let publishCallback: (err: BusinessError, data: Array<dataShare.PublishedItem>) => void = (err: BusinessError, result: Array<dataShare.PublishedItem>): void => {
  console.info("**** Observer publish callback ****");
};
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).getPublishedData("com.acts.ohos.data.datasharetest", publishCallback);
}
```

## getPublishedData

```TypeScript
getPublishedData(bundleName: string): Promise<Array<PublishedItem>>
```

Obtains the published data of an application. Only silent access is supported. This API uses a promise to return the result. In silent scenarios, the size of the **bundleName** parameter passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-getPublishedData(bundleName: string): Promise<Array<PublishedItem>>--><!--Device-DataShareHelper-getPublishedData(bundleName: string): Promise<Array<PublishedItem>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
if (dataShareHelper != undefined) {
  let publishedData: Promise<Array<dataShare.PublishedItem>> = (dataShareHelper as dataShare.DataShareHelper).getPublishedData("com.acts.ohos.data.datasharetest");
}
```

## insert

```TypeScript
insert(uri: string, value: ValuesBucket, callback: AsyncCallback<number>): void
```

Inserts a single data record into the database. This API uses an asynchronous callback to return the result. In non-silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let key1: string = "name";
let value1: string = "rose";
let key2: string = "age";
let value2: number = 22;
let key3: string = "salary";
let value3: number = 200.5;
const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
};
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).insert(uri, valueBucket, (err: BusinessError, data: number) => {
      if (err !== undefined) {
        console.error(`Failed to insert. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info("insert succeed, data : " + data);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to insert. Code: ${code}, message: ${message}`);
}
```

## insert

```TypeScript
insert(uri: string, value: ValuesBucket): Promise<number>
```

Inserts a single data record into the database. This API uses a promise to return the result. In non-silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket): Promise<int>--><!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { ValuesBucket } from '@kit.ArkData';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let key1: string = "name";
let value1: string = "rose1";
let key2: string = "age";
let value2: number = 21;
let key3: string = "salary";
let value3: number = 20.5;
const valueBucket: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
};
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).insert(uri, valueBucket).then((data: number) => {
      console.info("insert succeed, data : " + data);
    }).catch((err: BusinessError) => {
      console.error(`Failed to insert. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to insert. Code: ${code}, message: ${message}`);
}
```

## normalizeUri

```TypeScript
normalizeUri(uri: string, callback: AsyncCallback<string>): void
```

Normalizes a **DataShare** URI. The **DataShare** URI can be used only by the local device, but the normalized URI can be used across devices. This API uses an asynchronous callback to return the result. Silent access is not supported currently.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).normalizeUri(uri, (err: BusinessError, data: string) => {
    if (err !== undefined) {
      console.info("normalizeUri failed, error message : " + err);
    } else {
      console.info("normalizeUri = " + data);
    }
  });
}
```

## normalizeUri

```TypeScript
normalizeUri(uri: string): Promise<string>
```

Normalizes a **DataShare** URI. The **DataShare** URI can be used only by the local device, but the normalized URI can be used across devices. This API uses a promise to return the result. Silent access is not supported currently.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-normalizeUri(uri: string): Promise<string>--><!--Device-DataShareHelper-normalizeUri(uri: string): Promise<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).normalizeUri(uri).then((data: string) => {
    console.info("normalizeUri = " + data);
  }).catch((err: BusinessError) => {
    console.info("normalizeUri failed, error message : " + err);
  });
}
```

## notifyChange

```TypeScript
notifyChange(uri: string, callback: AsyncCallback<void>): void
```

Notifies the registered observer of data changes. This API uses an asynchronous callback to return the result. Silent access is not supported currently. In non-silent scenarios, the size of the **uri** parameter passed in this API called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void--><!--Device-DataShareHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).notifyChange(uri, () => {
    console.info("***** notifyChange *****");
  });
}
```

## notifyChange

```TypeScript
notifyChange(uri: string): Promise<void>
```

Notifies the registered observer of data changes. This API uses a promise to return the result. Silent access is not supported currently. In non-silent scenarios, the size of the **uri** parameter passed in this API called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-notifyChange(uri: string): Promise<void>--><!--Device-DataShareHelper-notifyChange(uri: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).notifyChange(uri);
}
```

## notifyChange

```TypeScript
notifyChange(data: ChangeInfo): Promise<void>
```

Notifies the observer of the data change of the specified URI. This API uses a promise to return the result. Silent access is not supported currently. In non-silent scenarios, the size of the **data** parameter passed in this API called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-notifyChange(data: ChangeInfo): Promise<void>--><!--Device-DataShareHelper-notifyChange(data: ChangeInfo): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [ChangeInfo](arkts-arkdata-relationalstore-changeinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { ValuesBucket } from '@kit.ArkData';

let dsUri = "datashare:///com.acts.datasharetest";
let people: ValuesBucket[] = [
  { "name": "LiSi" },
  { "name": "WangWu" },
  { "name": "ZhaoLiu" }
]

let changeData:dataShare.ChangeInfo= { type:dataShare.ChangeType.INSERT, uri:dsUri, values:people};
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).notifyChange(changeData);
}
```

## offDataChange

```TypeScript
offDataChange(uri: string, callback?: Callback<void>): void
```

Unsubscribes from the data change of the specified URI. This API corresponds to the [on](#ondatachange) API.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offDataChange(uri: string, callback?: Callback<void>): void--><!--Device-DataShareHelper-offDataChange(uri: string, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offDataChange

```TypeScript
offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void
```

Unsubscribes from the data change of the specified URI. This API corresponds to the [on](#ondatachange) API.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void--><!--Device-DataShareHelper-offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | Yes |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offPublishedDataChange

```TypeScript
offPublishedDataChange(
       uris: Array<string>,
       subscriberId: string,
       callback?: Callback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

Unsubscribes from the change of the published data. Only silent access is supported.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback?: Callback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-offPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback?: Callback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | Array & lt;string & gt; | Yes |
| subscriberId | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## offRdbDataChange

```TypeScript
offRdbDataChange(
       uris: Array<string>,
       templateId: TemplateId,
       callback?: Callback<RdbDataChangeNode>
     ): Array<OperationResult>
```

Unsubscribes from the changes of the data corresponding to the specified URI and template. Only silent access is supported.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback?: Callback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-offRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback?: Callback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | Array & lt;string & gt; | Yes |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_dataChange

```TypeScript
off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void
```

Unsubscribes from the data change of the specified URI. This API corresponds to the [on](#ondatachange) API.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void--><!--Device-DataShareHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataChange' | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let callback: () => void = (): void => {
  console.info("**** Observer on callback ****");
}
let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).on("dataChange", uri, callback);
  (dataShareHelper as dataShare.DataShareHelper).off("dataChange", uri, callback);
}
```

## off_dataChange

```TypeScript
off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void
```

Unsubscribes from the data change of the specified URI. This API corresponds to the [on](#ondatachange) API.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void--><!--Device-DataShareHelper-off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.acts.datasharetest";
export function callback(error:BusinessError, ChangeInfo:dataShare.ChangeInfo) {
    console.info(' **** Observer callback **** ChangeInfo:' + JSON.stringify(ChangeInfo));
}
if (dataShareHelper !== undefined) {
  (dataShareHelper as dataShare.DataShareHelper).on("dataChange", dataShare.SubscriptionType.SUBSCRIPTION_TYPE_EXACT_URI, uri, callback);
  (dataShareHelper as dataShare.DataShareHelper).off("dataChange", dataShare.SubscriptionType.SUBSCRIPTION_TYPE_EXACT_URI, uri, callback);
}
```

## off_publishedDataChange

```TypeScript
off(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback?: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

Unsubscribes from the change of the published data. Only silent access is supported.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback?: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-off(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback?: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishedDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| subscriberId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let offCallback: (err: BusinessError, node: dataShare.PublishedDataChangeNode) => void = (err: BusinessError, node:dataShare.PublishedDataChangeNode): void => {
  console.info("**** Observer off callback ****");
}
let uris:Array<string> = ["city", "datashareproxy://com.acts.ohos.data.datasharetest/appInfo", "key2"];
let subscriberId = '11';
if (dataShareHelper != undefined) {
  let result: Array<dataShare.OperationResult> = (dataShareHelper as dataShare.DataShareHelper).off("publishedDataChange", uris, subscriberId, offCallback);
}
```

## off_rdbDataChange

```TypeScript
off(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback?: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

Unsubscribes from the changes of the data corresponding to the specified URI and template. Only silent access is supported.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback?: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-off(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback?: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rdbDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let uri = "datashareproxy://com.samples.datasharetest.DataShare";
let templateId:dataShare.TemplateId = {subscriberId:"11", bundleNameOfOwner:"com.acts.ohos.data.datasharetest"};
if (dataShareHelper != undefined) {
  let result: Array<dataShare.OperationResult> = (dataShareHelper as dataShare.DataShareHelper).off("rdbDataChange", [uri], templateId);
}
```

## onDataChange

```TypeScript
onDataChange(uri: string, callback: Callback<void>): void
```

Subscribes to the data change of the specified URI. After an observer is registered, the subscriber will receive a notification when the **notifyChange** API is called. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription. An application can subscribe to a single URI for a maximum of 51 times.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onDataChange(uri: string, callback: Callback<void>): void--><!--Device-DataShareHelper-onDataChange(uri: string, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onDataChange

```TypeScript
onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void
```

Subscribes to the data change of the specified URI. After a change notification is registered, the subscriber will receive a notification when the **notifyChange** API is called. The change notification contains the data change type, URI of the data changed, and the changed data. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription. An application can subscribe to a single URI for a maximum of 51 times.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void--><!--Device-DataShareHelper-onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | Yes |
| uri | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onPublishedDataChange

```TypeScript
onPublishedDataChange(
       uris: Array<string>,
       subscriberId: string,
       callback: Callback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

Subscribes to the change of the published data. Only silent access is supported. This function does not support cross-user notification subscription.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback: Callback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-onPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback: Callback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | Array & lt;string & gt; | Yes |
| subscriberId | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## onRdbDataChange

```TypeScript
onRdbDataChange(
       uris: Array<string>,
       templateId: TemplateId,
       callback: Callback<RdbDataChangeNode>
     ): Array<OperationResult>
```

Subscribes to the changes of the data corresponding to the specified URI and template. Only silent access is supported. This function does not support cross-user notification subscription.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback: Callback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-onRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback: Callback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | Array & lt;string & gt; | Yes |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_dataChange

```TypeScript
on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void
```

Subscribes to the data change of the specified URI. After an observer is registered, the subscriber will receive a notification when the **notifyChange** API is called. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription. An application can subscribe to a single URI for a maximum of 51 times. Notification triggering: In non-silent scenarios, a notification is published if the [notifyChange](#notifychange) method is called. In silent scenarios, a notification is automatically published if data is modified via silent access.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void--><!--Device-DataShareHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataChange' | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let onCallback: () => void = (): void => {
  console.info("**** Observer on callback ****");
}
let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper !== undefined) {
  (dataShareHelper as dataShare.DataShareHelper).on("dataChange", uri, onCallback);
}
```

## on_dataChange

```TypeScript
on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void
```

Subscribes to the data change of the specified URI. After a change notification is registered, the subscriber will receive a notification when the **notifyChange** API is called. The change notification contains the data change type, URI of the data changed, and the changed data. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription. An application can subscribe to a single URI for a maximum of 51 times. Notification triggering: In non-silent scenarios, a notification is published if the [notifyChange](#notifychange) method is called. In silent scenarios, a notification is automatically published if data is modified via silent access, but **changeInfo** in the callback is invalid.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void--><!--Device-DataShareHelper-on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.acts.datasharetest";
export function callback(error:BusinessError, ChangeInfo:dataShare.ChangeInfo) {
    console.info(' **** Observer callback **** ChangeInfo:' + JSON.stringify(ChangeInfo));
}
if (dataShareHelper !== undefined) {
  (dataShareHelper as dataShare.DataShareHelper).on('dataChange', dataShare.SubscriptionType.SUBSCRIPTION_TYPE_EXACT_URI, uri, callback);
}
```

## on_publishedDataChange

```TypeScript
on(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

Subscribes to the change of the published data. Only silent access is supported. This function does not support cross-user notification subscription.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-on(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishedDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| subscriberId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onPublishCallback: (err: BusinessError, node: dataShare.PublishedDataChangeNode) => void = (err: BusinessError, node:dataShare.PublishedDataChangeNode): void => {
  console.info("onPublishCallback node bundleName " + JSON.stringify(node.bundleName));
  console.info("onPublishCallback node data size" + node.data.length);
  for (let i = 0; i < node.data.length; i++) {
    console.info("onPublishCallback node " + typeof node.data[i].data);
    if (typeof node.data[i].data != 'string') {
      let array: ArrayBuffer = node.data[i].data as ArrayBuffer;
      let data: Uint8Array = new Uint8Array(array);
      console.info("onPublishCallback " + i + " " + JSON.stringify(data));
    }
    console.info("onPublishCallback data " + i + " " + JSON.stringify(node.data[i]));
  }
}
let uris:Array<string> = ['city', 'datashareproxy://com.acts.ohos.data.datasharetest/appInfo', 'key2'];
let subscriberId = '11';
if (dataShareHelper != undefined) {
  let result: Array<dataShare.OperationResult> = (dataShareHelper as dataShare.DataShareHelper).on('publishedDataChange', uris, subscriberId, onPublishCallback);
}
```

## on_rdbDataChange

```TypeScript
on(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

Subscribes to the changes of the data corresponding to the specified URI and template. Only silent access is supported. This function does not support cross-user notification subscription.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-on(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rdbDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onCallback: (err: BusinessError, node: dataShare.RdbDataChangeNode) => void = (err: BusinessError, node:dataShare.RdbDataChangeNode): void => {
  if (!node.data.length) {
    console.info("node.data is empty");
    return;
  }
  console.info("onCallback " + JSON.stringify(node.uri));
  console.info("onCallback " + JSON.stringify(node.templateId));
  console.info("onCallback " + node.data.length);
  for (let i = 0; i < node.data.length; i++) {
    console.info("onCallback " + typeof node.data[i] + " " + node.data[i]);
  }
}

let uri = "datashareproxy://com.samples.datasharetest.DataShare";
let templateId:dataShare.TemplateId = {subscriberId:"11", bundleNameOfOwner:"com.acts.ohos.data.datasharetest"};
if (dataShareHelper != undefined) {
  let result: Array<dataShare.OperationResult> = (dataShareHelper as dataShare.DataShareHelper).on("rdbDataChange", [uri], templateId, onCallback);
}
```

## publish

```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       version: number,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

Publishes data to the database. You should pass in the version of the data to be published. If the passed version is later than the version recorded in the current database, the operation is successful. Only silent access is supported. This API uses an asynchronous callback to return the result. In silent scenarios, the total size of the **data** and **bundleName** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       version: int,       callback: AsyncCallback<Array<OperationResult>>     ): void--><!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       version: int,       callback: AsyncCallback<Array<OperationResult>>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | Yes |
| bundleName | string | Yes |
| version | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let arrayBuffer = new ArrayBuffer(1);
let version = 1;
let dataArray : Array<dataShare.PublishedItem> = [{key:"key2", subscriberId:"11", data:arrayBuffer}];
let publishCallback: (err: BusinessError, result: Array<dataShare.OperationResult>) => void = (err: BusinessError, result: Array<dataShare.OperationResult>): void => {
  console.info("publishCallback " + JSON.stringify(result));
}
try {
  console.info("dataArray length is:", dataArray.length);
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).publish(dataArray, "com.acts.ohos.data.datasharetest", version, publishCallback);
  }
} catch (e) {
  console.error(`Failed to publish. Code: ${e.code}, message: ${e.message}`);
}
```

## publish

```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

Publishes data to the database. Only silent access is supported. This API uses an asynchronous callback to return the result. In silent scenarios, the total size of the **data** and **bundleName** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       callback: AsyncCallback<Array<OperationResult>>     ): void--><!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       callback: AsyncCallback<Array<OperationResult>>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit'

let publishCallback: (err: BusinessError, result: Array<dataShare.OperationResult>) => void = (err: BusinessError, result: Array<dataShare.OperationResult>): void => {
  console.info("publishCallback " + JSON.stringify(result));
}
let dataArray : Array<dataShare.PublishedItem> = [
  {key:"city", subscriberId:"11", data:"xian"},
  {key:"datashareproxy://com.acts.ohos.data.datasharetest/appInfo", subscriberId:"11", data:"appinfo is just a test app"},
  {key:"empty", subscriberId:"11", data:"nobody sub"}];
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).publish(dataArray, "com.acts.ohos.data.datasharetest", publishCallback);
}
```

## publish

```TypeScript
publish(data: Array<PublishedItem>, bundleName: string, version?: number): Promise<Array<OperationResult>>
```

Publishes data to the database. You should pass in the version of the data to be published. If the passed version is later than the version recorded in the current database, the operation is successful. Only silent access is supported. This API uses a promise to return the result. In silent scenarios, the total size of the **data** and **bundleName** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>--><!--Device-DataShareHelper-publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | Yes |
| bundleName | string | Yes |
| version | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let dataArray: Array<dataShare.PublishedItem> = [
  {key:"city", subscriberId:"11", data:"xian"},
  {key:"datashareproxy://com.acts.ohos.data.datasharetest/appInfo", subscriberId:"11", data:"appinfo is just a test app"},
  {key:"empty", subscriberId:"11", data:"nobody sub"}];
if (dataShareHelper != undefined) {
  let result: Promise<Array<dataShare.OperationResult>> = (dataShareHelper as dataShare.DataShareHelper).publish(dataArray, "com.acts.ohos.data.datasharetest");
}
```

## query

```TypeScript
query(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       columns: Array<string>,
       callback: AsyncCallback<DataShareResultSet>
     ): void
```

Queries data in the database. This API uses an asynchronous callback to return the result. In non-silent scenarios, the size of the **predicates** parameter and the total size of the **uri** and **columns** parameters passed in this API cannot exceed 128 MB and 200 KB, respectively. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri**, **predicates**, and **columns** parameters passed in this API cannot exceed 200 KB. If the size exceeds the limit, the operation fails or an exception is thrown. When this API is used to query database data, if the query content exceeds the resource limit, the operation fails and an error is returned. You can retry the operation based on the scenario. For details about the resource limit, see [Silent Access via DatamgrService](../../../database/share-data-by-silent-access-sys.md#constraints) and [Sharing Data Using DataShareExtensionAbility](../../../database/share-data-by-datashareextensionability-sys.md#constraints) .

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>,       callback: AsyncCallback<DataShareResultSet>     ): void--><!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>,       callback: AsyncCallback<DataShareResultSet>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareResultSet](../../apis-na/arkts-apis/arkts-na-data-datashareresultset-datashareresultset-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { dataSharePredicates, DataShareResultSet } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let columns = ["*"];
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).query(uri, da, columns, (err: BusinessError, data: DataShareResultSet) => {
      if (err !== undefined) {
        console.error(`Failed to query. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info("query succeed, rowCount : " + data.rowCount);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to query. Code: ${code}, message: ${message}`);
}
```

## query

```TypeScript
query(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       columns: Array<string>
     ): Promise<DataShareResultSet>
```

Queries data in the database. This API uses a promise to return the result. In non-silent scenarios, the size of the **predicates** parameter and the total size of the **uri** and **columns** parameters passed in this API cannot exceed 128 MB and 200 KB, respectively. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri**, **predicates**, and **columns** parameters passed in this API cannot exceed 200 KB. If the size exceeds the limit, the operation fails or an exception is thrown. When this API is used to query database data, if the query content exceeds the resource limit, the operation fails and an error is returned. You can retry the operation based on the scenario. For details about the resource limit, see [Silent Access via DatamgrService (ArkTS) (for System Applications Only)](../../../database/share-data-by-silent-access-sys.md#constraints) and [Sharing Data Using DataShareExtensionAbility (ArkTS) (for System Applications Only)](../../../database/share-data-by-datashareextensionability-sys.md#constraints) .

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>     ): Promise<DataShareResultSet>--><!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>     ): Promise<DataShareResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataShareResultSet](../../apis-na/arkts-apis/arkts-na-data-datashareresultset-datashareresultset-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { dataSharePredicates, DataShareResultSet } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let columns = ["*"];
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).query(uri, da, columns).then((data: DataShareResultSet) => {
      console.info("query succeed, rowCount : " + data.rowCount);
    }).catch((err: BusinessError) => {
      console.error(`Failed to query. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to query. Code: ${code}, message: ${message}`);
}
```

## update

```TypeScript
update(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       value: ValuesBucket,
       callback: AsyncCallback<number>
     ): void
```

Updates data in the database. This API uses an asynchronous callback to return the result. In non-silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed when this API is called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-update(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       value: ValuesBucket,       callback: AsyncCallback<int>     ): void--><!--Device-DataShareHelper-update(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       value: ValuesBucket,       callback: AsyncCallback<int>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { dataSharePredicates, ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
let key1: string = "name";
let value1: string = "roe1";
let key2: string = "age";
let value2: number = 21;
let key3: string = "salary";
let value3: number = 20.5;
const va: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
};
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).update(uri, da, va, (err: BusinessError, data: number) => {
      if (err !== undefined) {
        console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info("update succeed, data : " + data);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to update. Code: ${code}, message: ${message}`);
}
```

## update

```TypeScript
update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<number>
```

Updates data in the database. This API uses a promise to return the result. In non-silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown. In silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed when this API is called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>--><!--Device-DataShareHelper-update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { dataSharePredicates, ValuesBucket } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "datashare:///com.samples.datasharetest.DataShare";
let da = new dataSharePredicates.DataSharePredicates();
da.equalTo("name", "ZhangSan");
let key1: string = "name";
let value1: string = "roe1";
let key2: string = "age";
let value2: number = 21;
let key3: string = "salary";
let value3: number = 20.5;
const va: ValuesBucket = {
  key1: value1,
  key2: value2,
  key3: value3,
};
try {
  if (dataShareHelper != undefined) {
    (dataShareHelper as dataShare.DataShareHelper).update(uri, da, va).then((data: number) => {
      console.info("update succeed, data : " + data);
    }).catch((err: BusinessError) => {
      console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
    });
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Failed to update. Code: ${code}, message: ${message}`);
}
```
