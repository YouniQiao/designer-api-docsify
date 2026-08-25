# isSupportEffect

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## isSupportEffect

```TypeScript
function isSupportEffect(effectId: string, callback: AsyncCallback<boolean>): void
```

查询当前设备是否支持传入的预置振动效果effectId。使用callback异步回调。 当开发者需要在触发预置振动前确认当前设备是否支持指定的振动效果时使用此接口。由于不同设备可能预置不同的振动效果，建议在使用 [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md) 的VibratePreset类型前先调用此接口查询，避免在不支持的设备上触发振动效果不佳。调用成功后，通过callback返回boolean结果：返回true表示设备支持该effectId，可直接用于startVibration； 返回false表示不支持，此时使用该effectId触发振动可能效果不佳或无法振动。

**起始版本：** 10

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## isSupportEffect

```TypeScript
function isSupportEffect(effectId: string): Promise<boolean>
```

查询当前设备是否支持传入的预置振动效果effectId。使用promise异步回调。 当开发者需要在触发预置振动前确认当前设备是否支持指定的振动效果时使用此接口。与callback版本功能一致，开发者可根据异步回调风格偏好选择使用。调用成功时Promise resolve返回boolean结果：返回true表示设备 支持该effectId；返回false表示不支持，此时使用该effectId触发振动可能效果不佳或无法振动。

**起始版本：** 10

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
