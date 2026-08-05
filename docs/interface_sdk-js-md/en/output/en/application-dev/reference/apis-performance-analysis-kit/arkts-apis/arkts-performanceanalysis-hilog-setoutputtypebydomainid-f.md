# setOutputTypeByDomainID

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
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | output type for hilog. |
| domainIDs | ArkTS-Dyn: Array&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Array&lt;int&gt; | Yes | domainID list, if isExclude is true, the output type for the domainID list is set to DEFAULT, and the output type for the remaining domainIDs is set to the currently specified output type; if isExclude is false, the output type for the domainID list is set to the currently specified output type, and the output type for the remaining domainIDs is set to DEFAULT |
| isExclude | boolean | Yes | determine whether the domainIDs take effect for the currently specified output type. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | previous value of output type. |

