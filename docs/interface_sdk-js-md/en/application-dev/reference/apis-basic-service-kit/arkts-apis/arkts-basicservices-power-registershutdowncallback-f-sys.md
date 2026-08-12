# registerShutdownCallback (System API)

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## registerShutdownCallback

```TypeScript
function registerShutdownCallback(callback: Callback<boolean>): void
```

Registers a callback to be invoked when the device is shut down or rebooted. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.REBOOT

<!--Device-power-function registerShutdownCallback(callback: Callback<boolean>): void--><!--Device-power-function registerShutdownCallback(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the device is rebooted, and **false** indicates that the device is shut down. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [4900101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) | Failed to connect to the service. |

## Examples

```TypeScript
try {
    power.registerShutdownCallback((isReboot: boolean) => {
        console.info('device shutdown is: ' + isReboot);
    });
    console.info('register shutdown callback success.');
} catch(err) {
    console.error('register shutdown callback failed, err: ' + err);
}
```

