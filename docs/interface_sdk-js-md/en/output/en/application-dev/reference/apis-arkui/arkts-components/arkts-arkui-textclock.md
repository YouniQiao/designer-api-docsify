# TextClock

The **TextClock** component displays the current system time in text format for different time zones. The time is accurate to seconds. When the component is invisible, the time change stops. The visible status of a component is processed based on [onVisibleAreaChange]{@link CommonMethod#onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback)}. If the visible threshold **ratios** is greater than 0, the component is visible.

## Child Components Not supported

## TextClock

```TypeScript
TextClock(options?: TextClockOptions)
```

Create TextClock component.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TextClockInterface-(options?: TextClockOptions): TextClockAttribute--><!--Device-TextClockInterface-(options?: TextClockOptions): TextClockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Options of the text clock. |

## Summary

