# TimeOptions

TimeOptions defines options for the time picker.

Inherits from [CommonOptions](arkts-arkui-arkui-advanced-datepickercomponent-commonoptions-c.md).

**Inheritance/Implementation:** TimeOptions extends [CommonOptions](arkts-arkui-arkui-advanced-datepickercomponent-commonoptions-c.md)

**Since:** 26.0.0

<!--Device-unnamed-export declare class TimeOptions extends CommonOptions--><!--Device-unnamed-export declare class TimeOptions extends CommonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DisplayMode, TimeFormat, DatePickerComponent, DateMode, DatePickerComponentOptions, DatePickerComponentResult } from '@kit.ArkUI';
```

## format

```TypeScript
format?: TimeFormat
```

Defines the format of the time picker.

Default value: TimeFormat.HOUR_MINUTE

**Type:** TimeFormat

**Default:** TimeFormat.HOUR_MINUTE

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeOptions-format?: TimeFormat--><!--Device-TimeOptions-format?: TimeFormat-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useMilitaryTime

```TypeScript
useMilitaryTime?: boolean
```

Specifies whether to display time in 24-hour format.

- true: Time is displayed in 24-hour format.  
- false: Time is displayed in 12-hour format.

Default value: false

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeOptions-useMilitaryTime?: boolean--><!--Device-TimeOptions-useMilitaryTime?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

