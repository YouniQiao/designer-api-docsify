# DataShareHelper（系统接口）

DataShare管理工具实例，可使用此实例访问或管理服务端的数据。在调用DataShareHelper提供的方法前，需要先通过 [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f-sys.md#createDataShareHelper（系统接口）) 构建一个实例。

**起始版本：** 23

**废弃版本：** -1

<!--Device-dataShare-interface DataShareHelper--><!--Device-dataShare-interface DataShareHelper-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

## addTemplate

```TypeScript
addTemplate(uri: string, subscriberId: string, template: Template): void
```

添加一个指定订阅者的数据模板。仅支持静默访问。 静默场景下，调用此接口时，传入的uri、subscriberId和template参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-addTemplate(uri: string, subscriberId: string, template: Template): void--><!--Device-DataShareHelper-addTemplate(uri: string, subscriberId: string, template: Template): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| subscriberId | string | 是 |
| template | [Template](arkts-arkdata-datashare-template-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

将批量数据插入数据库。使用callback异步回调。暂不支持静默访问。 非静默场景下，调用此接口时，传入的values参数的大小不能超过128MB，传入的uri参数大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

将批量数据插入数据库。使用Promise异步回调。暂不支持静默访问。 非静默场景下，调用此接口时，传入的values参数的大小不能超过128MB，传入的uri参数大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>--><!--Device-DataShareHelper-batchInsert(uri: string, values: Array<ValuesBucket>): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

批量更新数据库中的数据记录，所有操作的总数(即operations对象的键值对)不得超过4000个，超出限制将导致更新失败；该接口的事务性取决于provider（数据提供方）。使用Promise异步回调。暂不支持静默访问。 非静默场景下，调用此接口时，传入的operations参数的大小不能超过900KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>--><!--Device-DataShareHelper-batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<int>>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operations | Record & lt;string, Array & lt;UpdateOperation & gt; & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Record & lt;string, Array & lt;number & gt; & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |

## 示例

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
      // 遍历data获取每条数据的更新结果， value为更新成功的数据记录数，若小于0，说明该次更新失败
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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-close(): Promise<void>--><!--Device-DataShareHelper-close(): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [15700000](../errorcode-datashare.md#15700000-内部错误) |

## 示例

```TypeScript
if (dataShareHelper != undefined) {
  (dataShareHelper as dataShare.DataShareHelper).close();
}
```

## delTemplate

```TypeScript
delTemplate(uri: string, subscriberId: string): void
```

删除一个指定订阅者的数据模板。仅支持静默访问。 静默场景下，调用此接口时，传入的uri和subscriberId参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-delTemplate(uri: string, subscriberId: string): void--><!--Device-DataShareHelper-delTemplate(uri: string, subscriberId: string): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| subscriberId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700011](../errorcode-datashare.md#15700011-uri不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

从数据库中删除一条或多条数据记录。使用callback异步回调。 非静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

从数据库中删除一条或多条数据记录。使用Promise异步回调。 非静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri和predicates参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>--><!--Device-DataShareHelper-delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareHelper-denormalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-denormalizeUri(uri: string): Promise<string>--><!--Device-DataShareHelper-denormalizeUri(uri: string): Promise<string>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

获取给定的APP和模板指定的数据。仅支持静默访问。使用callback异步回调。 静默场景下，调用此接口时，传入的bundleName参数的大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void--><!--Device-DataShareHelper-getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

获取给定的APP和模板指定的数据。仅支持静默访问。使用Promise异步回调。 静默场景下，调用此接口时，传入的bundleName参数的大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-getPublishedData(bundleName: string): Promise<Array<PublishedItem>>--><!--Device-DataShareHelper-getPublishedData(bundleName: string): Promise<Array<PublishedItem>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
if (dataShareHelper != undefined) {
  let publishedData: Promise<Array<dataShare.PublishedItem>> = (dataShareHelper as dataShare.DataShareHelper).getPublishedData("com.acts.ohos.data.datasharetest");
}
```

## insert

```TypeScript
insert(uri: string, value: ValuesBucket, callback: AsyncCallback<number>): void
```

将单条数据插入数据库。使用callback异步回调。 非静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void--><!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

将单条数据插入数据库。使用Promise异步回调。 非静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket): Promise<int>--><!--Device-DataShareHelper-insert(uri: string, value: ValuesBucket): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void--><!--Device-DataShareHelper-normalizeUri(uri: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-normalizeUri(uri: string): Promise<string>--><!--Device-DataShareHelper-normalizeUri(uri: string): Promise<string>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

通知已注册的观察者指定URI对应的数据资源已发生变更。使用callback异步回调。暂不支持静默访问。 非静默场景下，调用此接口时，传入的uri参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void--><!--Device-DataShareHelper-notifyChange(uri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

通知已注册的观察者指定URI对应的数据资源已发生变更。使用Promise异步回调。暂不支持静默访问。 非静默场景下，调用此接口时，传入的uri参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-notifyChange(uri: string): Promise<void>--><!--Device-DataShareHelper-notifyChange(uri: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

通知已注册的观察者指定URI对应的数据资源已发生变更类型及变更内容。使用Promise异步回调。暂不支持静默访问。 非静默场景下，调用此接口时，传入的data参数大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-notifyChange(data: ChangeInfo): Promise<void>--><!--Device-DataShareHelper-notifyChange(data: ChangeInfo): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [ChangeInfo](arkts-arkdata-relationalstore-changeinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

取消订阅指定URI下指定callback对应的数据资源的变更通知。 与订阅接口[onDataChange](#on_dataChange)相对应。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-offDataChange(uri: string, callback?: Callback<void>): void--><!--Device-DataShareHelper-offDataChange(uri: string, callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offDataChange

```TypeScript
offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。 与订阅接口[onDataChange](#on_dataChange)相对应。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void--><!--Device-DataShareHelper-offDataChange(type:SubscriptionType, uri: string, callback?: Callback<ChangeInfo>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | 是 |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offPublishedDataChange

```TypeScript
offPublishedDataChange(
       uris: Array<string>,
       subscriberId: string,
       callback?: Callback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

取消订阅已发布数据的数据变更通知。仅支持静默访问。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-offPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback?: Callback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-offPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback?: Callback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array & lt;string & gt; | 是 |
| subscriberId | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offRdbDataChange

```TypeScript
offRdbDataChange(
       uris: Array<string>,
       templateId: TemplateId,
       callback?: Callback<RdbDataChangeNode>
     ): Array<OperationResult>
```

取消订阅指定URI和模板对应的数据变更事件。仅支持静默访问。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-offRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback?: Callback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-offRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback?: Callback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array & lt;string & gt; | 是 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## off_dataChange

```TypeScript
off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void
```

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口 [on](#on_dataChange)相对应。

**起始版本：** 9

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void--><!--Device-DataShareHelper-off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

取消订阅指定URI下指定callback对应的数据资源的变更通知。与订阅接口 [on](#on_dataChange) 相对应。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void--><!--Device-DataShareHelper-off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

取消订阅已发布数据的数据变更通知。仅支持静默访问。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-off(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback?: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-off(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback?: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishedDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| subscriberId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

取消订阅指定URI和模板对应的数据变更事件。仅支持静默访问。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-off(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback?: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-off(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback?: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rdbDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

订阅指定URI对应数据的数据变更事件。若订阅者已注册了观察者，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知。使用callback异步回调。 该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限为51次。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-onDataChange(uri: string, callback: Callback<void>): void--><!--Device-DataShareHelper-onDataChange(uri: string, callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onDataChange

```TypeScript
onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册变更通知，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知， 通知携带数据变更类型、变化的uri、变更的数据内容。使用callback回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限为51次。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void--><!--Device-DataShareHelper-onDataChange(type:SubscriptionType, uri: string, callback: Callback<ChangeInfo>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | 是 |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onPublishedDataChange

```TypeScript
onPublishedDataChange(
       uris: Array<string>,
       subscriberId: string,
       callback: Callback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

订阅已发布数据的数据变更通知。仅支持静默访问。该功能不支持跨用户订阅通知。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-onPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback: Callback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-onPublishedDataChange(       uris: Array<string>,       subscriberId: string,       callback: Callback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array & lt;string & gt; | 是 |
| subscriberId | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onRdbDataChange

```TypeScript
onRdbDataChange(
       uris: Array<string>,
       templateId: TemplateId,
       callback: Callback<RdbDataChangeNode>
     ): Array<OperationResult>
```

订阅指定URI和模板对应的数据变更事件。仅支持静默访问。该功能不支持跨用户订阅通知。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-onRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback: Callback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-onRdbDataChange(       uris: Array<string>,       templateId: TemplateId,       callback: Callback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | Array & lt;string & gt; | 是 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on_dataChange

```TypeScript
on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void
```

订阅指定URI对应数据的数据变更事件。若订阅者已注册了观察者，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知。使用callback异步回调。该功能不支持跨用户订阅通知。同一应用内对单个URI的重复订阅上限 为51次。 触发通知：非静默场景下，调用[notifyChange](#notifyChange)方法，就会触发对指定URI订阅者的通知；或者静默场景 下，使用指定URI的静默访问修改了数据，也会自动触发通知。

**起始版本：** 9

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void--><!--Device-DataShareHelper-on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'dataChange' | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

订阅指定URI对应数据的数据变更事件。若订阅者已注册变更通知，当有其他通知者触发了变更通知时，订阅者将会接收到callback通知，通知携带数据变更类型、变化的uri、变更的数据内容。使用callback回调。该功能不支持跨用 户订阅通知。同一应用内对单个URI的重复订阅上限为51次。 触发通知：非静默场景下，调用[notifyChange](#notifyChange)方法，就会触发对指定URI订阅者的通知；或 者静默场景下，使用指定URI的静默访问修改了数据，也会自动触发通知, 但此时callback通知中的changeInfo无效。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void--><!--Device-DataShareHelper-on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'dataChange' | 是 |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | 是 |
| uri | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

订阅已发布数据的数据变更通知。仅支持静默访问。该功能不支持跨用户订阅通知。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-on(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-on(       type: 'publishedDataChange',       uris: Array<string>,       subscriberId: string,       callback: AsyncCallback<PublishedDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'publishedDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| subscriberId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

订阅指定URI和模板对应的数据变更事件。仅支持静默访问。该功能不支持跨用户订阅通知。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-on(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>--><!--Device-DataShareHelper-on(       type: 'rdbDataChange',       uris: Array<string>,       templateId: TemplateId,       callback: AsyncCallback<RdbDataChangeNode>     ): Array<OperationResult>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'rdbDataChange' | 是 |
| uris | Array & lt;string & gt; | 是 |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

发布数据，将数据更新至数据库。需传入要发布的数据版本，当传入版本号高于当前数据库记录的版本时成功。仅支持静默访问。使用callback异步回调。 静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       version: int,       callback: AsyncCallback<Array<OperationResult>>     ): void--><!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       version: int,       callback: AsyncCallback<Array<OperationResult>>     ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | 是 |
| bundleName | string | 是 |
| version | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

发布数据，将数据更新至数据库。仅支持静默访问。使用callback异步回调。 静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       callback: AsyncCallback<Array<OperationResult>>     ): void--><!--Device-DataShareHelper-publish(       data: Array<PublishedItem>,       bundleName: string,       callback: AsyncCallback<Array<OperationResult>>     ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

发布数据，将数据更新至数据库。可以选择传入要发布的数据版本，当传入版本号高于当前数据库记录的版本时成功。仅支持静默访问。使用Promise异步回调。 静默场景下，调用此接口时，传入的data和bundleName参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>--><!--Device-DataShareHelper-publish(data: Array<PublishedItem>, bundleName: string, version?: int): Promise<Array<OperationResult>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | 是 |
| bundleName | string | 是 |
| version | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [15700012](../errorcode-datashare.md#15700012-数据区不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

查询数据库中的数据。使用callback异步回调。 非静默场景下，调用此接口时，传入的predicates参数的大小不能超过128MB，传入的uri和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri、predicates和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。 使用此接口查询数据库数据时，如查询内容达到资源上限，操作将失败并返回错误，用户可根据场景考虑重试。有关于资源上限的详细说明，请参见 [通过数据管理服务实现数据共享静默访问](../../../database/share-data-by-silent-access-sys.md#约束与限制)和 [通过DataShareExtensionAbility实现数据共享](../../../database/share-data-by-datashareextensionability-sys.md#约束与限制)。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>,       callback: AsyncCallback<DataShareResultSet>     ): void--><!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>,       callback: AsyncCallback<DataShareResultSet>     ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

查询数据库中的数据。使用Promise异步回调。 非静默场景下，调用此接口时，传入的predicates参数的大小不能超过128MB，传入的uri和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri、predicates和columns参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。 使用此接口查询数据库数据时，如查询内容达到资源上限，操作将失败并返回错误，用户可根据场景考虑重试。有关于资源上限的详细说明，请参见 [通过数据管理服务实现数据共享静默访问](../../../database/share-data-by-silent-access-sys.md#约束与限制)和 [通过DataShareExtensionAbility实现数据共享](../../../database/share-data-by-datashareextensionability-sys.md#约束与限制)。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>     ): Promise<DataShareResultSet>--><!--Device-DataShareHelper-query(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       columns: Array<string>     ): Promise<DataShareResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| columns | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

更新数据库中的数据记录。使用callback异步回调。 非静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-update(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       value: ValuesBucket,       callback: AsyncCallback<int>     ): void--><!--Device-DataShareHelper-update(       uri: string,       predicates: dataSharePredicates.DataSharePredicates,       value: ValuesBucket,       callback: AsyncCallback<int>     ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

更新数据库中的数据记录。使用Promise异步回调。 非静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过900KB，超出限制将导致操作失败或抛出异常。 静默场景下，调用此接口时，传入的uri、predicates和value参数的总大小不能超过200KB，超出限制将导致操作失败或抛出异常。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DataShareHelper-update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>--><!--Device-DataShareHelper-update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<int>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| predicates | dataSharePredicates.DataSharePredicates | 是 |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper实例被关闭) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
