# RotationMatrixResponse

设置旋转矩阵响应对象，用于描述旋转矩阵和倾斜矩阵的计算结果。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-sensor-interface RotationMatrixResponse--><!--Device-sensor-interface RotationMatrixResponse-End-->

**System capability:** SystemCapability.Sensors.Sensor

## Modules to Import

```TypeScript
import { sensor } from 'kits/@kit.SensorServiceKit';
```

## inclination

```TypeScript
inclination: Array<double>
```

倾斜矩阵，长度为9的一维数组，表示地磁倾斜变换矩阵。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-RotationMatrixResponse-inclination: Array<double>--><!--Device-RotationMatrixResponse-inclination: Array<double>-End-->

**System capability:** SystemCapability.Sensors.Sensor

## rotation

```TypeScript
rotation: Array<double>
```

旋转矩阵，长度为9的一维数组，表示设备在三维空间中的旋转状态。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-RotationMatrixResponse-rotation: Array<double>--><!--Device-RotationMatrixResponse-rotation: Array<double>-End-->

**System capability:** SystemCapability.Sensors.Sensor

