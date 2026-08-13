# authSmbDeviceAsRegisteredUser (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## authSmbDeviceAsRegisteredUser

```TypeScript
function authSmbDeviceAsRegisteredUser(host: SharedHost, username: string, password: string): Promise<PrinterInformation[]>
```

Authenticate SMB device as registered user and get available printers.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function authSmbDeviceAsRegisteredUser(host: SharedHost, username: string, password: string): Promise<PrinterInformation[]>--><!--Device-print-function authSmbDeviceAsRegisteredUser(host: SharedHost, username: string, password: string): Promise<PrinterInformation[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | [SharedHost](arkts-basicservices-print-sharedhost-i.md) | Yes |
| username | string | Yes |
| password | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 13100014 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13100013 |
| 13100012 |
