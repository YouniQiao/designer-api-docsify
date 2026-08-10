# CalendarConfig

日历配置信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-calendarManager-interface CalendarConfig--><!--Device-calendarManager-interface CalendarConfig-End-->

**System capability:** SystemCapability.Applications.CalendarData

## Modules to Import

```TypeScript
import { calendarManager } from 'kits/@kit.CalendarKit';
```

## color

```TypeScript
color?: number | string
```

设置Calendar颜色。值为number时取值范围为0x000000至0xFFFFFF或0x00000000至0xFFFFFFFF，值为string时长度为7或9，如'#FFFFFF'，'#FFFFFFFFF'。不设置时默认值为0xFF0A59F7，输入undefined或错误值时抛异常。

**Type:** number \| string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-CalendarConfig-color?: number | string--><!--Device-CalendarConfig-color?: number | string-End-->

**System capability:** SystemCapability.Applications.CalendarData

## enableReminder

```TypeScript
enableReminder?: boolean
```

是否打开Calendar下所有Event提醒能力。当取值为true时，该Calendar下所有Event具备提醒能力；当取值为false时，不具备提醒能力，默认具备提醒能力。

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-CalendarConfig-enableReminder?: boolean--><!--Device-CalendarConfig-enableReminder?: boolean-End-->

**System capability:** SystemCapability.Applications.CalendarData

