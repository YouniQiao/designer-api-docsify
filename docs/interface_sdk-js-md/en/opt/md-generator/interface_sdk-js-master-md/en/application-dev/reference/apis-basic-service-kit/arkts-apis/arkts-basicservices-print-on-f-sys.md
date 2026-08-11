# on (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## on('printerStateChange')

```TypeScript
function on(type: 'printerStateChange', callback: (state: PrinterState, info: PrinterInfo) => void): void
```

Registers a listener for printer state change events. This API uses a callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function on(type: 'printerStateChange', callback: (state: PrinterState, info: PrinterInfo) => void): void--><!--Device-print-function on(type: 'printerStateChange', callback: (state: PrinterState, info: PrinterInfo) => void): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'printerStateChange' | Yes |
| callback | (state: PrinterState, info: PrinterInfo) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';

print.on('printerStateChange', (state: print.PrinterState, info: print.PrinterInfo) => {
    if (state === null || info === null) {
        console.error('printer state changed state is null or info is null');
        return;
    } else {
        console.info('on printer state changed, state : ' + JSON.stringify(state));
        console.info('on printer state changed, info : ' + JSON.stringify(info));
    }
})
```


## on('jobStateChange')

```TypeScript
function on(type: 'jobStateChange', callback: (state: PrintJobState, job: PrintJob) => void): void
```

Registers a listener for print job state change events. This API uses a callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function on(type: 'jobStateChange', callback: (state: PrintJobState, job: PrintJob) => void): void--><!--Device-print-function on(type: 'jobStateChange', callback: (state: PrintJobState, job: PrintJob) => void): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'jobStateChange' | Yes |
| callback | (state: PrintJobState, job: PrintJob) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';

print.on('jobStateChange', (state: print.PrintJobState, job: print.PrintJob) => {
    console.info('onJobStateChange, state : ' + JSON.stringify(state) + ', job : ' + JSON.stringify(job));
})
```


## on('extInfoChange')

```TypeScript
function on(type: 'extInfoChange', callback: (extensionId: string, info: string) => void): void
```

Registers a listener for printer extension information change events. This API uses a callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function on(type: 'extInfoChange', callback: (extensionId: string, info: string) => void): void--><!--Device-print-function on(type: 'extInfoChange', callback: (extensionId: string, info: string) => void): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'extInfoChange' | Yes |
| callback | (extensionId: string, info: string) =&gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';

print.on('extInfoChange', (extensionId: string, info: string) => {
    console.info('onExtInfoChange, extensionId : ' + JSON.stringify(extensionId) + ', info : ' + JSON.stringify(info));
})
```
