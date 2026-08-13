# discoverUsbPrinters（系统接口）

## discoverUsbPrinters

```TypeScript
function discoverUsbPrinters(): Promise<Array<PrinterInformation>>
```

发现usb打印机，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function discoverUsbPrinters(): Promise<Array<PrinterInformation>>--><!--Device-print-function discoverUsbPrinters(): Promise<Array<PrinterInformation>>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.discoverUsbPrinters().then((printers : print.PrinterInformation[]) => {
    console.info('discoverUsbPrinters data : ' + JSON.stringify(printers));
}).catch((error: BusinessError) => {
    console.error(`Failed to discover USB printers. Code: ${error.code}, message: ${error.message}`);
});
```
