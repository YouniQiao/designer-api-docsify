# disconnectPrinter（系统接口）

## 导入模块

```TypeScript
```

## disconnectPrinter

```TypeScript
function disconnectPrinter(printerId: string, callback: AsyncCallback<void>): void
```

断开特定打印机的连接，使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function disconnectPrinter(printerId: string, callback: AsyncCallback<void>): void--><!--Device-print-function disconnectPrinter(printerId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |
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

let printerId: string = 'printerId_32';
print.disconnectPrinter(printerId, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to disconnect printer. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('start disconnect Printer success');
    }
});
```


## disconnectPrinter

```TypeScript
function disconnectPrinter(printerId: string): Promise<void>
```

断开特定打印机的连接，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function disconnectPrinter(printerId: string): Promise<void>--><!--Device-print-function disconnectPrinter(printerId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |

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

let printerId: string = 'printerId_32';
print.disconnectPrinter(printerId).then(() => {
    console.info('start disconnect Printer success');
}).catch((error: BusinessError) => {
    console.error(`Failed to disconnect printer. Code: ${error.code}, message: ${error.message}`);
});
```
