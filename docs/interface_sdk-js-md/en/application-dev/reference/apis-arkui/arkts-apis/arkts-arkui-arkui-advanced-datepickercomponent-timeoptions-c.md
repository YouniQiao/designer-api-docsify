# TimeOptions

TimeOptions定义时间选择器的选项。

继承于[CommonOptions](arkts-arkui-arkui-advanced-datepickercomponent-commonoptions-c.md)。

**Inheritance/Implementation:** TimeOptions extends [CommonOptions](arkts-arkui-arkui-advanced-datepickercomponent-commonoptions-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class TimeOptions extends CommonOptions--><!--Device-unnamed-export declare class TimeOptions extends CommonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DisplayMode, TimeFormat, DatePickerComponent, DateMode, DatePickerComponentOptions, DatePickerComponentResult } from 'kits/@kit.ArkUI';
```

## format

```TypeScript
format?: TimeFormat
```

定义时间选择器的格式。

默认值：TimeFormat.HOUR_MINUTE

**Type:** [TimeFormat](arkts-arkui-arkui-advanced-datepickercomponent-timeformat-e.md)

**Default:** TimeFormat.HOUR_MINUTE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimeOptions-format?: TimeFormat--><!--Device-TimeOptions-format?: TimeFormat-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useMilitaryTime

```TypeScript
useMilitaryTime?: boolean
```

指定是否使用24小时制显示时间。

- true：时间以24小时制展示。  
- false：时间以12小时制展示。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimeOptions-useMilitaryTime?: boolean--><!--Device-TimeOptions-useMilitaryTime?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

