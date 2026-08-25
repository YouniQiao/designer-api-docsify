# query

## Modules to Import

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## query

```TypeScript
function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void
```

Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [10600001](../errorcode-faultlogger.md#10600001-service-faulty-or-not-started) |


## query

```TypeScript
function query(faultType: FaultType): Promise<Array<FaultLogInfo>>
```

Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [10600001](../errorcode-faultlogger.md#10600001-service-faulty-or-not-started) |
