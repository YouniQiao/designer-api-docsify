# QueryArg (System API)

Defines arguments for an event query.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiSysEvent-interface QueryArg--><!--Device-hiSysEvent-interface QueryArg-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## beginTime

```TypeScript
beginTime: long
```

Start time of the system event to be queried. The value is a 13-digit timestamp, indicating the number of milliseconds elapsed since 00:00:00:00 on January 1, 1970.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-QueryArg-beginTime: long--><!--Device-QueryArg-beginTime: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## endTime

```TypeScript
endTime: long
```

End time of the system event to be queried. The value is a 13-digit timestamp, indicating the number of milliseconds elapsed since 00:00:00:00 on January 1, 1970.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-QueryArg-endTime: long--><!--Device-QueryArg-endTime: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## fromSeq

```TypeScript
fromSeq?: long
```

Start SN of the events to be queried. The default value is **-1

**Type:** long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-QueryArg-fromSeq?: long--><!--Device-QueryArg-fromSeq?: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## maxEvents

```TypeScript
maxEvents: long
```

Maximum number of events that can be queried.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-QueryArg-maxEvents: long--><!--Device-QueryArg-maxEvents: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## toSeq

```TypeScript
toSeq?: long
```

End SN of the system events to be queried. The default value is **-1**.

**Type:** long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-QueryArg-toSeq?: long--><!--Device-QueryArg-toSeq?: long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

