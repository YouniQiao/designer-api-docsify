# Sensor

指示传感器信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-sensor-interface Sensor--><!--Device-sensor-interface Sensor-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId?: int
```

设备ID。-1表示本地设备，其它值表示远程设备。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Sensor-deviceId?: int--><!--Device-Sensor-deviceId?: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## deviceName

```TypeScript
deviceName?: string
```

设备名称，标识传感器的来源设备。

**Type:** string

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Sensor-deviceName?: string--><!--Device-Sensor-deviceName?: string-End-->

**System capability:** SystemCapability.Sensors.Sensor

## firmwareVersion

```TypeScript
firmwareVersion:string
```

传感器固件版本号，标识传感器固件的当前版本。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-firmwareVersion:string--><!--Device-Sensor-firmwareVersion:string-End-->

**System capability:** SystemCapability.Sensors.Sensor

## hardwareVersion

```TypeScript
hardwareVersion:string
```

传感器硬件版本号，标识传感器硬件的当前版本。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-hardwareVersion:string--><!--Device-Sensor-hardwareVersion:string-End-->

**System capability:** SystemCapability.Sensors.Sensor

## isLocalSensor

```TypeScript
isLocalSensor?: boolean
```

是否为本地传感器。true表示本地传感器，false表示非本地传感器（即远程设备上的传感器）。默认值：true。

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Sensor-isLocalSensor?: boolean--><!--Device-Sensor-isLocalSensor?: boolean-End-->

**System capability:** SystemCapability.Sensors.Sensor

## isMockSensor

```TypeScript
isMockSensor?: boolean
```

是否为模拟传感器。true表示模拟传感器，false表示真实传感器。默认值：false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Sensor-isMockSensor?: boolean--><!--Device-Sensor-isMockSensor?: boolean-End-->

**System capability:** SystemCapability.Sensors.Sensor

## maxRange

```TypeScript
maxRange:double
```

传感器最大测量范围。单位：取决于具体传感器类型（如加速度传感器为m/s²）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-maxRange:double--><!--Device-Sensor-maxRange:double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## maxSamplePeriod

```TypeScript
maxSamplePeriod:long
```

传感器最大采样周期。单位：ns（纳秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-maxSamplePeriod:long--><!--Device-Sensor-maxSamplePeriod:long-End-->

**System capability:** SystemCapability.Sensors.Sensor

## minSamplePeriod

```TypeScript
minSamplePeriod:long
```

传感器最小采样周期。单位：ns（纳秒）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-minSamplePeriod:long--><!--Device-Sensor-minSamplePeriod:long-End-->

**System capability:** SystemCapability.Sensors.Sensor

## power

```TypeScript
power:double
```

传感器估计功耗。单位：mA（毫安）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-power:double--><!--Device-Sensor-power:double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## precision

```TypeScript
precision:double
```

传感器精度。单位：取决于具体传感器类型。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-precision:double--><!--Device-Sensor-precision:double-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorId

```TypeScript
sensorId:int
```

传感器类型ID，对应[SensorId](arkts-sensorservice-sensor-sensorid-e.md)枚举值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-sensorId:int--><!--Device-Sensor-sensorId:int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorIndex

```TypeScript
sensorIndex?: int
```

传感器索引，同一类型传感器可能有多个实例，通过sensorIndex区分。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Sensor-sensorIndex?: int--><!--Device-Sensor-sensorIndex?: int-End-->

**System capability:** SystemCapability.Sensors.Sensor

## sensorName

```TypeScript
sensorName:string
```

传感器名称，标识传感器的类型和型号。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-sensorName:string--><!--Device-Sensor-sensorName:string-End-->

**System capability:** SystemCapability.Sensors.Sensor

## vendorName

```TypeScript
vendorName:string
```

传感器厂商名称，标识传感器的制造商。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Sensor-vendorName:string--><!--Device-Sensor-vendorName:string-End-->

**System capability:** SystemCapability.Sensors.Sensor

