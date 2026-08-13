# offVibratorStateChange

## offVibratorStateChange

```TypeScript
function offVibratorStateChange(callback?: Callback<VibratorStatusEvent>): void
```

Unregister a callback function for vibrator plugin or unplug events.

**起始版本：** 23

**废弃版本：** -1

<!--Device-vibrator-function offVibratorStateChange(callback?: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function offVibratorStateChange(callback?: Callback<VibratorStatusEvent>): void-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-操作设备失败) |
