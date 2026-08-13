# removePrinterFromDiscovery

## removePrinterFromDiscovery

```TypeScript
function removePrinterFromDiscovery(printerId: string): Promise<void>
```

从系统打印机发现列表里移除打印机，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.PRINT

<!--Device-print-function removePrinterFromDiscovery(printerId: string): Promise<void>--><!--Device-print-function removePrinterFromDiscovery(printerId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

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

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId : string = 'testPrinterId';
print.removePrinterFromDiscovery(printerId).then(() => {
    console.info('removePrinterFromDiscovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to removePrinterFromDiscovery. Code: ${error.code}, message: ${error.message}`);
})
```
