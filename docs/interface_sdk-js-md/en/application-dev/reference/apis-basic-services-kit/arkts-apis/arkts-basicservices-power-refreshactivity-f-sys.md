# refreshActivity (System API)

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## refreshActivity

```TypeScript
function refreshActivity(reason: string): void
```

Refreshes the device activity status (for example, resetting the screen-off time).This API takes effect only when the device is active. For details about the device activity status, see [power.isActive](arkts-basicservices-power-isactive-f.md).

**Since:** 20

**Required permissions:** ohos.permission.REFRESH_USER_ACTION

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../errorcode-power.md#4900101-service-connection-failure) |
| [4900201](../errorcode-power.md#4900201-frequent-status-refreshes) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
