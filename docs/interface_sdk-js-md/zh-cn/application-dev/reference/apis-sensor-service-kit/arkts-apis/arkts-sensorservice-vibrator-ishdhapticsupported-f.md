# isHdHapticSupported

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## isHdHapticSupported

```TypeScript
function isHdHapticSupported(): boolean
```

查询当前设备是否支持高清振动。 适用于在触发高清振动前确认设备是否支持，避免在不支持的设备上调用VibrateFromFile或VibrateFromPattern类型振动导致振动效果不佳或返回错误码801。返回true表示设备支持高清振动，可使用 VibrateFromFile和VibrateFromPattern类型触发振动；返回false表示不支持，使用自定义振动类型将返回错误码801或效果不佳。

**起始版本：** 12

**系统能力：** SystemCapability.Sensors.MiscDevice

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-操作设备失败) |
