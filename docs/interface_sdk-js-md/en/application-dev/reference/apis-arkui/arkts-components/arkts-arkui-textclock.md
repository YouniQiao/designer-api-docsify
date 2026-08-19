# TextClock

The **TextClock** component displays the current system time in text format for different time zones. The time is accurate to seconds. When the component is invisible, the time change stops. The visible status of a component is processed based on onVisibleAreaChange. If the visible threshold **ratios** is greater than 0, the component is visible.

## Child Components Not supported

## TextClock

```TypeScript
TextClock(options?: TextClockOptions)
```

Create TextClock component.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TextClockInterface-(options?: TextClockOptions): TextClockAttribute--><!--Device-TextClockInterface-(options?: TextClockOptions): TextClockAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextClockOptions](arkts-arkui-textclockoptions-i.md) | No | Options of the text clock. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [TextClockConfiguration](arkts-arkui-textclockconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. |
| [TextClockOptions](arkts-arkui-textclockoptions-i.md) | Options used to build the **TextClock** component. &gt; **NOTE：**&gt; &gt; To standardize anonymous object definitions, the element definitions here have been revised in API version 18. &gt; While historical version information is preserved for anonymous objects, there may be cases where the outer element &gt; 's @since version number is higher than inner elements'. This does not affect interface usability. |

