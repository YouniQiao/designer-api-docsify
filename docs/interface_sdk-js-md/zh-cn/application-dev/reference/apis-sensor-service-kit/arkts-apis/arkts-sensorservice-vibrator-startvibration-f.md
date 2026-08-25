# startVibration

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## startVibration

```TypeScript
function startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>): void
```

根据指定的振动效果和振动属性触发马达振动，使用callback异步回调。 适用于为用户交互提供触觉反馈、为通知/闹钟等事件提供振动提醒，或在游戏、多媒体等场景中提供沉浸式振动体验。调用成功后，设备马达将按指定效果和属性开始振动；若同一马达已有正在进行的振动，新请求将按系统优先级规则处理。同功能还提供 Promise版本vibrator.startVibration (#vibratorstartvibration9-1)，开发者可根据回调风格偏好选择。

**起始版本：** 9

**需要权限：** ohos.permission.VIBRATE

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [VibrateEffect](arkts-sensorservice-vibrator-vibrateeffect-t.md) | 是 |
| attribute | [VibrateAttribute](arkts-sensorservice-vibrator-vibrateattribute-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14600101](../errorcode-vibrator.md#14600101-操作设备失败) |


## startVibration

```TypeScript
function startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Promise<void>
```

根据指定的振动效果和振动属性触发马达振动，使用promise异步回调。 适用于交互触觉反馈、事件振动提醒或游戏、多媒体等沉浸式振动场景。调用成功时Promise resolve无返回值；调用失败时Promise reject返回错误对象。若同一马达已有振动正在进行，新请求按系统优先级规则处理。同功能还 提供callback版本vibrator.startVibration (#vibratorstartvibration9)，开发者可根据回调风格偏好选择。

**起始版本：** 9

**需要权限：** ohos.permission.VIBRATE

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [VibrateEffect](arkts-sensorservice-vibrator-vibrateeffect-t.md) | 是 |
| attribute | [VibrateAttribute](arkts-sensorservice-vibrator-vibrateattribute-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14600101](../errorcode-vibrator.md#14600101-操作设备失败) |
