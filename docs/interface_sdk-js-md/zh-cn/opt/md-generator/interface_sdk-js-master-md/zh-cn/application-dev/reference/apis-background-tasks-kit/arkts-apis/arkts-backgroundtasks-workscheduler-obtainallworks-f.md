# obtainAllWorks

## obtainAllWorks

```TypeScript
function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>
```

获取当前应用所有的延迟任务，使用Callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [workScheduler.obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks)(callback:

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>--><!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;WorkInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |


## obtainAllWorks

```TypeScript
function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void
```

获取当前应用所有的延迟任务，使用Callback异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void--><!--Device-workScheduler-function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;WorkInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { workScheduler } from '@kit.BackgroundTasksKit';

workScheduler.obtainAllWorks((error: BusinessError, res: Array<workScheduler.WorkInfo>) => {
  if (error) {
    console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
  } else {
    console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
  }
});
```


## obtainAllWorks

```TypeScript
function obtainAllWorks(): Promise<Array<WorkInfo>>
```

获取当前应用所有的延迟任务，使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function obtainAllWorks(): Promise<Array<WorkInfo>>--><!--Device-workScheduler-function obtainAllWorks(): Promise<Array<WorkInfo>>-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;WorkInfo&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { workScheduler } from '@kit.BackgroundTasksKit';

workScheduler.obtainAllWorks().then((res: Array<workScheduler.WorkInfo>) => {
  console.info(`workschedulerLog obtainAllWorks success, data is: ${JSON.stringify(res)}`);
}).catch((error: BusinessError) => {
  console.error(`workschedulerLog obtainAllWorks failed. code is ${error.code} message is ${error.message}`);
})
```
