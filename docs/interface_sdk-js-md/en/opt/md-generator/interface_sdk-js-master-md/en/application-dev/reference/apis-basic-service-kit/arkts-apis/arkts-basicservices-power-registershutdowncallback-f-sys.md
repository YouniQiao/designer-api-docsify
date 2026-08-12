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

**Required permissions:** ohos.permission.REBOOT

<!--Device-power-function registerShutdownCallback(callback: Callback<boolean>): void--><!--Device-power-function registerShutdownCallback(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

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
