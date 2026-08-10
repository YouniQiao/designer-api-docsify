# TextTimer

TextTimer是通过文本显示计时信息并控制其计时器状态的组件，支持正向计时与倒计时两种模式，可自定义显示格式，适用于秒表、活动倒计时等需要展示时间流逝的场景。常用于倒计时场景，如考试倒计时、限时活动、运动计时等。

组件不可见（非锁屏状态和应用后台状态）时，UI时间变动将停止（即该组件此时不会绘制），[onTimer]{@link TextTimerAttribute#onTimer}仍然会正常触发。

## 子组件

无

## TextTimer

```TypeScript
TextTimer(options?: TextTimerOptions)
```

创建文本计时器组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-TextTimerInterface-(options?: TextTimerOptions): TextTimerAttribute--><!--Device-TextTimerInterface-(options?: TextTimerOptions): TextTimerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextTimerOptions](arkts-arkui-texttimeroptions-i.md) | No | 通过文本显示计时信息并控制其计时器状态的组件参数。当需要自定义计时器配置（如设置倒计时开关、计时时间、初始时间、控制器等）时传入此参数；不传入时使用 TextTimerOptions的默认配置。 <br>默认值继承[TextTimerOptions]{@link TextTimerOptions} 。 |

## Summary

- [TextTimerConfiguration](arkts-arkui-texttimer-texttimerconfiguration-i.md)
- [TextTimerOptions](arkts-arkui-texttimer-texttimeroptions-i.md)
