# on_SensorId.GYROSCOPE

## on_SensorId.GYROSCOPE

```TypeScript
function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>,
    options?: Options): void
```

订阅校准的陀螺仪传感器数据。陀螺仪传感器用于测量设备绕X、Y、Z轴的旋转角速度，适用于设备旋转检测、姿态跟踪、游戏操控等场景。调用后，系统会按设定频率通过callback持续上报角速度数据。

**起始版本：** 9

**废弃版本：** -1

**需要权限：** ohos.permission.GYROSCOPE

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-sensor-function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>,    options?: Options): void--><!--Device-sensor-function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>,    options?: Options): void-End-->

**系统能力：** SystemCapability.Sensors.Sensor

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | SensorId.GYROSCOPE | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GyroscopeResponse&gt; | 是 |
| options | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [14500101](../errorcode-sensor.md#14500101-传感器服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  // 订阅校准的陀螺仪传感器数据
  sensor.on(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
    // 输出X、Y、Z坐标分量
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GYROSCOPE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Failed to invoke on. Code: ${e.code}, message: ${e.message}`);
}
```
