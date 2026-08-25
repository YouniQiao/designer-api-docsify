# stop

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## stop

```TypeScript
function stop(stopMode: VibratorStopMode): Promise<void>
```

按照指定模式停止马达的振动。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)(stopMode: VibratorStopMode)

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [stopMode](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## stop

```TypeScript
function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void
```

按照指定模式停止马达的振动。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)(stopMode: VibratorStopMode, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [stopMode](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |
