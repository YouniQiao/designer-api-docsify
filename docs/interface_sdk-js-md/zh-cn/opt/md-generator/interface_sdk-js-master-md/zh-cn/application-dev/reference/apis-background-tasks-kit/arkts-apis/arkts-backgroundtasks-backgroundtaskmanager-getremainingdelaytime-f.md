# getRemainingDelayTime

## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void
```

获取本次短时任务的剩余时间，使用callback异步回调。

**起始版本：** 9

<!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int, callback: AsyncCallback<int>): void--><!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [9800004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9900002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-短时任务校验失败) |
| [9800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) |
| [9800002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

// 短时任务的请求ID，用于查询剩余时间
let requestId = 1;
backgroundTaskManager.getRemainingDelayTime(requestId, (error: BusinessError, res: number) => {
  if(error) {
    console.error(`callback => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
  } else {
    console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
  }
})
```


## getRemainingDelayTime

```TypeScript
function getRemainingDelayTime(requestId: number): Promise<number>
```

获取本次短时任务的剩余时间，使用Promise异步回调。

**起始版本：** 9

<!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int): Promise<int>--><!--Device-backgroundTaskManager-function getRemainingDelayTime(requestId: int): Promise<int>-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| requestId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [9800004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9900002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-短时任务校验失败) |
| [9800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) |
| [9800002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let requestId = 1;
backgroundTaskManager.getRemainingDelayTime(requestId).then((res: number) => {
  console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
}).catch((error: BusinessError) => {
  console.error(`promise => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
})
```
