# QueryArg (System API)

Defines arguments for an event query.

**Since:** 23

<!--Device-hiSysEvent-interface QueryArg--><!--Device-hiSysEvent-interface QueryArg-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
```

## beginTime

```TypeScript
beginTime: long
```

Start time of the system event to be queried. The value is a 13-digit timestamp, indicating the number of milliseconds elapsed since 00:00:00:00 on January 1, 1970.

**Type:** long

**Since:** 23

<!--Device-QueryArg-beginTime: long--><!--Device-QueryArg-beginTime: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## endTime

```TypeScript
endTime: long
```

End time of the system event to be queried. The value is a 13-digit timestamp, indicating the number of milliseconds elapsed since 00:00:00:00 on January 1, 1970.

**Type:** long

**Since:** 23

<!--Device-QueryArg-endTime: long--><!--Device-QueryArg-endTime: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## fromSeq

```TypeScript
fromSeq?: long | null | undefined
```

Start SN of the events to be queried. The default value is **-1**

**Type:** long \| null \| undefined

**Since:** 23

<!--Device-QueryArg-fromSeq?: long | null | undefined--><!--Device-QueryArg-fromSeq?: long | null | undefined-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## maxEvents

```TypeScript
maxEvents: long
```

Maximum number of events that can be queried.

**Type:** long

**Since:** 23

<!--Device-QueryArg-maxEvents: long--><!--Device-QueryArg-maxEvents: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## toSeq

```TypeScript
toSeq?: long | null | undefined
```

End SN of the system events to be queried. The default value is **-1**.

**Type:** long \| null \| undefined

**Since:** 23

<!--Device-QueryArg-toSeq?: long | null | undefined--><!--Device-QueryArg-toSeq?: long | null | undefined-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

