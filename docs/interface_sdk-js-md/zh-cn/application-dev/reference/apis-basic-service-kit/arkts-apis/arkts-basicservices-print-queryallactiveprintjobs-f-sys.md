# queryAllActivePrintJobs（系统接口）

## queryAllActivePrintJobs

```TypeScript
function queryAllActivePrintJobs(): Promise<PrintJob[]>
```

查询所有活跃中的打印任务，使用Promise进行异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function queryAllActivePrintJobs(): Promise<PrintJob[]>--><!--Device-print-function queryAllActivePrintJobs(): Promise<PrintJob[]>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[PrintJob](arkts-basicservices-print-printjob-i.md)[]&gt; | Promise used to return a list of all active print jobs. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | the application does not have permission to call this function. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | not system application |

