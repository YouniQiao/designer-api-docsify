# connectPrinter（系统接口）

## 导入模块

```TypeScript
```

## connectPrinter

```TypeScript
function connectPrinter(printerId: string, callback: AsyncCallback<void>): void
```

通过打印机ID连接打印机，使用callback异步回调。

**起始版本：** 23

**需要权限：** 
- API版本20+：ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API版本10 - 19：ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function connectPrinter(printerId: string, callback: AsyncCallback<void>): void--><!--Device-print-function connectPrinter(printerId: string, callback: AsyncCallback<void>): void-End-->

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId: string = 'printerId_32';
print.connectPrinter(printerId, (error: BusinessError) => {
    if (error) {
        console.error(`Failed to connectPrinter. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('start connect Printer success');
    }
})
```


## connectPrinter

```TypeScript
function connectPrinter(printerId: string): Promise<void>
```

通过打印机ID连接打印机，使用Promise异步回调。

**起始版本：** 23

**需要权限：** 
- API版本20+：ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT
- API版本10 - 19：ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function connectPrinter(printerId: string): Promise<void>--><!--Device-print-function connectPrinter(printerId: string): Promise<void>-End-->

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId: string = 'printerId_32';
print.connectPrinter(printerId).then(() => {
    console.info('start connect Printer success');
}).catch((error: BusinessError) => {
    console.error(`Failed to connectPrinter. Code: ${error.code}, message: ${error.message}`);
})
```
