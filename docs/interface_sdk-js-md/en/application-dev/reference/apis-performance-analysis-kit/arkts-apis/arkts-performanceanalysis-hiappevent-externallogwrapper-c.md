# ExternalLogWrapper

The wrapper of external log, providing various information.

**Since:** 26.1.0

<!--Device-hiAppEvent-class ExternalLogWrapper--><!--Device-hiAppEvent-class ExternalLogWrapper-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## getFilePath

```TypeScript
getFilePath(): string
```

Get the file path

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ExternalLogWrapper-getFilePath(): string--><!--Device-ExternalLogWrapper-getFilePath(): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| string | The file path |

## getGenerationTime

```TypeScript
getGenerationTime(): long
```

Get the generation time point (ms) of the file

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ExternalLogWrapper-getGenerationTime(): long--><!--Device-ExternalLogWrapper-getGenerationTime(): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| long | The generation time |

## getSizeInKb

```TypeScript
getSizeInKb(): long
```

Get the file size in kb

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ExternalLogWrapper-getSizeInKb(): long--><!--Device-ExternalLogWrapper-getSizeInKb(): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| long | The file size in kb |

## getSysEvent

```TypeScript
getSysEvent(): string
```

Get the system event of the file

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ExternalLogWrapper-getSysEvent(): string--><!--Device-ExternalLogWrapper-getSysEvent(): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| string | The string form of system event |

