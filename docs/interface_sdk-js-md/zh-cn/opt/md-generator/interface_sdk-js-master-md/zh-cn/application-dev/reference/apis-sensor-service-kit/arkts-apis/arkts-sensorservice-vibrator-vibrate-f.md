# vibrate

## vibrate

```TypeScript
function vibrate(duration: number, callback?: AsyncCallback<void>): void
```

按照指定持续时间触发马达振动。 > **说明：** > > 从API version 8 开始支持，从API version 9 开始废弃，建议使用 > [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(duration: number, callback?: AsyncCallback<void>): void--><!--Device-vibrator-function vibrate(duration: number, callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## 示例

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(1000, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in vibrating');
  }
})
```


## vibrate

```TypeScript
function vibrate(duration: number): Promise<void>
```

按照指定持续时间触发马达振动。 > **说明：** > > 从API version 8 开始支持，从API version 9 开始废弃，建议使用 > [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)(effect: VibrateEffect, attribute: VibrateAttribute)

**需要权限：** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(duration: number): Promise<void>--><!--Device-vibrator-function vibrate(duration: number): Promise<void>-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(1000).then(() => {
  console.info('Succeed in vibrating');
}, (error: BusinessError) => {
  console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
});
```


## vibrate

```TypeScript
function vibrate(effectId: EffectId): Promise<void>
```

按照预置振动效果触发马达振动。 > **说明：** > > 从API version 8 开始支持，从API version 9 开始废弃，建议使用 > [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)(effect: VibrateEffect, attribute: VibrateAttribute)

**需要权限：** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(effectId: EffectId): Promise<void>--><!--Device-vibrator-function vibrate(effectId: EffectId): Promise<void>-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | [EffectId](arkts-sensorservice-vibrator-effectid-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER).then(() => {
  console.info('Succeed in vibrating');
}, (error: BusinessError) => {
  console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
});
```


## vibrate

```TypeScript
function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void
```

按照指定振动效果触发马达振动。 > **说明：** > > 从API version 8 开始支持，从API version 9 开始废弃，建议使用 > [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void--><!--Device-vibrator-function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | [EffectId](arkts-sensorservice-vibrator-effectid-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## 示例

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in vibrating');
  }
})
```
