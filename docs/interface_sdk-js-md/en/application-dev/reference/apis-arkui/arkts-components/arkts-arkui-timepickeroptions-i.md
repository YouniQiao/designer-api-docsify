# TimePickerOptions

时间选择器组件的参数说明。

在TimePicker组件滑动过程中修改TimePickerOptions中的属性，会导致这些属性无法生效。

> Date对象用于处理日期和时间，使用方式如下。
> 
> - 方式1：new Date()
> 获取系统当前日期和时间。
> 
> - 方式2：new Date(value: number | string)
> 
> - 方式3：new Date(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number,
> seconds?: number, ms?: number)

> **起始时间和结束时间的异常情形说明：**
> - 起始时间晚于结束时间：起始时间、结束时间都为默认值。
> - 选中时间早于起始时间：选中时间为起始时间。
> - 选中时间晚于结束时间：选中时间为结束时间。
> - 起始时间晚于当前系统时间，选中时间未设置：选中时间为起始时间。
> - 结束时间早于当前系统时间，选中时间未设置：选中时间为结束时间。
> - 时间格式不符合规范，如'01:61:61'：取默认值。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface TimePickerOptions--><!--Device-unnamed-declare interface TimePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: Date
```

指定时间选择组件的结束时间。

默认值：结束时间为23:59:59（小时=23，分钟=59）

> **说明：**
> 
> 1. 仅设置的小时和分钟生效。
> 2. 设置了start或end且为非默认值的场景下，loop不生效。

**Type:** Date

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TimePickerOptions-end?: Date--><!--Device-TimePickerOptions-end?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## format

```TypeScript
format?: TimePickerFormat
```

指定需要显示的TimePicker的格式。

默认值：TimePickerFormat.HOUR_MINUTE

**Type:** [TimePickerFormat](../arkts-apis/arkts-arkui-timepicker-timepickerformat-e.md)

**Default:** HOUR_MINUTE

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TimePickerOptions-format?: TimePickerFormat--><!--Device-TimePickerOptions-format?: TimePickerFormat-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: Date
```

设置选中项的时间。

默认值：当前系统时间

从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

**Type:** Date

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TimePickerOptions-selected?: Date--><!--Device-TimePickerOptions-selected?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: Date
```

指定时间选择组件的起始时间。

默认值：起始时间为00:00:00（小时=0，分钟=0）

> **说明：**
> 
> 1. 仅设置的小时和分钟生效。
> 2. 设置了start或end且为非默认值的场景下，loop不生效。

**Type:** Date

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TimePickerOptions-start?: Date--><!--Device-TimePickerOptions-start?: Date-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

