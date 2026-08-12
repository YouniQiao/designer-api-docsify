# HallResponse

Describes the Hall effect sensor data. It extends from [Response](arkts-sensorservice-sensor-response-i.md#Response).

**Inheritance/Implementation:** HallResponse extends [Response](arkts-sensorservice-sensor-response-i.md#Response)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface HallResponse extends Response--><!--Device-sensor-interface HallResponse extends Response-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
```

## status

```TypeScript
status: double
```

Hall effect sensor status. This parameter specifies whether a magnetic field exists around a device. The value  
**0** means that a magnetic field does not exist, and a value greater than **0** means the opposite.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-HallResponse-status: double--><!--Device-HallResponse-status: double-End-->

**System capability:** SystemCapability.Sensors.Sensor

