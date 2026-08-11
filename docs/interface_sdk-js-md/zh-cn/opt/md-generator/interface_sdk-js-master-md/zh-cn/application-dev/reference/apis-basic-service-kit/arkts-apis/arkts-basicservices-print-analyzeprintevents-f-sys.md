# analyzePrintEvents（系统接口）

## analyzePrintEvents

```TypeScript
function analyzePrintEvents(printerId: string, eventType: string): Promise<string>
```

分析打印事件。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-print-function analyzePrintEvents(printerId: string, eventType: string): Promise<string>--><!--Device-print-function analyzePrintEvents(printerId: string, eventType: string): Promise<string>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |
| eventType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
