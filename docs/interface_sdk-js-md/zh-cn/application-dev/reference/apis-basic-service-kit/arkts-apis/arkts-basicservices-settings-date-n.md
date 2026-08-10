# date

Provides methods for setting time and date formats.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-settings-namespace date--><!--Device-settings-namespace date-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 常量

| 名称 | 说明 |
| --- | --- |
| [DATE_FORMAT](arkts-basicservices-date-con.md#date_format) | Indicates the date format.  &lt;p&gt;The formats {@code mm/dd/yyyy}, {@code dd/mm/yyyy}, and {@code yyyy/mm/dd} are available. |
| [TIME_FORMAT](arkts-basicservices-date-con.md#time_format) | Specifies whether the time is displayed in 12-hour or 24-hour format.  &lt;p&gt;If the value is {@code 12}, the 12-hour format is used. If the value is {@code 24}, the 24-hour format is used. |
| [AUTO_GAIN_TIME](arkts-basicservices-date-con.md#auto_gain_time) | Specifies whether the date, time, and time zone are automatically obtained from the Network Identity and Time Zone (NITZ).  &lt;p&gt;If the value is {@code true}, the information is automatically obtained from NITZ.If the value is {@code false}, the information is not obtained from NITZ. |
| [AUTO_GAIN_TIME_ZONE](arkts-basicservices-date-con.md#auto_gain_time_zone) | Specifies whether the time zone is automatically obtained from NITZ.  &lt;p&gt;If the value is {@code true}, the information is automatically obtained from NITZ. If the value is {@code false}, the information is not obtained from NITZ. |

