# tracepoint

## Modules to Import

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## tracepoint

```TypeScript
function tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void
```

Adds a trace point for the [@ohos.hiTraceMeter (Performance Tracing)](arkts-hitracemeter.md) logging, which is synchronous.When type is set to **CS** and **SR**, the HiTraceMeter tracing starts. When type is set to **CR** and **SS**, the HiTraceMeter tracing ends. When type is set to **GENERAL**, the HiTraceMeter tracing does not start.The trace points for **CS** and **CR** types must be used as a pair; likewise, trace points for **SR** and **SS** types must also be used together. Otherwise, the start and end trace points of HiTraceMeter cannot match each other.

**Since:** 8

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [HiTraceCommunicationMode](arkts-performanceanalysis-hitracechain-hitracecommunicationmode-e.md) | Yes |
| type | [HiTraceTracepointType](arkts-performanceanalysis-hitracechain-hitracetracepointtype-e.md) | Yes |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Yes |
| msg | string | No |
