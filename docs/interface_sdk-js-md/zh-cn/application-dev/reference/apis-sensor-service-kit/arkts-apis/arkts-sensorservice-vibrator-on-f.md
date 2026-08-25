# on

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## on('vibratorStateChange')

```TypeScript
function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void
```

注册马达上线或下线事件的回调函数。当马达设备上线或下线时触发回调。 当开发者需要实时感知马达设备的上下线状态变化时使用此接口。适用于分布式多设备场景中动态获取马达设备信息，以便在马达上线时及时触发振动或在下线时停止振动。注册成功后，当马达设备上线或下线时，系统将回调 VibratorStatusEvent对象，包含设备ID、马达数量、上下线状态等信息。回调中获取的deviceId可用于 [startVibration](arkts-sensorservice-vibrator-startvibration-f.md) 和[stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)等接口指定目标设备。 注册回调后，需在合适的时机调用 vibrator.off注销回调，避免内存泄 露。同一type重复注册同一callback不会覆盖，需先off再on。

**起始版本：** 19

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'vibratorStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-操作设备失败) |
