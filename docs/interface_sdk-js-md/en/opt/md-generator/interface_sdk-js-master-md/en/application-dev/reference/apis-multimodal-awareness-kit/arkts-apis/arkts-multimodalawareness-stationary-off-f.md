# off

## Modules to Import

```TypeScript
import { stationary } from 'kits/@kit.MultimodalAwarenessKit';
```

## off

```TypeScript
function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void
```

Unsubscribes from the device status.

**Since:** 9

<!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void--><!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Stationary

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| activity | [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | Yes |
| event | [ActivityEvent](arkts-multimodalawareness-stationary-activityevent-e.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ActivityResponse&gt; | No |

## Examples

```TypeScript
stationary.off('still', stationary.ActivityEvent.ENTER);
```
