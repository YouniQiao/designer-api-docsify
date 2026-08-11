# off (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## off('uninstallDLPSandbox')

```TypeScript
function off(type: 'uninstallDLPSandbox', listener?: Callback<DLPSandboxState>): void
```

Unsubscribes from the DLP sandbox uninstall event. After the API is successfully called, the application will no longer receive callback notifications for the DLP sandbox uninstall event.

This API can be called only after a listener is registered using   
[on](dlpPermission.on(type: 'uninstallDLPSandbox', listener: Callback&lt;DLPSandboxState&gt;)).

When the DLP management application exits or no longer needs to track sandbox status changes, unregister the listener to release resources.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function off(type: 'uninstallDLPSandbox', listener?: Callback<DLPSandboxState>): void--><!--Device-dlpPermission-function off(type: 'uninstallDLPSandbox', listener?: Callback<DLPSandboxState>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'uninstallDLPSandbox' | Yes | Event type. It has a fixed value of **uninstallDLPSandbox**, which indicates the DLP sandbox application uninstall event. |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DLPSandboxState&gt; | No | Callback used when a sandbox application is uninstalled. By default, this parameter is left blank, which unregisters all callbacks for the sandbox uninstall event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.off('uninstallDLPSandbox', (info: dlpPermission.DLPSandboxState) => {
    console.info('uninstallDLPSandbox event', info.appIndex, info.bundleName)
  }); // Unsubscribe from the DLP sandbox application uninstall event.
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}
```

