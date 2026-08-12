# connectPrinterByIpAndPpd (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## connectPrinterByIpAndPpd

```TypeScript
function connectPrinterByIpAndPpd(printerIp: string, protocol: string, ppdName: string): Promise<void>
```

Connect a printer by the printer IP and ppd.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function connectPrinterByIpAndPpd(printerIp: string, protocol: string, ppdName: string): Promise<void>--><!--Device-print-function connectPrinterByIpAndPpd(printerIp: string, protocol: string, ppdName: string): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerIp | string | Yes |
| protocol | string | Yes |
| [ppdName](arkts-basicservices-print-ppdinfo-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13100005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-print.md#13100005-invalid-printer) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
