# Querier (System API)

Defines an event query instance.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiSysEvent-interface Querier--><!--Device-hiSysEvent-interface Querier-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
```

## onComplete

ArkTS-Dyn:
```TypeScript
onComplete: (reason: number, total: number) => void
```

ArkTS-Sta:
```TypeScript
onComplete: (reason: int, total: int) => void
```

Callback used to return the query result statistics: (reason: int, total: int) => void

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Querier-onComplete: (reason: int, total: int) => void--><!--Device-Querier-onComplete: (reason: int, total: int) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reason | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| total | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |

## onQuery

```TypeScript
onQuery: (infos: SysEventInfo[]) => void
```

Callback used to return the queried system events: (infos: [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md#SysEventInfo)[]) =>void.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Querier-onQuery: (infos: SysEventInfo[]) => void--><!--Device-Querier-onQuery: (infos: SysEventInfo[]) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| infos | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md)[] | Yes |  |

