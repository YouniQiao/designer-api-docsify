# notifyPrintServiceSpoolerCloseForStarted（系统接口）

## notifyPrintServiceSpoolerCloseForStarted

```TypeScript
function notifyPrintServiceSpoolerCloseForStarted(jobId: string, callback: AsyncCallback<void>): void
```

Notify print service the information.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string, callback: AsyncCallback<void>): void--><!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string, callback: AsyncCallback<void>): void-End-->

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


## notifyPrintServiceSpoolerCloseForStarted

```TypeScript
function notifyPrintServiceSpoolerCloseForStarted(jobId: string): Promise<void>
```

Notify print service the information.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string): Promise<void>--><!--Device-print-function notifyPrintServiceSpoolerCloseForStarted(jobId: string): Promise<void>-End-->

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
