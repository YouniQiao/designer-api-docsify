# addPrinters（系统接口）

## 导入模块

```TypeScript
```

## addPrinters

```TypeScript
function addPrinters(printers: Array<PrinterInfo>, callback: AsyncCallback<void>): void
```

添加打印机，使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function addPrinters(printers: Array<PrinterInfo>, callback: AsyncCallback<void>): void--><!--Device-print-function addPrinters(printers: Array<PrinterInfo>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printers | Array&lt;[PrinterInfo](arkts-basicservices-print-printerinfo-i-sys.md)&gt; | 是 |
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

let printerInfo : print.PrinterInfo = {
    printerId : '3232',
    printerName : 'hhhhh',
    printerState : 0,
    printerIcon : 12,
    description : 'str',
    capability : undefined,
    options : 'opt'
};
print.addPrinters([printerInfo], (error: BusinessError) => {
    if (error) {
        console.error(`Failed to add printers. Code: ${error.code}, message: ${error.message}`);
    } else {
        console.info('addPrinters success');
    }
});
```


## addPrinters

```TypeScript
function addPrinters(printers: Array<PrinterInfo>): Promise<void>
```

添加打印机，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function addPrinters(printers: Array<PrinterInfo>): Promise<void>--><!--Device-print-function addPrinters(printers: Array<PrinterInfo>): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printers | Array&lt;[PrinterInfo](arkts-basicservices-print-printerinfo-i-sys.md)&gt; | 是 |

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

let printerInfo : print.PrinterInfo = {
    printerId : '3232',
    printerName : 'hhhhh',
    printerState : 0,
    printerIcon : 12,
    description : 'str',
    capability : undefined,
    options : 'opt'
};
print.addPrinters([printerInfo]).then(() => {
    console.info('add printers success.');
}).catch((error: BusinessError) => {
    console.error(`Failed to add printers. Code: ${error.code}, message: ${error.message}`);
});
```
