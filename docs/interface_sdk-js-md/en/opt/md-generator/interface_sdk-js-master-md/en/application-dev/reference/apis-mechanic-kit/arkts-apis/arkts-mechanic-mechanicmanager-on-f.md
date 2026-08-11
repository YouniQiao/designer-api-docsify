# on

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## on('attachStateChange')

```TypeScript
function on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void
```

Subscribes to device attachment state change events.

**Since:** 20

<!--Device-mechanicManager-function on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void--><!--Device-mechanicManager-function on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'attachStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachStateChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
// Define the callback for device connection state changes. The result parameter carries the device connection state change information.
let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(`'callback result:' ${result}`);
};

// Print a log indicating the listener registration starts.
console.info('Register');
// Register the attachStateChange event listener. The callback is triggered when the device connection state changes.
mechanicManager.on("attachStateChange", callback);
// Print a log indicating that the listener is registered successfully.
console.info('Succeeded in registering callback.');
```


## on('trackingStateChange')

```TypeScript
function on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void
```

Subscribes to tracking events.

**Since:** 20

<!--Device-mechanicManager-function on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void--><!--Device-mechanicManager-function on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'trackingStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TrackingEventInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
// Define the callback for tracking state changes. The result is the tracking event information.
let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(`'callback result:' ${result}`);
};

console.info('Register');
// Register the trackingStateChange event listener. The callback is triggered when the tracking state changes.
mechanicManager.on("trackingStateChange", callback);
console.info('Succeeded in registering callback.');
```
