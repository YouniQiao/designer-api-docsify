# off

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## off('locationChange')

```TypeScript
function off(type: 'locationChange', callback?: Callback<Location>): void
```

Unsubscribe location changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** locationChange

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'locationChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | No |


## off('locationServiceState')

```TypeScript
function off(type: 'locationServiceState', callback?: Callback<boolean>): void
```

Unsubscribe location switch changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** locationEnabledChange

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'locationServiceState' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |


## off('cachedGnssLocationsReporting')

```TypeScript
function off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void
```

Unsubscribe to cache GNSS locations update messages

**Since:** 8

**Deprecated since:** 9

**Substitutes:** cachedGnssLocationsChange

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cachedGnssLocationsReporting' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | No |


## off('gnssStatusChange')

```TypeScript
function off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void
```

Unsubscribe gnss status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** satelliteStatusChange

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'gnssStatusChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | No |


## off('nmeaMessageChange')

```TypeScript
function off(type: 'nmeaMessageChange', callback?: Callback<string>): void
```

Unsubscribe nmea message changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** nmeaMessage

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'nmeaMessageChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |


## off('fenceStatusChange')

```TypeScript
function off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void
```

Remove a geofence and unsubscribe geo fence status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** gnssFenceStatusChange

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'fenceStatusChange' | Yes |
| request | [GeofenceRequest](arkts-location-geolocationmanager-geofencerequest-i.md) | Yes |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |
