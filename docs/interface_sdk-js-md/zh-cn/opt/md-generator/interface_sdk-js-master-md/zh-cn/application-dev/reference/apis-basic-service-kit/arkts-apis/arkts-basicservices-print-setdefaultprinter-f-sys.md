# setDefaultPrinter（系统接口）

## setDefaultPrinter

```TypeScript
function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>
```

设置默认打印机，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>--><!--Device-print-function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |
| type | [DefaultPrinterType](arkts-basicservices-print-defaultprintertype-e.md) | 是 |

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

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = '1';
let type : print.DefaultPrinterType = print.DefaultPrinterType.DEFAULT_PRINTER_TYPE_SET_BY_USER;
print.setDefaultPrinter(printerId, type).then(() => {
    console.info('setDefaultPrinter success');
}).catch((error: BusinessError) => {
    console.error(`Failed to set default printer. Code: ${error.code}, message: ${error.message}`);
});
```
