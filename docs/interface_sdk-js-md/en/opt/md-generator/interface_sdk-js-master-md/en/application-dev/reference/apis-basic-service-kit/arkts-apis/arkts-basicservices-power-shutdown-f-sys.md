# shutdown (System API)

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## shutdown

```TypeScript
function shutdown(reason: string): void
```

Shuts down the system.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.REBOOT

<!--Device-power-function shutdown(reason: string): void--><!--Device-power-function shutdown(reason: string): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

## Examples

```TypeScript
try {
    power.shutdown('shutdown_test');
} catch(err) {
    console.error('shutdown failed, err: ' + err);
}
```
