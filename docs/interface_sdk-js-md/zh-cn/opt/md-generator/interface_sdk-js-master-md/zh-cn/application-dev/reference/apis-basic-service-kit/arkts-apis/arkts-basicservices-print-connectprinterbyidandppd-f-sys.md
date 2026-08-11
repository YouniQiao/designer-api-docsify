# connectPrinterByIdAndPpd（系统接口）

## connectPrinterByIdAndPpd

```TypeScript
function connectPrinterByIdAndPpd(printerId: string, protocol: string, ppdName: string): Promise<void>
```

根据打印机ID查询推荐的打印机驱动程序。

**起始版本：** 24

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-print-function connectPrinterByIdAndPpd(printerId: string, protocol: string, ppdName: string): Promise<void>--><!--Device-print-function connectPrinterByIdAndPpd(printerId: string, protocol: string, ppdName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |
| protocol | string | 是 |
| ppdName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [13100003](../../apis-basic-services-kit/errorcode-print.md#13100003-打印服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
