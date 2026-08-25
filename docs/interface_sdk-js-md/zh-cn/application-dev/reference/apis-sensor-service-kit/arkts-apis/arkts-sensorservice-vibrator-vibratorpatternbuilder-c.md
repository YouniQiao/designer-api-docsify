# VibratorPatternBuilder

提供添加长振、短振事件和生成VibratorPattern对象的方法。使用流程：先通过 [addContinuousEvent](#addcontinuousevent)或 [addTransientEvent](#addtransientevent)添加振动事件，再通过 [build](#build)方法生成VibratorPattern对象，最后将该对象作为 [VibrateFromPattern](arkts-sensorservice-vibrator-vibratefrompattern-i.md)的pattern参数传入 [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md) 接口触发振动。 当开发者需要通过灵活组合振动事件（长振和短振）构建自定义振动序列时使用此接口。适用于需要动态排列振动事件的交互反馈场景（如表情包拟真效果、游戏场景反馈），相比VibrateFromFile以文件描述符方式传递振动事件， VibratorPatternBuilder以振动事件数组形式传递，支持更灵活的振动事件排列组合。

**起始版本：** 18

**系统能力：** SystemCapability.Sensors.MiscDevice

## 导入模块

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## addContinuousEvent

```TypeScript
addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder
```

添加长振事件的方法。添加后使用build (#build18)方法生成VibratorPattern (#vibratorpattern18)对象。 用于在自定义振动序列中添加一段持续振动事件，适用于需要持续振动反馈的场景（如引擎振动、拉弓振动等）。返回VibratorPatternBuilder对象，支持链式调用addContinuousEvent或 addTransientEvent继续添加振动事件

**起始版本：** 18

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| time | number | 是 |
| duration | number | 是 |
| options | [ContinuousParam](arkts-sensorservice-vibrator-continuousparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## addTransientEvent

```TypeScript
addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder
```

添加短振事件的方法，添加后使用[build](#build)方法生成 [VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md)对象。适用于点击、按键等短促振动反馈场景，返回VibratorPatternBuilder对象，支持链式调用继续添加振动事件。

**起始版本：** 18

**系统能力：** SystemCapability.Sensors.MiscDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| time | number | 是 |
| options | [TransientParam](arkts-sensorservice-vibrator-transientparam-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## build

```TypeScript
build(): VibratorPattern
```

构造组合短事件或长事件的振动序列的方法。 适用于需要将自定义振动事件组合为振动序列后，通过[VibrateFromPattern](arkts-sensorservice-vibrator-vibratefrompattern-i.md)触发马达振动的场景。需先通过 [addContinuousEvent](#addcontinuousevent)或 [addTransientEvent](#addtransientevent)添加振动事件后，再调用本方法生成VibratorPattern对象。返回 VibratorPattern对象，包含振动序列的起始时间和振动事件数组。该对象可作为VibrateFromPattern的pattern参数传入 [startVibration](arkts-sensorservice-vibrator-startvibration-f.md) 接口触发振动。需先通过[addContinuousEvent](#addcontinuousevent)或 [addTransientEvent](#addtransientevent)添加至少一个振动事件后调用本方法，否则生成的VibratorPattern 为空序列。

**起始版本：** 18

**系统能力：** SystemCapability.Sensors.MiscDevice

**返回值：**

| 类型 |
| --- |
| [VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md) |
