# Geolocation

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [geoLocationManager/geoLocationManager](arkts-geolocationmanager.md)

<!--Device-unnamed-export default class Geolocation--><!--Device-unnamed-export default class Geolocation-End-->

**System capability:** SystemCapability.Location.Location.Lite

## Modules to Import

```TypeScript
import { Geolocation, GeolocationResponse, GetLocationOption, GetLocationTypeOption, GetLocationTypeResponse, SubscribeLocationOption } from '@kit.LocationKit';
```

## getLocation

```TypeScript
static getLocation(options?: GetLocationOption): void
```

Obtains the geographic location.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md)

**Required permissions:** ohos.permission.LOCATION

**Model restriction:** This API can be used only in the FA model.

<!--Device-Geolocation-static getLocation(options?: GetLocationOption): void--><!--Device-Geolocation-static getLocation(options?: GetLocationOption): void-End-->

**System capability:** SystemCapability.Location.Location.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetLocationOption](arkts-location-system-geolocation-getlocationoption-i.md) | No |  |

**Examples**

```TypeScript
export default {    
  getLocation() {        
    geolocation.getLocation({            
      success: function(data) {                
        console.info('success get location data. latitude:' + data.latitude);            
      },            
      fail: function(data, code) {                
        console.info('fail to get location. code:' + code + ', data:' + data);            
      }
    });    
  }
}
```

## getLocationType

```TypeScript
static getLocationType(options?: GetLocationTypeOption): void
```

Obtains the location types supported by the system.

**Since:** 3

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-Geolocation-static getLocationType(options?: GetLocationTypeOption): void--><!--Device-Geolocation-static getLocationType(options?: GetLocationTypeOption): void-End-->

**System capability:** SystemCapability.Location.Location.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetLocationTypeOption](arkts-location-system-geolocation-getlocationtypeoption-i.md) | No |  |

**Examples**

```TypeScript
export default {    
  getLocationType() {        
    geolocation.getLocationType({            
      success: function(data) {                
        console.info('success get location type:' + data.types[0]);            
      },            
      fail: function(data, code) {                
        console.info('fail to get location. code:' + code + ', data:' + data);            
       },        
     });    
  },
}
```

## getSupportedCoordTypes

```TypeScript
static getSupportedCoordTypes(): Array<string>
```

Obtains the supported coordinate system types.

**Since:** 3

**Deprecated since:** 9

**Model restriction:** This API can be used only in the FA model.

<!--Device-Geolocation-static getSupportedCoordTypes(): Array<string>--><!--Device-Geolocation-static getSupportedCoordTypes(): Array<string>-End-->

**System capability:** SystemCapability.Location.Location.Lite

**Return value:**

| Type | Description |
| --- | --- |
**Examples**

```TypeScript
export default {    
  getSupportedCoordTypes() {       
    var types = geolocation.getSupportedCoordTypes();   
  },
}
```

## subscribe

```TypeScript
static subscribe(options: SubscribeLocationOption): void
```

Listens to the geographical location. If this method is called multiple times, the last call takes effect.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** locationChange

**Required permissions:** ohos.permission.LOCATION

**Model restriction:** This API can be used only in the FA model.

<!--Device-Geolocation-static subscribe(options: SubscribeLocationOption): void--><!--Device-Geolocation-static subscribe(options: SubscribeLocationOption): void-End-->

**System capability:** SystemCapability.Location.Location.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SubscribeLocationOption](arkts-location-system-geolocation-subscribelocationoption-i.md) | Yes |  |

**Examples**

```TypeScript
export default {    
  subscribe() {        
    geolocation.subscribe({            
      success: function(data) {                
        console.info('get location. latitude:' + data.latitude);            
      },            
      fail: function(data, code) {                
        console.info('fail to get location. code:' + code + ', data:' + data);            
      },        
    });    
  },
}
```

## unsubscribe

```TypeScript
static unsubscribe(): void
```

Cancels listening to the geographical location.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** locationChange

**Required permissions:** ohos.permission.LOCATION

**Model restriction:** This API can be used only in the FA model.

<!--Device-Geolocation-static unsubscribe(): void--><!--Device-Geolocation-static unsubscribe(): void-End-->

**System capability:** SystemCapability.Location.Location.Lite

**Examples**

```TypeScript
export default {    
  unsubscribe() {        
    geolocation.unsubscribe();    
  }
}
```

