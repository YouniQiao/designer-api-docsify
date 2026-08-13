# authPrintJob（系统接口）

## authPrintJob

```TypeScript
function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>
```

验证打印作业。

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-print-function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>--><!--Device-print-function authPrintJob(jobId: string, userName: string, password: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| [userName](../../apis-telephony-kit/arkts-apis/arkts-telephony-call-voipcallattribute-i-sys.md) | string | 是 |
| password | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [13100006](../../apis-basic-services-kit/errorcode-print.md#13100006-无效的打印任务) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
