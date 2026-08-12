# sendCommand

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## sendCommand

```TypeScript
function sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void
```

Send extended commands to location subsystem.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendCommand](ohos.geoLocationManager/geoLocationManager.sendCommand)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void--><!--Device-geolocation-function sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
geolocation.sendCommand(requestInfo, (err, result) => {
    if (err) {
        console.info('sendCommand: err=' + JSON.stringify(err));
    }
    if (result) {
        console.info('sendCommand: result=' + JSON.stringify(result));
    }
});
```


## sendCommand

```TypeScript
function sendCommand(command: LocationCommand): Promise<boolean>
```

Send extended commands to location subsystem.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendCommand](ohos.geoLocationManager/geoLocationManager.sendCommand)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function sendCommand(command: LocationCommand): Promise<boolean>--><!--Device-geolocation-function sendCommand(command: LocationCommand): Promise<boolean>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
geolocation.sendCommand(requestInfo).then((result) => {
    console.info('promise, sendCommand: ' + JSON.stringify(result));
});
```
