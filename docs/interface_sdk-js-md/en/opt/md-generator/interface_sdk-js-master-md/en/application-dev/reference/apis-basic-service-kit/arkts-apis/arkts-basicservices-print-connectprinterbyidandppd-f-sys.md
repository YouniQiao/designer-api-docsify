# connectPrinterByIdAndPpd (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## connectPrinterByIdAndPpd

```TypeScript
function connectPrinterByIdAndPpd(printerId: string, protocol: string, ppdName: string): Promise<void>
```

Query recommend printer drivers by printer ID.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function connectPrinterByIdAndPpd(printerId: string, protocol: string, ppdName: string): Promise<void>--><!--Device-print-function connectPrinterByIdAndPpd(printerId: string, protocol: string, ppdName: string): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |
| protocol | string | Yes |
| [ppdName](arkts-basicservices-print-ppdinfo-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-print.md#13100003-print-service-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
