# setMinLogLevel

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## setMinLogLevel

```TypeScript
function setMinLogLevel(level: LogLevel): void
```

Sets the minimum log level.

> **NOTE：**&gt;
> If the set log level is lower than the
> [global log level](../../../dfx/hilog.md#displaying-and-setting-log-levels), the setting does not take effect.&gt;
> This function does not take effect for debug applications.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [LogLevel](arkts-performanceanalysis-hilog-loglevel-e.md) | Yes |
