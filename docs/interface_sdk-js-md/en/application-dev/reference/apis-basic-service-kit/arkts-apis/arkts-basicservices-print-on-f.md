# on

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## on('printerChange')

```TypeScript
function on(type: 'printerChange', callback: PrinterChangeCallback): void
```

Registers a listener for the printer change events. This API uses a callback to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void--><!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'printerChange' | Yes | Printer change event. |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | Yes | Callback to be invoked when the printer changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

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

