# setOutputTypeByDomainID

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## setOutputTypeByDomainID

```TypeScript
function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<int>, isExclude: boolean): OutputType
```

Sets the output type for hilog for the domainID list.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hilog-function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<int>, isExclude: boolean): OutputType--><!--Device-hilog-function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<int>, isExclude: boolean): OutputType-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [OutputType](arkts-performanceanalysis-hilog-outputtype-e.md) | Yes | output type for hilog. |
| domainIDs | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | domainID list, if isExclude is true, the output type for the domainID list is set to DEFAULT, and the output type for the remaining domainIDs is set to the currently specified output type; if isExclude is false, the output type for the domainID list is set to the currently specified output type, and the output type for the remaining domainIDs is set to DEFAULT |
| isExclude | boolean | Yes | determine whether the domainIDs take effect for the currently specified output type. |

**Return value:**

| Type | Description |
| --- | --- |
| [OutputType](arkts-performanceanalysis-hilog-outputtype-e.md) | previous value of output type. |

