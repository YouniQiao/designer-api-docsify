# Querier (System API)

Defines an event query instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hiSysEvent-interface Querier--><!--Device-hiSysEvent-interface Querier-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from 'hiSysEvent';
```

## onComplete

```TypeScript
onComplete: (reason: int, total: int) => void
```

Callback used to return the query result statistics: (reason: int, total: int) => void

**Type:** (reason: int, total: int) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Querier-onComplete: (reason: int, total: int) => void--><!--Device-Querier-onComplete: (reason: int, total: int) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## onQuery

```TypeScript
onQuery: (infos: SysEventInfo[]) => void
```

Callback used to return the queried system events: (infos: [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md#SysEventInfo-(System-API))[]) => void.

**Type:** (infos: SysEventInfo[]) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Querier-onQuery: (infos: SysEventInfo[]) => void--><!--Device-Querier-onQuery: (infos: SysEventInfo[]) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

