# suspend (System API)

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## suspend

```TypeScript
function suspend(isImmediate?: boolean): void
```

Enables a device to enter the sleep state.

**Since:** 9

**Required permissions:** 
- API version 19+: ohos.permission.POWER_MANAGER

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isImmediate | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4900101](../errorcode-power.md#4900101-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
