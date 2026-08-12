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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function connectPrinterByIpAndPpd(printerIp: string, protocol: string, ppdName: string): Promise<void>--><!--Device-print-function connectPrinterByIpAndPpd(printerIp: string, protocol: string, ppdName: string): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| printerIp | string | Yes | Indicates the printer IP. &lt;br&gt;IP of the printer to be connected. |
| protocol | string | Yes | Indicates the protocol. &lt;br&gt;Protocol of the printer to be connected. |
| ppdName | string | Yes | Indicates the ppd name. &lt;br&gt;Ppd name of the printer to be connected. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13100005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-print.md#13100005-invalid-printer) | Invalid printer IP. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

