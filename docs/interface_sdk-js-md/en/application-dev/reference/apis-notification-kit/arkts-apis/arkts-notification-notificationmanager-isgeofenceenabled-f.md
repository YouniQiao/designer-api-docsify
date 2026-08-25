# isGeofenceEnabled

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isGeofenceEnabled

```TypeScript
function isGeofenceEnabled(): Promise<boolean>
```

Checks whether geofencing is enabled. This API uses a promise to return the result.

**Since:** 23

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
