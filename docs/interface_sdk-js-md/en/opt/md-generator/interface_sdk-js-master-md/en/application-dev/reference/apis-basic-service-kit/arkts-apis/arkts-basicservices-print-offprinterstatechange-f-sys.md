# offPrinterStateChange (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## offPrinterStateChange

```TypeScript
function offPrinterStateChange(callback?: Callback<boolean>): void
```

Unregister event callback for the state change of printer.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function offPrinterStateChange(callback?: Callback<boolean>): void--><!--Device-print-function offPrinterStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
