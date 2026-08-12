# updatePrintJobState

## updatePrintJobState

```TypeScript
function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState,
    callback: AsyncCallback<void>): void
```

更新打印任务状态，使用callback异步回调。

**起始版本：** 24

**需要权限：** 
- API版本24+：ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
- API版本10 - 23：ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState,    callback: AsyncCallback<void>): void--><!--Device-print-function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState,    callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| state | [PrintJobState](arkts-basicservices-print-printjobstate-e.md) | 是 |
| subState | [PrintJobSubState](arkts-basicservices-print-printjobsubstate-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// jobId可通过打印扩展能力PrintExtensionAbility的onStartPrintJob回调获得
let jobId : string = 'jobId';
let state : print.PrintJobState = print.PrintJobState.PRINT_JOB_PREPARE;
let subState : print.PrintJobSubState = print.PrintJobSubState.PRINT_JOB_COMPLETED_SUCCESS;
print.updatePrintJobState(jobId, state, subState, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to updatePrintJobState. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('updatePrintJobState success');
    }
})
```


## updatePrintJobState

```TypeScript
function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>
```

更新打印任务状态，使用Promise异步回调。

**起始版本：** 24

**需要权限：** 
- API版本24+：ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
- API版本10 - 23：ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>--><!--Device-print-function updatePrintJobState(jobId: string, state: PrintJobState, subState: PrintJobSubState): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| state | [PrintJobState](arkts-basicservices-print-printjobstate-e.md) | 是 |
| subState | [PrintJobSubState](arkts-basicservices-print-printjobsubstate-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// jobId可通过打印扩展能力PrintExtensionAbility的onStartPrintJob回调获得
let jobId : string = 'jobId';
let state : print.PrintJobState = print.PrintJobState.PRINT_JOB_PREPARE;
let subState : print.PrintJobSubState = print.PrintJobSubState.PRINT_JOB_COMPLETED_SUCCESS;
print.updatePrintJobState(jobId, state, subState).then(() => {
    console.info('update print job state success');
}).catch((error: BusinessError) => {
    console.error(`Failed to updatePrintJobState. Code: ${error.code}, message: ${error.message}`);
})
```
