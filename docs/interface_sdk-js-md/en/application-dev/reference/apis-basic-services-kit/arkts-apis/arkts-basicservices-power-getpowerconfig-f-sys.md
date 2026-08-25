# getPowerConfig (System API)

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## getPowerConfig

```TypeScript
function getPowerConfig(sceneName: string): string
```

Query the power configuration value for a given scene name.

**Since:** 26.0.0

**Required permissions:** ohos.permission.POWER_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sceneName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-unifiedgroupinfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../errorcode-power.md#4900101-service-connection-failure) |
| [4900400](../errorcode-power.md#4900400-incorrect-input-parameter) |
| [4900501](../errorcode-power.md#4900501-failure-to-read-the-power-supply-configuration-node) |
