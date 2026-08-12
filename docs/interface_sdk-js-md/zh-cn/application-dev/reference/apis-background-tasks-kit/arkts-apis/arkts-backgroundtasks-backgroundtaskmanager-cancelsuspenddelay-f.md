# cancelSuspendDelay

## cancelSuspendDelay

```TypeScript
function cancelSuspendDelay(requestId: int): void
```

取消短时任务。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-backgroundTaskManager-function cancelSuspendDelay(requestId: int): void--><!--Device-backgroundTaskManager-function cancelSuspendDelay(requestId: int): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 短时任务的请求ID。通过申请短时任务[requestSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-requestsuspenddelay-f.md#requestSuspendDelay) 接口获取。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameters types; 3. Parameter verification failed. |
| [9800004](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) | System service operation failed. |
| [9800001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-内存操作失败) | Memory operation failed. |
| [9900002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900002-短时任务校验失败) | Transient task verification failed. |
| [9800003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) | Internal transaction failed. |
| [9900001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9900001-短时任务调用方信息校验失败) | Caller information verification failed for a transient task. |
| [9800002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; &lt;br&gt; 2. Failed to apply for memory. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

let requestId = 1;
try {
  backgroundTaskManager.cancelSuspendDelay(requestId);
} catch (error) {
  console.error(`cancelSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

