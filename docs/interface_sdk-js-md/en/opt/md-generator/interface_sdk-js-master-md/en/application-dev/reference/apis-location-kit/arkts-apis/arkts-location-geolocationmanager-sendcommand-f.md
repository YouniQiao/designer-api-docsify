# sendCommand

## Modules to Import

```TypeScript
```

## sendCommand

```TypeScript
function sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void
```

Send extended commands to location subsystem.

**Since:** 23

<!--Device-geoLocationManager-function sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void--><!--Device-geoLocationManager-function sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let requestInfo: geoLocationManager.LocationCommand = { 'scenario': 0x301, 'command': "command_1" };
try {
  geoLocationManager.sendCommand(requestInfo, (err) => {
    if (err) {
      console.error('sendCommand: err=' + JSON.stringify(err));
    }
  });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```


## sendCommand

```TypeScript
function sendCommand(command: LocationCommand): Promise<void>
```

Send extended commands to location subsystem.

**Since:** 23

<!--Device-geoLocationManager-function sendCommand(command: LocationCommand): Promise<void>--><!--Device-geoLocationManager-function sendCommand(command: LocationCommand): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let requestInfo: geoLocationManager.LocationCommand = { 'scenario': 0x301, 'command': "command_1" };
try {
  geoLocationManager.sendCommand(requestInfo).then(() => {
    console.info('promise, sendCommand success');
  })
    .catch((error: BusinessError) => {
      console.error('promise, sendCommand: error=' + JSON.stringify(error));
    });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
