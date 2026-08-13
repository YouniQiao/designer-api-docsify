# cancelPrintJob（系统接口）

## cancelPrintJob

```TypeScript
function cancelPrintJob(jobId: string, callback: AsyncCallback<void>): void
```

取消已发送到打印机的打印任务，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function cancelPrintJob(jobId: string, callback: AsyncCallback<void>): void--><!--Device-print-function cancelPrintJob(jobId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let jobId : string = '121212';
print.cancelPrintJob(jobId, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to cancel print job. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('cancelPrintJob success');
    }
});
```


## cancelPrintJob

```TypeScript
function cancelPrintJob(jobId: string): Promise<void>
```

取消已发送到打印机的打印任务，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function cancelPrintJob(jobId: string): Promise<void>--><!--Device-print-function cancelPrintJob(jobId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |

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

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let jobId : string = '121212';
print.cancelPrintJob(jobId).then(() => {
    console.info('cancelPrintJob success');
}).catch((error: BusinessError) => {
    console.error(`Failed to cancel print job. Code: ${error.code}, message: ${error.message}`);
});
```
