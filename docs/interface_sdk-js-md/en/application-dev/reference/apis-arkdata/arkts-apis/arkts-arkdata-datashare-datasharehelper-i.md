# DataShareHelper

DataShare管理工具实例，可使用此实例访问或管理服务端的数据。在调用DataShareHelper提供的方法前，需要先通过  
[createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f.md#createdatasharehelper)构建一个实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataShareHelper--><!--Device-dataShare-interface DataShareHelper-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## addTemplate

```TypeScript
addTemplate(uri: string, subscriberId: string, template: Template): void
```

添加一个指定订阅者的数据模板。仅支持静默访问。

静默场景下，调用此接口时，传入的uri、subscriberId和template参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-addTemplate(uri: string, subscriberId: string, template: Template): void--><!--Device-DataShareHelper-addTemplate(uri: string, subscriberId: string, template: Template): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要插入的数据的路径。 |
| subscriberId | string | Yes | 要添加模板的订阅者ID，每个订阅者的ID是唯一的。 |
| template | [Template](arkts-arkdata-datashare-template-i.md) | Yes | 要添加的数据模板。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700011 | The URI is not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void
```

将批量数据插入数据库。使用callback异步回调。暂不支持静默访问。

非静默场景下，调用此接口时，传入的values参数的大小不能超过128MB，传入的uri参数大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要插入的数据的路径。 |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | 要插入的数据。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | 回调函数。当将批量数据插入数据库成功，err为undefined，data为获取到的插入的数据记录数；否则为错误对象。&lt;br /&gt;因部分数据库（ 如KVDB）的相应接口并不提供相应支持，故若服务端使用此数据库，则此Promise也无法返回插入的数据记录数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>): Promise<number>
```

ArkTS-Sta:
```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>
```

将批量数据插入数据库。使用Promise异步回调。暂不支持静默访问。

非静默场景下，调用此接口时，传入的values参数的大小不能超过128MB，传入的uri参数大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>--><!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要插入的数据的路径。 |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | 要插入的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象。返回插入的数据记录数。&lt;br /&gt;因部分数据库（如KVDB）的相应接口并不提供相应支持，故若服务端使用此数据库，则此Promise也无法返回插入的数据记录 数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<number>>>
```

ArkTS-Sta:
```TypeScript
batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>
```

批量更新数据库中的数据记录，所有操作的总数(即operations对象的键值对)不得超过4000个，超出限制将导致更新失败；该接口的事务性取决于provider（数据提供方）。使用Promise异步回调。暂不支持静默访问。

非静默场景下，调用此接口时，传入的operations参数的大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>--><!--Device-DataShareHelper-batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operations | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Array&lt;UpdateOperation&gt;&gt; | Yes | 要更新数据的路径、筛选条件和数据集合。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;Record&lt;string, Array&lt;number&gt;&gt;&gt;  <br>ArkTS-Sta：Promise&lt;Record&lt;string, Array&lt;int&gt;&gt;&gt; | Promise used to return an array of updated data records. The value **-1** means the update operation fails. The number of updated data records is not returned if the APIs of the database in use (for example, KVDB) do not support this return. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 15700000 | Inner error. Possible causes: 1.The internal status is abnormal; 2.The interface is incorrectly used; 3.Permission configuration error; 4.A system error. |

## Examples

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

关闭DataShareHelper实例，调用后该实例失效。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-close(): Promise<void>--><!--Device-DataShareHelper-close(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 19 and later |
| 15700000 | Inner error. |

## Examples

```TypeScript
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).close();
}
```

## delTemplate

```TypeScript
delTemplate(uri: string, subscriberId: string): void
```

删除一个指定订阅者的数据模板。仅支持静默访问。

静默场景下，调用此接口时，传入的uri和subscriberId参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-delTemplate(uri: string, subscriberId: string): void--><!--Device-DataShareHelper-delTemplate(uri: string, subscriberId: string): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要删除的数据的路径。 |
| subscriberId | string | Yes | 订阅者ID，每个订阅者的ID是唯一的。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700011 | The URI is not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void
```

从数据库中删除一条或多条数据记录。使用callback异步回调。

非静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要删除的数据的路径。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 筛选条件。&lt;br /&gt;delete接口所支持的谓词方法取决于服务端所选用的数据库，如KVDB的删除 目前仅支持inKeys谓词。静默场景下谓词内方法为空时，默认全表删除。非静默场景下规格由数据提供方制定。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | 回调函数。当从数据库中删除一条或多条数据记录成功，err为undefined，data为获取到的已删除的数据记录数；否则为错误对象。&lt;br /&gt; 因部分数据库（如KVDB）的相应接口并不提供相应支持，故若服务端使用此数据库，则此callback也无法返回删除的数据记录数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

ArkTS-Sta:
```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>
```

从数据库中删除一条或多条数据记录。使用Promise异步回调。

非静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>--><!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要删除的数据的路径。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 筛选条件。&lt;br /&gt;delete接口所支持的谓词方法取决于服务端所选用的数据库，如KVDB的删除 目前仅支持inKeys谓词。静默场景下谓词内方法为空时，默认全表删除。非静默场景下规格由数据提供方制定。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象。返回已删除的数据记录数。&lt;br /&gt;因部分数据库（如KVDB）的相应接口并不提供相应支持，故若服务端使用此数据库，则此Promise也无法返回删除的数据记 录数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

将指定的URI转换为非规范化URI。使用callback异步回调。暂不支持静默访问。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要反规范化的[URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md/arkts-arkts-uri-uri-c.md)。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数。当将指定的URI转换为非规范化URI，err为undefined，data为获取到的反规范化URI（如果反规范化成功，则返回反规 范化的URI；如果无需进行反规范化，则返回原始URI；若不支持则返回空）；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

将指定的URI转换为非规范化URI。使用Promise异步回调。暂不支持静默访问。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-denormalizeUri(uri: string): Promise<string>--><!--Device-DataShareHelper-denormalizeUri(uri: string): Promise<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要反规范化的[URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md/arkts-arkts-uri-uri-c.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。如果反规范化成功，则返回反规范化的URI；如果无需执行任何操作，则返回原始URI；若不支持则返回空。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

获取给定的APP和模板指定的数据。仅支持静默访问。使用callback异步回调。

静默场景下，调用此接口时，传入的bundleName参数的大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void--><!--Device-DataShareHelper-getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示数据所属的APP。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;PublishedItem&gt;&gt; | Yes | 回调函数，返回给定的APP和模板发布的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700012 | The data area does not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

获取给定的APP和模板指定的数据。仅支持静默访问。使用Promise异步回调。

静默场景下，调用此接口时，传入的bundleName参数的大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-getPublishedData(bundleName: string): Promise<Array<PublishedItem>>--><!--Device-DataShareHelper-getPublishedData(bundleName: string): Promise<Array<PublishedItem>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 表示数据所属的APP。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PublishedItem&gt;&gt; | Promise对象，返回给定的APP和模板发布的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700012 | The data area does not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
if (dataShareHelper != undefined) {
  let publishedData: Promise<Array<dataShare.PublishedItem>> = (dataShareHelper as dataShare.DataShareHelper).getPublishedData("com.acts.ohos.data.datasharetest");
}
```

## insert

ArkTS-Dyn:
```TypeScript
insert(uri: string, value: ValuesBucket, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void
```

将单条数据插入数据库。使用callback异步回调。

非静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要插入的数据的路径。 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | 要插入的数据的值。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | 回调函数。当将单条数据插入数据库成功，err为undefined，data为获取到的插入数据记录的索引；否则为错误对象。&lt;br /&gt;因部分数据库 （如KVDB）的相应接口并不支持返回索引，故若服务端使用了不支持索引的数据库，则此callback也无法返回索引值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
insert(uri: string, value: ValuesBucket): Promise<number>
```

ArkTS-Sta:
```TypeScript
insert(uri: string, value: ValuesBucket): Promise<int>
```

将单条数据插入数据库。使用Promise异步回调。

非静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket): Promise<int>--><!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要插入的数据的路径。 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | 要插入的数据的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象。返回插入数据记录的索引。&lt;br /&gt;因部分数据库（如KVDB）的相应接口并不支持返回索引，故若服务端使用了不支持索引的数据库，则此Promise也无法返回 索引值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

将给定的DataShare URI转换为规范化URI，规范化URI可供跨设备使用，DataShare URI仅供本地环境中使用。使用callback异步回调。暂不支持静默访问。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要规范化的[URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md/arkts-arkts-uri-uri-c.md)。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数。当将给定的DataShare URI转换为规范化URI成功，err为undefined，data为获取到的规范化URI（如果支持 URI规范化，则返回规范化URI，否则返回空）；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

将给定的DataShare URI转换为规范化URI，规范化URI可供跨设备使用，DataShare URI仅供本地环境中使用。使用Promise异步回调。暂不支持静默访问。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-normalizeUri(uri: string): Promise<string>--><!--Device-DataShareHelper-normalizeUri(uri: string): Promise<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要规范化的[URI](../../apis-arkts/arkts-apis/arkts-arkts-uri-uri-c.md/arkts-arkts-uri-uri-c.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。如果支持URI规范化，则返回规范化URI，否则返回空。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

通知已注册的观察者指定URI对应的数据资源已发生变更。使用callback异步回调。暂不支持静默访问。

非静默场景下，调用此接口时，传入的uri参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void--><!--Device-DataShareHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当通知已注册的观察者指定URI对应的数据资源已发生变更成功，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Mandatory parameters are left unspecified.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

通知已注册的观察者指定URI对应的数据资源已发生变更。使用Promise异步回调。暂不支持静默访问。

非静默场景下，调用此接口时，传入的uri参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-notifyChange(uri: string): Promise<void>--><!--Device-DataShareHelper-notifyChange(uri: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 表示指定的数据路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Mandatory parameters are left unspecified.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

通知已注册的观察者指定URI对应的数据资源已发生变更类型及变更内容。使用Promise异步回调。暂不支持静默访问。

非静默场景下，调用此接口时，传入的data参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-notifyChange(data: ChangeInfo): Promise<void>--><!--Device-DataShareHelper-notifyChange(data: ChangeInfo): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [ChangeInfo](arkts-arkdata-datashare-changeinfo-i.md) | Yes | 表示数据变更类型、变化的uri、变更的数据内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

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

## off('dataChange')

```TypeScript
off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口  
[on](dataShare.DataShareHelper.on(type: 'dataChange', uri: string, callback: AsyncCallback&lt;void&gt;))相对应。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void--><!--Device-DataShareHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataChange' | Yes | 取消订阅的事件/回调类型，支持的事件为'dataChange'。 |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | 表示指定取消订阅的callback通知，如果为空、为undefined、null，则取消订阅该uri下所有的通知事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

## off

```TypeScript
off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口  
[on](dataShare.DataShareHelper.on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback&lt;ChangeInfo&gt;))相对应。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void--><!--Device-DataShareHelper-off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'dataChange' | Yes | 取消订阅的事件/回调类型，支持的事件为'dataChange'。 |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e.md) | Yes | 表示数据更改时按指定数据路径通知变更。 |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | No | 表示指定取消订阅的callback通知，如果为空、为undefined、null，则取消订阅该uri下所有的通知事件。如果不为空， 传入的callback必须和注册为同一个。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

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

## off('rdbDataChange')

```TypeScript
off(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback?: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

取消订阅指定URI和模板对应的数据变更事件。仅支持静默访问。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback?: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-off(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback?: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'rdbDataChange' | Yes | 取消订阅的事件类型，支持的事件为'rdbDataChange'，表示rdb数据的变更事件。 |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i.md) | Yes | 处理回调的templateId。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RdbDataChangeNode&gt; | No | 回调函数。表示指定取消订阅的callback通知，如果为空、为undefined、null，则取消订阅该uri下所有 的通知事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
let uri = "datashareproxy://com.samples.datasharetest.DataShare";
let templateId:dataShare.TemplateId = {subscriberId:"11", bundleNameOfOwner:"com.acts.ohos.data.datasharetest"};
if (dataShareHelper != undefined) {
  let result: Array<dataShare.OperationResult> = (dataShareHelper as dataShare.DataShareHelper).off("rdbDataChange", [uri], templateId);
}
```

## off('publishedDataChange')

```TypeScript
off(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback?: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

取消订阅已发布数据的数据变更通知。仅支持静默访问。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-off(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback?: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-off(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback?: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'publishedDataChange' | Yes | 取消订阅的事件类型，支持的事件为'publishedDataChange'，表示已发布数据的变更事件。 |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| subscriberId | string | Yes | 指定处理回调的用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PublishedDataChangeNode&gt; | No | 回调函数。表示指定取消订阅的callback通知，如果为空、为undefined、null，则取消订阅该 uri下所有的通知事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

## offDataChange

```TypeScript
offDataChange(uri: string, callback?: Callback<void>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口[onDataChange](dataShare.DataShareHelper.onDataChange(uri: string, callback: Callback&lt;void&gt;))相对应。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offDataChange(uri: string, callback?: Callback<void>): void--><!--Device-DataShareHelper-offDataChange(uri: string, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback to unregister. If this parameter is **undefined**, **null**, or left empty, this API unregisters all callbacks for the specified URI. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## offDataChange

```TypeScript
offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口[onDataChange](dataShare.DataShareHelper.onDataChange(type:SubscriptionType, uri: string, callback:Callback&lt;ChangeInfo&gt;))相对应。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void--><!--Device-DataShareHelper-offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e.md) | Yes | 表示数据更改时按指定数据路径通知变更。 |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeInfo&gt; | No | Callback to unregister. If this parameter is **undefined**, **null**, or left empty, this API unregisters all callbacks for the specified URI. If this parameter is specified, the callback must be the one registered in [on('datachange')](dataShare.DataShareHelper.on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback&lt;ChangeInfo&gt;)) . |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## offPublishedDataChange

```TypeScript
offPublishedDataChange(
       uris: Array<string>,
       subscriberId: string,
       callback?: Callback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

取消订阅已发布数据的数据变更通知。仅支持静默访问。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback?: Callback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-offPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback?: Callback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| subscriberId | string | Yes | 指定处理回调的用户ID。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PublishedDataChangeNode&gt; | No | Callback to unregister. If this parameter is **undefined**, **null**, or left empty, this API unregisters all callbacks for the specified URI. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## offRdbDataChange

```TypeScript
offRdbDataChange(
       uris: Array<string>,
       templateId: TemplateId,
       callback?: Callback<RdbDataChangeNode>
     ): Array<OperationResult>
```

取消订阅指定URI和模板对应的数据变更事件。仅支持静默访问。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-offRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback?: Callback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-offRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback?: Callback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i.md) | Yes | 处理回调的templateId。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RdbDataChangeNode&gt; | No | Callback to unregister. If this parameter is **undefined** , **null**, or left empty, this API unregisters all callbacks for the specified URI. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | : The operation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## on('dataChange')

```TypeScript
on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册了观察者，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知。使用callback异步回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限为51次。

触发通知：非静默场景下，调用[notifyChange](arkts-arkdata-datashare-datasharehelper-i.md#notifychange)方法，就会触发对指定URI订阅者的通知；或者静默场景下，使用指定URI的静默访问修改了数据，也会自动触发通知。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void--><!--Device-DataShareHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'dataChange' | Yes | 订阅的事件/回调类型，支持的事件为'dataChange'，当数据更改时，触发该事件。 |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当有其他用户触发了变更通知时调用，err为undefined；否则不被触发或为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.<br>**Applicable version:** 12 and later |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
let onCallback: () => void = (): void => {
  console.info("**** Observer on callback ****");
}
let uri = "datashare:///com.samples.datasharetest.DataShare";
if (dataShareHelper !== undefined) {
  (dataShareHelper as dataShare.DataShareHelper).on("dataChange", uri, onCallback);
}
```

## on

```TypeScript
on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册变更通知，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知，通知携带数据变更类型、变化的uri、变更的数据内容。使用callback回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限为51次。

触发通知：非静默场景下，调用[notifyChange](arkts-arkdata-datashare-datasharehelper-i.md#notifychange)方法，就会触发对指定URI订阅者的通知；或者静默场景下，使用指定URI的静默访问修改了数据，也会自动触发通知, 但此时callback通知中的changeInfo无效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void--><!--Device-DataShareHelper-on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'dataChange' | Yes | 订阅的事件/回调类型，支持的事件为'dataChange'，当有其他用户触发了变更通知时，触发该事件。 |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e.md) | Yes | 表示数据更改时按指定数据路径通知变更。 |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | Yes | 回调函数。当有其他用户触发了变更通知时会回调该函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

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

## on('rdbDataChange')

```TypeScript
on(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

订阅指定URI和模板对应的数据变更事件。仅支持静默访问。该功能不支持跨用户订阅通知。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-on(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'rdbDataChange' | Yes | 订阅的事件类型，支持的事件为'rdbDataChange'，表示rdb数据的变更事件。type是固定值以外时，接口无响应。 |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i.md) | Yes | 处理回调的templateId。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RdbDataChangeNode&gt; | Yes | 回调函数。当触发变更通知时调用，err为undefined，node为订阅数据变更结果；否则不被触发或为错误对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

## on('publishedDataChange')

```TypeScript
on(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

订阅已发布数据的数据变更通知。仅支持静默访问。该功能不支持跨用户订阅通知。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-on(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-on(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'publishedDataChange' | Yes | 订阅的事件类型，支持的事件为'publishedDataChange'，表示已发布数据的变更事件。 |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| subscriberId | string | Yes | 指定处理回调的用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PublishedDataChangeNode&gt; | Yes | 回调函数。当触发变更通知时调用，err为undefined，node为订阅数据变更结果；否则不被触发或为 错误对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

## onDataChange

```TypeScript
onDataChange(uri: string, callback: Callback<void>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册了观察者，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知。使用callback异步回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限为51次。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onDataChange(uri: string, callback: Callback<void>): void--><!--Device-DataShareHelper-onDataChange(uri: string, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。当有其他用户触发了变更通知时调用；否则不被触发或为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## onDataChange

```TypeScript
onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册变更通知，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知，通知携带数据变更类型、变化的uri、变更的数据内容。使用callback回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限为51次。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void--><!--Device-DataShareHelper-onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e.md) | Yes | 表示数据更改时按指定数据路径通知变更。 |
| uri | string | Yes | 表示指定的数据路径。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeInfo&gt; | Yes | 回调函数。当有其他用户触发了变更通知时会回调该函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## onPublishedDataChange

```TypeScript
onPublishedDataChange(
       uris: Array<string>,
       subscriberId: string,
       callback: Callback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

订阅已发布数据的数据变更通知。仅支持静默访问。该功能不支持跨用户订阅通知。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback: Callback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-onPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback: Callback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| subscriberId | string | Yes | 指定处理回调的用户ID。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PublishedDataChangeNode&gt; | Yes | 回调函数。当触发变更通知时调用，err为undefined， node为订阅数据变更结果；否则不被触发或为错误对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## onRdbDataChange

```TypeScript
onRdbDataChange(
       uris: Array<string>,
       templateId: TemplateId,
       callback: Callback<RdbDataChangeNode>
     ): Array<OperationResult>
```

订阅指定URI和模板对应的数据变更事件。仅支持静默访问。该功能不支持跨用户订阅通知。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-onRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback: Callback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-onRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback: Callback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | Array&lt;string&gt; | Yes | 要操作的数据的路径。 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i.md) | Yes | 处理回调的templateId。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RdbDataChangeNode&gt; | Yes | 回调函数。当触发变更通知时调用，err为undefined，node为订阅数据变更结果；否则不被触发或为错误对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;OperationResult&gt; | 返回操作结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700013 | The DataShareHelper instance is already closed. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## publish

ArkTS-Dyn:
```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       version: number,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

ArkTS-Sta:
```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       version: int,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

发布数据，将数据更新至数据库。需传入要发布的数据版本，当传入版本号高于当前数据库记录的版本时成功。仅支持静默访问。使用callback异步回调。

静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       version: int,       callback: AsyncCallback<Array<OperationResult>>     ): void--><!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       version: int,       callback: AsyncCallback<Array<OperationResult>>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Array&lt;PublishedItem&gt; | Yes | 要发布的数据。 |
| bundleName | string | Yes | 表示要发布数据所属的APP，对发布的私有数据生效，仅该app可以读取数据。 |
| version | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要发布的数据版本，越大表示数据版本越新。如果发布的版本号小于数据库中的记录，则更新失败。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OperationResult&gt;&gt; | Yes | 回调函数。当发布数据时调用，err为undefined，result为发布数据结果；否则不被触发或为错误对 象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700012 | The data area is not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

发布数据，将数据更新至数据库。仅支持静默访问。使用callback异步回调。

静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       callback: AsyncCallback<Array<OperationResult>>     ): void--><!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       callback: AsyncCallback<Array<OperationResult>>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Array&lt;PublishedItem&gt; | Yes | 要发布的数据。 |
| bundleName | string | Yes | 表示要发布数据所属的APP，对发布的私有数据生效，仅该app可以读取数据。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OperationResult&gt;&gt; | Yes | 回调函数。当发布数据时调用，err为undefined，result为发布数据结果；否则不被触发或为错误对 象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700012 | The data area is not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
publish(data: Array<PublishedItem>, bundleName: string, version?: number): Promise<Array<OperationResult>>
```

ArkTS-Sta:
```TypeScript
publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>
```

发布数据，将数据更新至数据库。可以选择传入要发布的数据版本，当传入版本号高于当前数据库记录的版本时成功。仅支持静默访问。使用Promise异步回调。

静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>--><!--Device-DataShareHelper-publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Array&lt;PublishedItem&gt; | Yes | 要发布的数据。 |
| bundleName | string | Yes | 表示要发布数据所属的APP，对发布的私有数据生效，仅该app可以读取数据。 |
| version | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 要发布的数据版本，越大表示数据版本越新。如果发布的版本号小于数据库中的记录，则更新失败。 如果不检查要发布的数据版本，则不填。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;OperationResult&gt;&gt; | 发布数据结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 15700012 | The data area is not exist. |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

查询数据库中的数据。使用callback异步回调。

非静默场景下，调用此接口时，传入的predicates参数的大小不能超过128MB，传入的uri和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri、predicates和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

使用此接口查询数据库数据时，如查询内容达到资源上限，操作将失败并返回错误，用户可根据场景考虑重试。有关于资源上限的详细说明，请参见  
[通过数据管理服务实现数据共享静默访问](../../../database/share-data-by-silent-access-sys.md#约束与限制)和  
[通过DataShareExtensionAbility实现数据共享](../../../database/share-data-by-datashareextensionability-sys.md#约束与限制)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>,       callback: AsyncCallback<DataShareResultSet>     ): void--><!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>,       callback: AsyncCallback<DataShareResultSet>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要查询的数据的路径。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 筛选条件。&lt;br /&gt;query接口所支持的谓词方法取决于服务端所选用的数据库，如KVDB目前仅支 持inKeys和prefixKey。静默场景下谓词内方法为空时，默认全表查询。非静默场景下规格由数据提供方制定。 |
| columns | Array&lt;string&gt; | Yes | 要查询的列。如果此参数为空，则查询所有列。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; | Yes | 回调函数。当查询数据库中的数据成功，err为undefined，data为获取到的查询到的结果集；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

查询数据库中的数据。使用Promise异步回调。

非静默场景下，调用此接口时，传入的predicates参数的大小不能超过128MB，传入的uri和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri、predicates和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

使用此接口查询数据库数据时，如查询内容达到资源上限，操作将失败并返回错误，用户可根据场景考虑重试。有关于资源上限的详细说明，请参见  
[通过数据管理服务实现数据共享静默访问](../../../database/share-data-by-silent-access-sys.md#约束与限制)和  
[通过DataShareExtensionAbility实现数据共享](../../../database/share-data-by-datashareextensionability-sys.md#约束与限制)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>     ): Promise<DataShareResultSet>--><!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>     ): Promise<DataShareResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要查询的数据的路径。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 筛选条件。&lt;br /&gt;query接口所支持的谓词方法取决于服务端所选用的数据库，如KVDB目前仅支 持inKeys和prefixKey。静默场景下谓词内方法为空时，默认全表查询。非静默场景下规格由数据提供方制定。 |
| columns | Array&lt;string&gt; | Yes | 要查询的列。如果此参数为空，则查询所有列。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; | Promise对象。返回查询到的结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
update(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       value: ValuesBucket,
       callback: AsyncCallback<number>
     ): void
```

ArkTS-Sta:
```TypeScript
update(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       value: ValuesBucket,
       callback: AsyncCallback<int>
     ): void
```

更新数据库中的数据记录。使用callback异步回调。

非静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-update(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       value: ValuesBucket,       callback: AsyncCallback<int>     ): void--><!--Device-DataShareHelper-update(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       value: ValuesBucket,       callback: AsyncCallback<int>     ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要更新的数据的路径。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 筛选条件。&lt;br /&gt;update接口是否支持谓词筛选条件取决于服务端所选用的数据库，如KVDB目 前并不支持谓词筛选条件，仅RDB支持。静默场景下谓词内方法为空时，默认全表更新。非静默场景下规格由数据提供方制定。 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | 要更新的数据的值。 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | 回调函数。当更新数据库中的数据记录成功，err为undefined，data为获取到的更新的数据记录数；否则为错误对象。&lt;br /&gt;因部分数据库 （如KVDB）的相应接口并不提供相应支持，故若服务端使用此数据库，则此callback也无法返回更新的数据记录数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

ArkTS-Dyn:
```TypeScript
update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<number>
```

ArkTS-Sta:
```TypeScript
update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>
```

更新数据库中的数据记录。使用Promise异步回调。

非静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。

静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataShareHelper-update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>--><!--Device-DataShareHelper-update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 要更新的数据的路径。 |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 筛选条件。&lt;br /&gt;update接口是否支持谓词筛选条件取决于服务端所选用的数据库，如KVDB目 前并不支持谓词筛选条件，仅RDB支持。静默场景下谓词内方法为空时，默认全表更新。非静默场景下规格由数据提供方制定。 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes | 要更新的数据的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象。返回更新的数据记录数。&lt;br /&gt;因部分数据库（如KVDB）的相应接口并不提供相应支持，故若服务端使用此数据库，则此Promise也无法返回更新的数据记录 数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15700013 | The DataShareHelper instance is already closed.<br>**Applicable version:** 12 and later |
| 202 | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 and later |

## Examples

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

