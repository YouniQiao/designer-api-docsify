# on

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## on('printerChange')

```TypeScript
function on(type: 'printerChange', callback: PrinterChangeCallback): void
```

注册打印机变动事件回调，使用callback回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void--><!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'printerChange' | Yes | 表示打印机变动事件。 |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | Yes | 打印机变动之后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 201 | the application does not have permission to call this function. |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';

// Trigger this callback when an added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
```

