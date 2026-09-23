# LocationOptions

```TypeScript
interface LocationOptions
```

Indicates the geographical location, which is used to pass the longitude, latitude, and altitude information for calculating the geomagnetic field.

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## altitude

```TypeScript
altitude: number
```

Altitude. Unit: m

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## latitude

```TypeScript
latitude: number
```

Latitude. Value range: [-90, 90]. Unit: degree

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## longitude

```TypeScript
longitude: number
```

Longitude. Value range: [-180, 180]. Unit: degree

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor
