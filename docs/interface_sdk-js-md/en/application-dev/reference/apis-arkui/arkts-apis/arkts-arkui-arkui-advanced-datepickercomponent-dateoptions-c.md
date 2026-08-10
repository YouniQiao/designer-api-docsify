# DateOptions

DateOptions定义日期选择器的选项。

继承于[CommonOptions](arkts-arkui-arkui-advanced-datepickercomponent-commonoptions-c.md)。

**Inheritance/Implementation:** DateOptions extends [CommonOptions](arkts-arkui-arkui-advanced-datepickercomponent-commonoptions-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class DateOptions extends CommonOptions--><!--Device-unnamed-export declare class DateOptions extends CommonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DisplayMode, TimeFormat, DatePickerComponent, DateMode, DatePickerComponentOptions, DatePickerComponentResult } from 'kits/@kit.ArkUI';
```

## lunar

```TypeScript
lunar?: boolean
```

指定是否显示农历。

- true：显示为农历。  
- false：不显示为农历。

默认值：false

**说明：**

仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateOptions-lunar?: boolean--><!--Device-DateOptions-lunar?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DateMode
```

定义日期选择器的模式。

默认值：DateMode.DATE

**Type:** [DateMode](arkts-arkui-arkui-advanced-datepickercomponent-datemode-e.md)

**Default:** DateMode.DATE

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DateOptions-mode?: DateMode--><!--Device-DateOptions-mode?: DateMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

