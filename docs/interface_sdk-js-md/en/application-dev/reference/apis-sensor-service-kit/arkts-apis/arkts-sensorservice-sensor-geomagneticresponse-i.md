# GeomagneticResponse

```TypeScript
interface GeomagneticResponse
```

Sets the geomagnetic response object, which describes the geomagnetic field information of a specified geographical location.

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## deflectionAngle

```TypeScript
deflectionAngle: number
```

Magnetic declination, which is the angle between true north (geographic north) and the magnetic north (the horizontal component of the field). in degrees.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## geomagneticDip

```TypeScript
geomagneticDip: number
```

Magnetic dip, also called magnetic inclination, which is the angle measured from the horizontal plane to the magnetic field vector, in degrees.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## levelIntensity

```TypeScript
levelIntensity: number
```

Horizontal magnetic field strength, which is the total strength of the geomagnetic field on the horizontal plane. in nT.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## totalIntensity

```TypeScript
totalIntensity: number
```

Total intensity of the geomagnetic field vector in three-dimensional space. in nT.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## x

```TypeScript
x: number
```

X component (north component) of the geomagnetic field, in nT.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: number
```

Y component (east component) of the geomagnetic field, in nT.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: number
```

Z component (vertical component) of the geomagnetic field, in nT.

**Type:** number

**Since:** 8

**System capability:** SystemCapability.Sensors.Sensor
