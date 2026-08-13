# getLogFile

## Modules to Import

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
```

## getLogFile

```TypeScript
function getLogFile(latestSeconds: int): Array<string>
```

Returns the list of hilog log file paths in the sandbox for the specified recent time period.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hilog-function getLogFile(latestSeconds: int): Array<string>--><!--Device-hilog-function getLogFile(latestSeconds: int): Array<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| latestSeconds | int | Yes | the specified time period from a given number of seconds in the past to the present. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | list of hilog log file paths in the sandbox for the specified rencent time period, with newer files appearing first in the list. |

