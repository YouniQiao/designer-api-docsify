# CalendarPicker

The **CalendarPicker** component provides a drop-down calendar for users to select a date.

> **NOTE**

Child Components

Not supported

## CalendarPicker

```TypeScript
CalendarPicker(options?: CalendarOptions)
```

Creates a calendar picker.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CalendarOptions](arkts-arkui-calendaroptions-i.md) | No | Parameters of the calendar picker. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CalendarDialogOptions](arkts-arkui-calendardialogoptions-i.md) | Defines the configuration options of the calendar picker dialog box. |
| [CalendarOptions](arkts-arkui-calendaroptions-i.md) | Describes the parameters of the calendar picker. |

### Enums

| Name | Description |
| --- | --- |
| [CalendarAlign](arkts-arkui-calendaralign-e.md) | Enumerates alignment types. |

## Examples

This example uses calendarPicker to implement the CalendarPicker component and provides a drop-down calendar.

```TypeScript
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2024-03-05');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: '#ff182431', font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(`CalendarPicker onChange: ${value.toString()}`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")

      Text('Calendar picker').fontSize(30)
    }.width('100%').margin({ top: 350 })
  }
}
```

Since API version 18, the start and end attributes are added to [CalendarOptions](arkts-arkui-calendaroptions-i.md).

```TypeScript
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2025-01-15');
  private startDate: Date = new Date('2025-01-05');
  private endDate: Date = new Date('2025-01-25');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate, start: this.startDate, end: this.endDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: '#ff182431', font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(`CalendarPicker onChange: ${value.toString()}`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")
    }.width('100%').margin({ top: 350 })
  }
}
```

Since API version 19, the [markToday](#marktoday19) API is added, and the disabledDateRange attribute is added to [CalendarOptions](arkts-arkui-calendaroptions-i.md).

```TypeScript
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private disabledDateRange: DateRange[] = [
    { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
    { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
    { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
    { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
    { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
  ];

  build() {
    Column() {
      CalendarPicker({ disabledDateRange: this.disabledDateRange })
        .margin(10)
        .markToday(true)
        .onChange((value) => {
          console.info(`CalendarPicker onChange: ${value.toString()}`);
        })
    }.alignItems(HorizontalAlign.End).width('100%')
  }
}
```
