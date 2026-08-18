# off_fenceStatusChange

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## off_fenceStatusChange('fenceStatusChange')

```TypeScript
function off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void
```

Remove a geofence and unsubscribe geo fence status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** gnssFenceStatusChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void--><!--Device-geolocation-function off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'fenceStatusChange' | Yes | Indicates the location service event to be subscribed to. |
| request | GeofenceRequest | Yes | Indicates the Geo-fence configuration parameters. |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes | Indicates which ability to start when the geofence event is triggered. |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
import wantAgent from '@ohos.app.ability.wantAgent';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: [
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1",
        }
    ],
    operationType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
  geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
  geolocation.off('fenceStatusChange', requestInfo, wantAgentObj);
});
```

