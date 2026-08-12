# queryAllPrintJobs（系统接口）

## queryAllPrintJobs

```TypeScript
function queryAllPrintJobs(callback: AsyncCallback<void>): void
```

查询所有打印任务，使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [null](null)

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrintJobs(callback: AsyncCallback<void>): void--><!--Device-print-function queryAllPrintJobs(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |


## queryAllPrintJobs

```TypeScript
function queryAllPrintJobs(): Promise<void>
```

查询所有打印任务，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [null](null)

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllPrintJobs(): Promise<void>--><!--Device-print-function queryAllPrintJobs(): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
