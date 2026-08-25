# RotationLimits（系统接口）

相对于参考点的旋转角度限制

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## negativePitchMax

```TypeScript
negativePitchMax: double
```

Maximum pitch rotation angles in the negative direction, ranging from -2*Math.PI to 0, measured in radians. If the value is less than or equal to -2*Math.PI, there is no restriction.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

## negativeRollMax

```TypeScript
negativeRollMax: double
```

Maximum roll rotation angles in the negative direction, ranging from -2*Math.PI to 0, measured in radians. If the value is less than or equal to -2*Math.PI, there is no restriction.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

## negativeYawMax

```TypeScript
negativeYawMax: double
```

Maximum yaw rotation angles in the negative direction, ranging from -2*Math.PI to 0, measured in radians. If the value is less than or equal to -2*Math.PI, there is no restriction.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

## positivePitchMax

```TypeScript
positivePitchMax: double
```

Maximum pitch rotation angles in the positive direction, ranging from 0 to 2*Math.PI, measured in radians. If the value is greater than or equal to 2*Math.PI, there is no restriction.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

## positiveRollMax

```TypeScript
positiveRollMax: double
```

Maximum roll rotation angles in the positive direction, ranging from 0 to 2*Math.PI, measured in radians. If the value is greater than or equal to 2*Math.PI, there is no restriction.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

## positiveYawMax

```TypeScript
positiveYawMax: double
```

Maximum yaw rotation angles in the positive direction, ranging from 0 to 2*Math.PI, measured in radians. If the value is greater than or equal to 2*Math.PI, there is no restriction.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。
