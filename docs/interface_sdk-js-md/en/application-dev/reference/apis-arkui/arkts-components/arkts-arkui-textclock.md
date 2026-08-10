# TextClock

TextClock组件通过文本将当前系统时间显示在设备上，支持不同时区的时间显示和时间格式自定义，最高精度到秒级。适用于需要在应用界面上实时展示系统时间、支持多时区显示的场景，可帮助开发者快速实现时间文本展示功能，无需手动计算和更新时
间。

组件不可见时，时间变动将停止。组件的可见状态基于
[onVisibleAreaChange]{@link CommonMethod#onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback)}
处理，可见阈值ratios大于0即视为可见状态。

## 子组件

无

## TextClock

```TypeScript
TextClock(options?: TextClockOptions)
```

创建文本时钟组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TextClockInterface-(options?: TextClockOptions): TextClockAttribute--><!--Device-TextClockInterface-(options?: TextClockOptions): TextClockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextClockOptions](arkts-arkui-textclockoptions-i.md) | No | 通过文本显示当前系统时间的组件参数。不传入时使用默认配置，各属性默认值详见TextClockOptions。 |

## Summary

- [TextClockConfiguration](arkts-arkui-textclock-textclockconfiguration-i.md)
- [TextClockOptions](arkts-arkui-textclock-textclockoptions-i.md)
