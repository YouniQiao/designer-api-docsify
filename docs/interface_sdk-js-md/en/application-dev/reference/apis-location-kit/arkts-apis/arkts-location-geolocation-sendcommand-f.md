# sendCommand

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## sendCommand

```TypeScript
function sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void
```

Send extended commands to location subsystem.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## sendCommand

```TypeScript
function sendCommand(command: LocationCommand): Promise<boolean>
```

Send extended commands to location subsystem.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [sendCommand](arkts-location-geolocationmanager-sendcommand-f.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| command | [LocationCommand](arkts-location-geolocationmanager-locationcommand-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
