# ProximityResponse

Describes the proximity sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#Response).

**Inheritance/Implementation:** ProximityResponse extends [Response](arkts-sensorservice-sensor-response-i.md#Response)

**Since:** 8

<!--Device-sensor-interface ProximityResponse extends Response--><!--Device-sensor-interface ProximityResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## distance

```TypeScript
distance: number
```

Proximity between the visible object and the device monitor. The value **0** means the two are close to each other, and a value greater than 0 means that they are far away from each other.

**Type:** number

**Since:** 8

<!--Device-ProximityResponse-distance: double--><!--Device-ProximityResponse-distance: double-End-->

**System capability:** SystemCapability.Sensors.Sensor
