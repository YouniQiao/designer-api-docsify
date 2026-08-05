# Filter

Defines the filter criteria.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-agent-interface Filter--><!--Device-agent-interface Filter-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## action

```TypeScript
action?: Action
```

Task action. - **UPLOAD**: Upload tasks. - **DOWNLOAD**: Download tasks. - If this parameter is not set, all tasks are queried.

**Type:** Action

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-action?: Action--><!--Device-Filter-action?: Action-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## after

```TypeScript
after?: long
```

Unix timestamp of the start time, in milliseconds. The default value is the invoking time minus 24 hours.

**Type:** long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-after?: long--><!--Device-Filter-after?: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## before

```TypeScript
before?: long
```

Unix timestamp of the end time, in milliseconds. The default value is the invoking time.

**Type:** long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-before?: long--><!--Device-Filter-before?: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## mode

```TypeScript
mode?: Mode
```

Task mode. - **FOREGROUND**: foreground task. - **BACKGROUND**: background task. - If this parameter is not set, all tasks are queried.

**Type:** Mode

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-mode?: Mode--><!--Device-Filter-mode?: Mode-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## state

```TypeScript
state?: State
```

Task state. If this parameter is not set, all tasks are queried.

**Type:** State

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Filter-state?: State--><!--Device-Filter-state?: State-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

