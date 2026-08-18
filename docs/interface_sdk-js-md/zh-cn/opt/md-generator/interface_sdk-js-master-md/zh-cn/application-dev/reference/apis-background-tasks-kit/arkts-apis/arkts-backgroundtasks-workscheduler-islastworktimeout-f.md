# isLastWorkTimeOut

## 导入模块

```TypeScript
```

## isLastWorkTimeOut

```TypeScript
function isLastWorkTimeOut(workId: number, callback: AsyncCallback<void>): boolean
```

检查延迟任务的最后一次执行是否超时，使用Callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [isLastWorkTimeOut](#islastworktimeout)(workId: int, callback: AsyncCallback&lt;boolean&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function isLastWorkTimeOut(workId: number, callback: AsyncCallback<void>): boolean--><!--Device-workScheduler-function isLastWorkTimeOut(workId: number, callback: AsyncCallback<void>): boolean-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [workId](arkts-backgroundtasks-workscheduler-workinfo-i.md) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |


## isLastWorkTimeOut

```TypeScript
function isLastWorkTimeOut(workId: number, callback: AsyncCallback<boolean>): void
```

检查延迟任务的最后一次执行是否超时，使用Callback异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function isLastWorkTimeOut(workId: int, callback: AsyncCallback<boolean>): void--><!--Device-workScheduler-function isLastWorkTimeOut(workId: int, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [workId](arkts-backgroundtasks-workscheduler-workinfo-i.md) | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { workScheduler } from '@kit.BackgroundTasksKit';

workScheduler.isLastWorkTimeOut(500, (error: BusinessError, res: boolean) => {
  if (error) {
    console.error(`workschedulerLog isLastWorkTimeOut failed. code is ${error.code} message is ${error.message}`);
  } else {
    console.info(`workschedulerLog isLastWorkTimeOut success, data is: ${res}`);
  }
});
```


## isLastWorkTimeOut

```TypeScript
function isLastWorkTimeOut(workId: number): Promise<boolean>
```

检查延迟任务的最后一次执行是否超时，使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-workScheduler-function isLastWorkTimeOut(workId: int): Promise<boolean>--><!--Device-workScheduler-function isLastWorkTimeOut(workId: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [workId](arkts-backgroundtasks-workscheduler-workinfo-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9700001](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { workScheduler } from '@kit.BackgroundTasksKit';

workScheduler.isLastWorkTimeOut(500)
  .then((res: boolean) => {
    console.info(`workschedulerLog isLastWorkTimeOut success, data is: ${res}`);
  })
  .catch((error: BusinessError) => {
    console.error(`workschedulerLog isLastWorkTimeOut failed. code is ${error.code} message is ${error.message}`);
  });
```
