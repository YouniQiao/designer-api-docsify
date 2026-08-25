# vibrate

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## vibrate

```TypeScript
function vibrate(duration: number, callback?: AsyncCallback<void>): void
```

按照指定持续时间触发马达振动。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md)(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |


## vibrate

```TypeScript
function vibrate(duration: number): Promise<void>
```

按照指定持续时间触发马达振动。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md)(effect: VibrateEffect, attribute: VibrateAttribute)

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## vibrate

```TypeScript
function vibrate(effectId: EffectId): Promise<void>
```

按照预置振动效果触发马达振动。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md)(effect: VibrateEffect, attribute: VibrateAttribute)

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | [EffectId](arkts-sensorservice-vibrator-effectid-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## vibrate

```TypeScript
function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void
```

按照指定振动效果触发马达振动。

> **说明：**&gt;
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md)(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effectId | [EffectId](arkts-sensorservice-vibrator-effectid-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |
