# setOutputTypeByDomainID

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## setOutputTypeByDomainID

```TypeScript
function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<number>, isExclude: boolean): OutputType
```

Sets the output type for hilog for the domainID list.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hilog-function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<int>, isExclude: boolean): OutputType--><!--Device-hilog-function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<int>, isExclude: boolean): OutputType-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [OutputType](arkts-performanceanalysis-hilog-outputtype-e.md) | Yes |
| domainIDs | Array&lt;number&gt; | Yes |
| isExclude | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OutputType](arkts-performanceanalysis-hilog-outputtype-e.md) |

## Examples

```TypeScript
hilog.setOutputTypeByDomainID(hilog.OutputType.SHARE_SANDBOX_ONLY, [0x0001, 0x0002, 0x0003], false);
hilog.info(0x0001, "testTag", 'sandbox log to share sandbox only');
hilog.info(0x0002, "testTag", 'sandbox log to share sandbox only');
hilog.info(0x0003, "testTag", 'sandbox log to share sandbox only');
hilog.info(0x0004, "testTag", 'sandbox log to share sandbox only');
hilog.flush();
```

Sandbox log output. The logs of domain 0x0004 are not printed.

```TypeScript
05-15 16:57:04.238 40518 40518 I A00001/testTag: sandbox log to share sandbox only
05-15 16:57:04.238 40518 40518 I A00002/testTag: sandbox log to share sandbox only
05-15 16:57:04.238 40518 40518 I A00003/testTag: sandbox log to share sandbox only
```
