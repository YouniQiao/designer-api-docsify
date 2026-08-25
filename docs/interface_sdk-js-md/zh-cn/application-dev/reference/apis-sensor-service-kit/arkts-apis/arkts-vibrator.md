# @ohos.vibrator

vibrator模块是设备马达振动的控制模块，属于SensorServiceKit。该模块提供精确控制设备马达振动的能力，支持按指定时长、预置效果、自定义配置文件、自定义振动模式等多种方式触发振动，并支持按指定模式或全部模式停止振动。 此外，模块还提供振动效果支持查询、马达设备信息查询、马达上下线状态监听等能力。 vibrator模块主要用于增强用户交互体验，通过触觉感知反馈为应用提供直观的物理反馈能力。典型使用场景包括：  
- 交互反馈：点击、长按、滑动、拖拽等触控操作的短振反馈，推荐使用VibratePreset预置效果以保持与系统整体振感风格一致。 - 通知提醒：消息通知、来电响铃、闹钟等场景的振动提醒。 - 游戏与多媒体：游戏操作反馈、表情包拟真效果等复杂场景的精细振动，推荐使用VibrateFromFile或VibrateFromPattern自定义振动效果。 - 多设备协同：在分布式场景下，通过指定设备ID和马达ID控制远端设备振动。 vibrator模块的核心能力围绕"启动振动"和"停止振动"两条主线展开，整体使用流程如下： 启动振动流程：  
1. 若使用预置振动效果（VibratePreset），建议先调用[vibrator.isSupportEffect](arkts-sensorservice-vibrator-issupporteffect-f.md)
或[vibrator.isSupportEffectSync](arkts-sensorservice-vibrator-issupporteffectsync-f.md)查询当前设备是否支持该效果；若使用自定义振动配置文件（VibrateFromFile）， 建议先确认设备支持自定义振动模式（可通过[vibrator.isHdHapticSupported](arkts-sensorservice-vibrator-ishdhapticsupported-f.md)查询是否支持高清振动）； 若使用自定义振动模式（VibrateFromPattern），需先通过[VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md)构建振动序列。
2. 调用[vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md)
启动振动，需同时指定振动效果（VibrateEffect）和振动属性（VibrateAttribute）。振动属性中的usage参数决定了振动的场景类型，不同场景类型受系统振动开关管控规则不同。 停止振动流程：  
- 停止指定时长振动或预置效果振动：调用 [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)（API version 9），传入对应的VibratorStopMode。 - 停止自定义振动（VibrateFromFile或VibrateFromPattern）：调用[vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)（API version 10+，无参数版本）停止所有模式振动。 - 停止所有模式振动：调用[vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)（无参数版本）或 [vibrator.stopVibrationSync](arkts-sensorservice-vibrator-stopvibrationsync-f.md)（同步版本）。 - 停止指定设备的马达振动：调用[vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)（API version 19+，传入 VibratorInfoParam）。 多马达设备场景： 从API version 19开始，支持多设备多马达场景。可通过[vibrator.getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md)查询马达信息，通过 [vibrator.on](arkts-sensorservice-vibrator-on-f.md#onvibratorstatechange)监听马达上下线事件，以便动态选择合适的马达触发振动。 振动效果类型对比： | 振动效果类型 | 适用场景 | 个性化程度 | 推荐优先级 | | --- | --- | --- | --- | | VibratePreset | 交互反馈类的短振场景（点击、长按、滑动、拖拽等） | 低，使用系统预置效果 | 推荐，与系统整体振感反馈体验风格一致 | | VibrateFromFile | 复杂场景效果（表情包拟真效果、游戏场景/操作反馈） | 高，支持自定义振动配置文件 | 适用于需要精细振动的场景 | | VibrateFromPattern | 与VibrateFromFile一致，但更灵活 | 高，支持振动事件数组组合 | 适用于需要动态组合振动事件的场景 | | VibrateTime | 基础时长振动，仅控制启停 | 低，无法调节强度和频率 | 仅满足基础功能需求 |

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Sensors.MiscDevice

## 导入模块

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getEffectInfoSync](arkts-sensorservice-vibrator-geteffectinfosync-f.md) |
| [getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md) |
| [isHdHapticSupported](arkts-sensorservice-vibrator-ishdhapticsupported-f.md) |
| [isSupportEffect](arkts-sensorservice-vibrator-issupporteffect-f.md) |
| [isSupportEffect](arkts-sensorservice-vibrator-issupporteffect-f.md) |
| [isSupportEffectSync](arkts-sensorservice-vibrator-issupporteffectsync-f.md) |
| [off](arkts-sensorservice-vibrator-off-f.md#offvibratorstatechange) |
| [offVibratorStateChange](arkts-sensorservice-vibrator-offvibratorstatechange-f.md) |
| [on](arkts-sensorservice-vibrator-on-f.md#onvibratorstatechange) |
| [onVibratorStateChange](arkts-sensorservice-vibrator-onvibratorstatechange-f.md) |
| [startVibration](arkts-sensorservice-vibrator-startvibration-f.md) |
| [startVibration](arkts-sensorservice-vibrator-startvibration-f.md) |
| [stop](arkts-sensorservice-vibrator-stop-f.md) |
| [stop](arkts-sensorservice-vibrator-stop-f.md) |
| [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md) |
| [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md) |
| [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md) |
| [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md) |
| [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md) |
| [stopVibrationSync](arkts-sensorservice-vibrator-stopvibrationsync-f.md) |
| [vibrate](arkts-sensorservice-vibrator-vibrate-f.md) |
| [vibrate](arkts-sensorservice-vibrator-vibrate-f.md) |
| [vibrate](arkts-sensorservice-vibrator-vibrate-f.md) |
| [vibrate](arkts-sensorservice-vibrator-vibrate-f.md) |

### 类

| 名称 |
| --- |
| [VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md) |

### 接口

| 名称 |
| --- |
| [ContinuousParam](arkts-sensorservice-vibrator-continuousparam-i.md) |
| [EffectInfo](arkts-sensorservice-vibrator-effectinfo-i.md) |
| [HapticFileDescriptor](arkts-sensorservice-vibrator-hapticfiledescriptor-i.md) |
| [TransientParam](arkts-sensorservice-vibrator-transientparam-i.md) |
| [VibrateAttribute](arkts-sensorservice-vibrator-vibrateattribute-i.md) |
| [VibrateFromFile](arkts-sensorservice-vibrator-vibratefromfile-i.md) |
| [VibrateFromPattern](arkts-sensorservice-vibrator-vibratefrompattern-i.md) |
| [VibratePreset](arkts-sensorservice-vibrator-vibratepreset-i.md) |
| [VibrateTime](arkts-sensorservice-vibrator-vibratetime-i.md) |
| [VibratorCurvePoint](arkts-sensorservice-vibrator-vibratorcurvepoint-i.md) |
| [VibratorEvent](arkts-sensorservice-vibrator-vibratorevent-i.md) |
| [VibratorInfo](arkts-sensorservice-vibrator-vibratorinfo-i.md) |
| [VibratorInfoParam](arkts-sensorservice-vibrator-vibratorinfoparam-i.md) |
| [VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md) |
| [VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [VibrateAttribute](arkts-sensorservice-vibrator-vibrateattribute-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [EffectId](arkts-sensorservice-vibrator-effectid-e.md) |
| [HapticFeedback](arkts-sensorservice-vibrator-hapticfeedback-e.md) |
| [VibratorEventType](arkts-sensorservice-vibrator-vibratoreventtype-e.md) |
| [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) |

### 类型

| 名称 |
| --- |
| [Usage](arkts-sensorservice-vibrator-usage-t.md) |
| [VibrateEffect](arkts-sensorservice-vibrator-vibrateeffect-t.md) |
