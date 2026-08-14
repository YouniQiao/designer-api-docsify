# AVControlCommand

The definition of command to be sent to the session

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-avSession-interface AVControlCommand--><!--Device-avSession-interface AVControlCommand-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## command

```TypeScript
command: AVControlCommandType
```

The command value [AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md#AVControlCommandType)

**Type:** [AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVControlCommand-command: AVControlCommandType--><!--Device-AVControlCommand-command: AVControlCommandType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## commandInfo

```TypeScript
commandInfo?: CommandInfo
```

The command value [CommandInfo](arkts-avsession-avsession-commandinfo-i.md#CommandInfo)

**Type:** [CommandInfo](arkts-avsession-avsession-commandinfo-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AVControlCommand-commandInfo?: CommandInfo--><!--Device-AVControlCommand-commandInfo?: CommandInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## parameter

```TypeScript
parameter?: LoopMode | string | double
```

parameter of the command. Whether this command requires parameters, see AVSessionCommand seek command requires a number parameter setSpeed command requires a number parameter setLoopMode command requires a [LoopMode](arkts-avsession-avsession-loopmode-e.md#LoopMode) parameter. toggleFavorite command requires assetId [assetId](arkts-avsession-avsession-avmetadata-i.md#assetId) parameter other commands need no parameter

**Type:** [LoopMode](arkts-avsession-avsession-loopmode-e.md) \| string \| double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVControlCommand-parameter?: LoopMode | string | double--><!--Device-AVControlCommand-parameter?: LoopMode | string | double-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

