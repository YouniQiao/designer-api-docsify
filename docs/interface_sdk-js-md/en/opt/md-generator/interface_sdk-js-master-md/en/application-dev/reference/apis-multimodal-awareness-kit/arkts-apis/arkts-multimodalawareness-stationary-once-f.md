# once

## Modules to Import

```TypeScript
import { stationary } from 'kits/@kit.MultimodalAwarenessKit';
```

## once

```TypeScript
function once(activity: ActivityType, callback: Callback<ActivityResponse>): void
```

Obtains the device status.

**Since:** 9

<!--Device-stationary-function once(activity: ActivityType, callback: Callback<ActivityResponse>): void--><!--Device-stationary-function once(activity: ActivityType, callback: Callback<ActivityResponse>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Stationary

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| activity | [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ActivityResponse&gt; | Yes |

## Examples

```TypeScript
stationary.once('still', (data) => {
    console.info('data=' + JSON.stringify(data));
})
```
