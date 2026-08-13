# on_fenceStatusChange

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## on_fenceStatusChange

```TypeScript
function on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void
```

Add a geofence and subscribe geo fence status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** gnssFenceStatusChange

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
