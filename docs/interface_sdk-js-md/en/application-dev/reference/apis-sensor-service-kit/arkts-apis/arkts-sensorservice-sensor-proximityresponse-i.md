# ProximityResponse

Describes the proximity sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#response).

**Inheritance/Implementation:** ProximityResponse extends [Response](arkts-sensorservice-sensor-response-i.md#response)

**Since:** 23

<!--Device-sensor-interface ProximityResponse--><!--Device-sensor-interface ProximityResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## distance

```TypeScript
distance: double
```

Proximity between the visible object and the device monitor. The value **0** means the two are close to each other, and a value greater than 0 means that they are far away from each other.

**Type:** double

**Since:** 23

<!--Device-ProximityResponse-distance: double--><!--Device-ProximityResponse-distance: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

