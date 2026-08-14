# setLogLevel

## Modules to Import

```TypeScript
import { hilog } from 'hilog';
```

## setLogLevel

```TypeScript
function setLogLevel(level: LogLevel, prefer: PreferStrategy): void
```

Sets the minimum log level of the current application process. You can configure different preference strategies using the **prefer** parameter. The **PREFER_CLOSE_LOG** strategy has the same effect as the **setMinLogLevel()** function. > **NOTE：**> > This function does not take effect for debug applications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hilog-function setLogLevel(level: LogLevel, prefer: PreferStrategy): void--><!--Device-hilog-function setLogLevel(level: LogLevel, prefer: PreferStrategy): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [LogLevel](arkts-performanceanalysis-hilog-loglevel-e.md) | Yes | Log level. |
| prefer | [PreferStrategy](arkts-performanceanalysis-hilog-preferstrategy-e.md) | Yes | Preference strategy. |

