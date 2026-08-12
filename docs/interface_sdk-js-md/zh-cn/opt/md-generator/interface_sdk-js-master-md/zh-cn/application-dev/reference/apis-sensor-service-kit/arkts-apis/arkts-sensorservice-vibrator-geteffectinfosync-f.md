# getEffectInfoSync

## getEffectInfoSync

```TypeScript
function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo
```

通过设备ID和马达ID获取预置振动效果信息，用于判断该预置振动效果是否受指定设备的指定马达支持。用于多设备多马达场景下确认指定设备的指定马达是否支持某个预置振动效果，不传param时默认查询本地设备。适用于触发振动前确认效果可用性，避免在不支持的设备或马达上触发振动效果不佳。返回EffectInfo对象，isEffectSupported字段指示是否支持该预置振动效果：返回true时可直接用于startVibration (#vibratorstartvibration9)，返回false时使用该effectId触发振动可能效果不佳。

**起始版本：** 19

<!--Device-vibrator-function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo--><!--Device-vibrator-function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | string | 是 |
| param | [VibratorInfoParam](arkts-sensorservice-vibrator-vibratorinfoparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [EffectInfo](arkts-sensorservice-vibrator-effectinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [14600101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-sensor-service-kit/errorcode-vibrator.md#14600101-操作设备失败) |

## 示例

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 使用try catch对可能出现的异常进行捕获
try {
  const effectInfo: vibrator.EffectInfo = vibrator.getEffectInfoSync('haptic.clock.timer', { deviceId: 1, vibratorId: 3});
  console.info(`isEffectSupported: ${effectInfo.isEffectSupported}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
