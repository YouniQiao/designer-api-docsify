# querySelfFaultLog

## Modules to Import

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## querySelfFaultLog

```TypeScript
function querySelfFaultLog(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void
```

Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** query

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; | Yes |


## querySelfFaultLog

```TypeScript
function querySelfFaultLog(faultType: FaultType): Promise<Array<FaultLogInfo>>
```

Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** query

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; |
