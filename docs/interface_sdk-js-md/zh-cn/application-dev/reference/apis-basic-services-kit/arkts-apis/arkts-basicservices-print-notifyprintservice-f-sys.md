# notifyPrintService（系统接口）

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## notifyPrintService('spooler_closed_for_cancelled' | 'spooler_closed_for_started')

```TypeScript
function notifyPrintService(jobId: string, type: 'spooler_closed_for_cancelled' | 'spooler_closed_for_started',
    callback: AsyncCallback<void>): void
```

将spooler关闭信息通知打印服务，使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| type | 'spooler_closed_for_cancelled' \| 'spooler_closed_for_started' | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## notifyPrintService('spooler_closed_for_cancelled' | 'spooler_closed_for_started')

```TypeScript
function notifyPrintService(jobId: string,
    type: 'spooler_closed_for_cancelled' | 'spooler_closed_for_started'): Promise<void>
```

将spooler关闭信息通知打印服务，使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| type | 'spooler_closed_for_cancelled' \| 'spooler_closed_for_started' | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
