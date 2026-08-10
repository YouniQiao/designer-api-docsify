# Querier (System API)

系统事件查询者对象接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiSysEvent-interface Querier--><!--Device-hiSysEvent-interface Querier-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
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

查询结果统计的回调方法(reason: int, total: int) => void。

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

返回查询到的系统事件的回调方法(infos: [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md)[]) => void。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-Querier-onQuery: (infos: SysEventInfo[]) => void--><!--Device-Querier-onQuery: (infos: SysEventInfo[]) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| infos | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md)[] | Yes |  |

