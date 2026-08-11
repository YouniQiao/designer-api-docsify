# setOutputType

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## setOutputType

```TypeScript
function setOutputType(type: OutputType): OutputType
```

Sets the output type of hilog.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hilog-function setOutputType(type: OutputType): OutputType--><!--Device-hilog-function setOutputType(type: OutputType): OutputType-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [OutputType](arkts-performanceanalysis-hilog-outputtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OutputType](arkts-performanceanalysis-hilog-outputtype-e.md) |

## Examples

```TypeScript
hilog.setOutputType(hilog.OutputType.SHARE_SANDBOX_ONLY);
hilog.info(0x0001, "testTag", 'sandbox log to share sandbox only');
hilog.flush();
```

Sandbox log output.

```TypeScript
05-15 16:57:04.238 40518 40518 I A00001/testTag: sandbox log to share sandbox only
```
