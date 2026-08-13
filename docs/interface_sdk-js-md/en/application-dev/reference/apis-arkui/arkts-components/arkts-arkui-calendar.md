# Calendar

Defines Calendar Component.

## Calendar

```TypeScript
Calendar(value: {
    date: { year: number; month: number; day: number };
    currentData: MonthData;
    preData: MonthData;
    nextData: MonthData;
    controller?: CalendarController;
  })
```

Set value.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 20

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-CalendarInterface-(value: {    date: { year: number; month: number; day: number };    currentData: MonthData;    preData: MonthData;    nextData: MonthData;    controller?: CalendarController;  }): CalendarAttribute--><!--Device-CalendarInterface-(value: {    date: { year: number; month: number; day: number };    currentData: MonthData;    preData: MonthData;    nextData: MonthData;    controller?: CalendarController;  }): CalendarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | {     date: { year: number; month: number; day: number };     currentData: MonthData;     preData: MonthData;     nextData: MonthData;     controller?: CalendarController;   } | Yes |  |

## Summary

- [CalendarDay](arkts-arkui-calendarday-i-sys.md)
- [CalendarRequestedData](arkts-arkui-calendarrequesteddata-i-sys.md)
- [CalendarSelectedDate](arkts-arkui-calendarselecteddate-i-sys.md)
- [CurrentDayStyle](arkts-arkui-currentdaystyle-i-sys.md)
- [MonthData](arkts-arkui-monthdata-i-sys.md)
- [NonCurrentDayStyle](arkts-arkui-noncurrentdaystyle-i-sys.md)
- [TodayStyle](arkts-arkui-todaystyle-i-sys.md)
- [WeekStyle](arkts-arkui-weekstyle-i-sys.md)
- [WorkStateStyle](arkts-arkui-workstatestyle-i-sys.md)
