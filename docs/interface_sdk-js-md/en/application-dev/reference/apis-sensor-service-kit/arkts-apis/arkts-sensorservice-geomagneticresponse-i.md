# GeomagneticResponse

Describes a geomagnetic response object.

**Since:** 8

<!--Device-sensor-interface GeomagneticResponse--><!--Device-sensor-interface GeomagneticResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## deflectionAngle

```TypeScript
deflectionAngle: number
```

Magnetic declination, which is the angle between true north (geographic north) and the magnetic north (the horizontal component of the field), in degrees.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-deflectionAngle: double--><!--Device-GeomagneticResponse-deflectionAngle: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## geomagneticDip

```TypeScript
geomagneticDip: number
```

Magnetic dip, also called magnetic inclination, which is the angle measured from the horizontal plane to the magnetic field vector, in degrees.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-geomagneticDip: double--><!--Device-GeomagneticResponse-geomagneticDip: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## levelIntensity

```TypeScript
levelIntensity: number
```

Horizontal intensity of the magnetic field vector field, in nT.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-levelIntensity: double--><!--Device-GeomagneticResponse-levelIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## totalIntensity

```TypeScript
totalIntensity: number
```

Total intensity of the magnetic field vector, in nT.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-totalIntensity: double--><!--Device-GeomagneticResponse-totalIntensity: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## x

```TypeScript
x: number
```

North component of the geomagnetic field, in nT.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-x: double--><!--Device-GeomagneticResponse-x: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## y

```TypeScript
y: number
```

East component of the geomagnetic field, in nT.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-y: double--><!--Device-GeomagneticResponse-y: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## z

```TypeScript
z: number
```

Vertical component of the geomagnetic field, in nT.

**Type:** number

**Since:** 8

<!--Device-GeomagneticResponse-z: double--><!--Device-GeomagneticResponse-z: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

