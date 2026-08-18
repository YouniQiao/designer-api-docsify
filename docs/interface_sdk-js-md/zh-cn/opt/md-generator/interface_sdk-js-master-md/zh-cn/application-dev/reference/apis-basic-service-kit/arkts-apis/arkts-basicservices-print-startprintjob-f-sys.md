# startPrintJob（系统接口）

## 导入模块

```TypeScript
```

## startPrintJob

```TypeScript
function startPrintJob(jobInfo: PrintJob, callback: AsyncCallback<void>): void
```

开始打印任务，使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function startPrintJob(jobInfo: PrintJob, callback: AsyncCallback<void>): void--><!--Device-print-function startPrintJob(jobInfo: PrintJob, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobInfo | [PrintJob](arkts-basicservices-print-printjob-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let jobInfo : print.PrintJob = {
    fdList : [44, 45], // fdList中的fd可通过fs.open等文件操作获取文件描述符
    jobId : 'jobId_12',
    printerId : 'printerId_32',
    jobState : print.PrintJobState.PRINT_JOB_COMPLETED,
    jobSubstate : print.PrintJobSubState.PRINT_JOB_COMPLETED_SUCCESS,
    copyNumber : 1,
    pageRange : {},
    isSequential : false,
    pageSize : {id : '', name : '', width : 10, height : 20},
    isLandscape : false,
    colorMode : print.PrintColorMode.COLOR_MODE_COLOR,
    duplexMode : print.PrintDuplexMode.DUPLEX_MODE_NONE,
    margin : undefined,
    preview : undefined,
    options : undefined
};
print.startPrintJob(jobInfo, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to start print job. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('start Print Job success');
    }
});
```


## startPrintJob

```TypeScript
function startPrintJob(jobInfo: PrintJob): Promise<void>
```

开始打印任务，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function startPrintJob(jobInfo: PrintJob): Promise<void>--><!--Device-print-function startPrintJob(jobInfo: PrintJob): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobInfo | [PrintJob](arkts-basicservices-print-printjob-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let jobInfo : print.PrintJob = {
    fdList : [44, 45], // fdList中的fd可通过fs.open等文件操作获取文件描述符
    jobId : 'jobId_12',
    printerId : 'printerId_32',
    jobState : print.PrintJobState.PRINT_JOB_COMPLETED,
    jobSubstate : print.PrintJobSubState.PRINT_JOB_COMPLETED_SUCCESS,
    copyNumber : 1,
    pageRange : {},
    isSequential : false,
    pageSize : {id : '', name : '', width : 10, height : 20},
    isLandscape : false,
    colorMode : print.PrintColorMode.COLOR_MODE_COLOR,
    duplexMode : print.PrintDuplexMode.DUPLEX_MODE_NONE,
    margin : undefined,
    preview : undefined,
    options : undefined
};
print.startPrintJob(jobInfo).then(() => {
    console.info('start Print success');
}).catch((error: BusinessError) => {
    console.error(`Failed to start print job. Code: ${error.code}, message: ${error.message}`);
});
```
