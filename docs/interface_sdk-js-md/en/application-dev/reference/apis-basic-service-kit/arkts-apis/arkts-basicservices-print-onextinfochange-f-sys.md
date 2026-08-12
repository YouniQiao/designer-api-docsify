# onExtInfoChange (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## onExtInfoChange

```TypeScript
function onExtInfoChange(callback: ExtInfoChangeCallback): void
```

Register event callback for the information change of print extension.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function onExtInfoChange(callback: ExtInfoChangeCallback): void--><!--Device-print-function onExtInfoChange(callback: ExtInfoChangeCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ExtInfoChangeCallback](arkts-basicservices-print-extinfochangecallback-t-sys.md) | Yes | The callback function for information change of print extension. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application |

