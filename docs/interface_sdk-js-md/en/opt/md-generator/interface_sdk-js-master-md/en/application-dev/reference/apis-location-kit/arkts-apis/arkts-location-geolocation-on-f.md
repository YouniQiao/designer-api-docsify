# on

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## on('locationChange')

```TypeScript
function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void
```

Subscribe location changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [locationChange](ohos.geoLocationManager/geoLocationManager.on#event:locationChange)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void--><!--Device-geolocation-function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'locationChange' | Yes |
| request | [LocationRequest](arkts-location-geolocationmanager-locationrequest-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);
```


## on('locationServiceState')

```TypeScript
function on(type: 'locationServiceState', callback: Callback<boolean>): void
```

Subscribe location switch changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [locationEnabledChange](ohos.geoLocationManager/geoLocationManager.on#event:locationEnabledChange)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'locationServiceState', callback: Callback<boolean>): void--><!--Device-geolocation-function on(type: 'locationServiceState', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'locationServiceState' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
```


## on('cachedGnssLocationsReporting')

```TypeScript
function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void
```

Subscribe to cache GNSS locations update messages

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [cachedGnssLocationsChange](ohos.geoLocationManager/geoLocationManager.on#event:cachedGnssLocationsChange)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void--><!--Device-geolocation-function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cachedGnssLocationsReporting' | Yes |
| request | [CachedGnssLocationsRequest](arkts-location-geolocationmanager-cachedgnsslocationsrequest-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
```


## on('gnssStatusChange')

```TypeScript
function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void
```

Subscribe gnss status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [satelliteStatusChange](ohos.geoLocationManager/geoLocationManager.on#event:satelliteStatusChange)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void--><!--Device-geolocation-function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'gnssStatusChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo):void => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);
```


## on('nmeaMessageChange')

```TypeScript
function on(type: 'nmeaMessageChange', callback: Callback<string>): void
```

Subscribe nmea message changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [nmeaMessage](ohos.geoLocationManager/geoLocationManager.on#event:nmeaMessage)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'nmeaMessageChange', callback: Callback<string>): void--><!--Device-geolocation-function on(type: 'nmeaMessageChange', callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'nmeaMessageChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb );
```


## on('fenceStatusChange')

```TypeScript
function on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void
```

Add a geofence and subscribe geo fence status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [gnssFenceStatusChange](ohos.geoLocationManager/geoLocationManager.on#event:gnssFenceStatusChange)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void--><!--Device-geolocation-function on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'fenceStatusChange' | Yes |
| request | [GeofenceRequest](arkts-location-geolocationmanager-geofencerequest-i.md) | Yes |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
import wantAgent from '@ohos.app.ability.wantAgent';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: [
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1"
        }
    ],
    operationType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
  geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
});
```
