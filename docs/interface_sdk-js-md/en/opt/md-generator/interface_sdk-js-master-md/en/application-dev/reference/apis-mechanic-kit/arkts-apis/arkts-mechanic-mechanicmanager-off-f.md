# off

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## off('attachStateChange')

```TypeScript
function off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void
```

Unsubscribes from device attachment state change events.

**Since:** 20

<!--Device-mechanicManager-function off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void--><!--Device-mechanicManager-function off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'attachStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachStateChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
// Define the callback function for device connection state changes.
let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Unregister');
// Unregister the attachStateChange event listener.
mechanicManager.off("attachStateChange", callback);
console.info('Succeeded in unregistering callback.');
```


## off('trackingStateChange')

```TypeScript
function off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void
```

Unsubscribes from tracking events.

**Since:** 20

<!--Device-mechanicManager-function off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trackingStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TrackingEventInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
// Define the callback function for tracking state changes.
let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Unregister');
// Unregister the trackingStateChange event listener.
mechanicManager.off("trackingStateChange", callback);
console.info('Succeeded in unregistering callback.');
```
