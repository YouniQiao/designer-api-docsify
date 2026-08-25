# on

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## on('printerChange')

```TypeScript
function on(type: 'printerChange', callback: PrinterChangeCallback): void
```

Registers a listener for the printer change events. This API uses a callback to return the result.

**Since:** 18

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'printerChange' | Yes |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
