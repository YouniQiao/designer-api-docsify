# isLoggable

## Modules to Import

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
```

## isLoggable

```TypeScript
function isLoggable(domain: number, tag: string, level: LogLevel): boolean
```

Checks whether logs are printable based on the specified service domain, log tag, and log level.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hilog-function isLoggable(domain: int, tag: string, level: LogLevel): boolean--><!--Device-hilog-function isLoggable(domain: int, tag: string, level: LogLevel): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domain | number | Yes |
| tag | string | Yes |
| level | [LogLevel](arkts-performanceanalysis-hilog-loglevel-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
hilog.isLoggable(0x0001, "testTag", hilog.LogLevel.INFO);
```
