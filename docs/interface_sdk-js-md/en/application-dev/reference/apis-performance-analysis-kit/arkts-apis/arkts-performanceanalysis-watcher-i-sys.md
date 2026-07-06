# Watcher (System API)

Defines a watcher for event subscription.

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
```

## onEvent

```TypeScript
onEvent: (info: SysEventInfo) => void
```

Callback for event subscription: (info: [SysEventInfo](arkts-performanceanalysis-syseventinfo-i-sys.md)) => void

**Type:** (info: SysEventInfo) => void

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## onServiceDied

```TypeScript
onServiceDied: () => void
```

Callback for disabling of event subscription: () => void

**Type:** () => void

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## rules

```TypeScript
rules: WatchRule[]
```

Array of matching event subscription rules.

**Type:** WatchRule[]

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

