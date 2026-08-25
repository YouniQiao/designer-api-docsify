# startGettingPrintFile（系统接口）

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## startGettingPrintFile

```TypeScript
function startGettingPrintFile(jobId: string, printAttributes: PrintAttributes, fd: number,
    onFileStateChanged: Callback<PrintFileCreationState>): void
```

开始获取打印文件，使用Callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jobId | string | 是 |
| printAttributes | [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | 是 |
| fd | number | 是 |
| onFileStateChanged | [Callback](arkts-basicservices-base-callback-i.md)&lt;[PrintFileCreationState](arkts-basicservices-print-printfilecreationstate-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
