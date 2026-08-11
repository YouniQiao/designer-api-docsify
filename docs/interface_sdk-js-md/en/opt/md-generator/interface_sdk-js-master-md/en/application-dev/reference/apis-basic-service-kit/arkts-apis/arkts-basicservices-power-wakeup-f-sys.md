# wakeup (System API)

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## wakeup

```TypeScript
function wakeup(detail: string): void
```

Wakes up a device.

**Since:** 9

**Required permissions:** 
- API version 19+: ohos.permission.POWER_MANAGER

<!--Device-power-function wakeup(detail: string): void--><!--Device-power-function wakeup(detail: string): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| detail | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

## Examples

```TypeScript
try {
    power.wakeup('wakeup_test');
} catch(err) {
    console.error('wakeup failed, err: ' + err);
}
```
