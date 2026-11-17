# rotateBySpeed（系统接口）

## 导入模块

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## rotateBySpeed

```TypeScript
function rotateBySpeed(mechId: number, speed: RotationSpeed, duration: number): Promise<Result>
```

以指定的速度旋转机械设备

**起始版本：** 20

<!--Device-mechanicManager-function rotateBySpeed(mechId: int, speed: RotationSpeed, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotateBySpeed(mechId: int, speed: RotationSpeed, duration: int): Promise<Result>-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mechId | number | 是 | 机械设备ID |
| speed | [RotationSpeed](arkts-mechanic-mechanicmanager-rotationspeed-i-sys.md) | 是 | 指定旋转速度。最大旋转速度不超过getMaxRotationSpeed的返回值大小，如果超过最大速度，默认取最大值 |
| duration | number | 是 | 旋转持续时间，单位：ms。最大时间不超过getMaxRotationTime的返回值大小，如果超过最大时间，默认取最大值 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[Result](arkts-mechanic-mechanicmanager-result-e-sys.md)&gt; | 返回执行结果 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Not system application. |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) | Service exception. |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) | Device not connected. |

<!--Del-->
**示例**

```TypeScript
console.info('Start rotate');
let degree: mechanicManager.RotationSpeed = {
  yawSpeed: 3 * Math.PI,
  rollSpeed: 3 * Math.PI,
  pitchSpeed: 3 * Math.PI
}
mechanicManager.rotateBySpeed(0, degree, 500)
  .then((result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('Rotate finish');
```

<!--DelEnd-->
