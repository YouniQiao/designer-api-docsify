# AVControlCommand

The definition of command to be sent to the session

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVControlCommand--><!--Device-avSession-interface AVControlCommand-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## command

```TypeScript
command: AVControlCommandType
```

The command value {@link AVControlCommandType}

**Type:** [AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVControlCommand-command: AVControlCommandType--><!--Device-AVControlCommand-command: AVControlCommandType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## commandInfo

```TypeScript
commandInfo?: CommandInfo
```

The command value {@link CommandInfo}

**Type:** [CommandInfo](arkts-avsession-avsession-commandinfo-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AVControlCommand-commandInfo?: CommandInfo--><!--Device-AVControlCommand-commandInfo?: CommandInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## parameter

```TypeScript
parameter?: LoopMode | string | double
```

parameter of the command. Whether this command requires parameters, see {@link AVSessionCommand}seek command requires a number parameter setSpeed command requires a number parameter setLoopMode command requires a {@link LoopMode} parameter.toggleFavorite command requires assetId {@link AVMetadata.assetId} parameter other commands need no parameter

**Type:** ArkTS-Dyn: [LoopMode](arkts-avsession-avsession-loopmode-e.md) \| string \| number  <br>ArkTS-Sta：[LoopMode](arkts-avsession-avsession-loopmode-e.md) \| string \| double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVControlCommand-parameter?: LoopMode | string | double--><!--Device-AVControlCommand-parameter?: LoopMode | string | double-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

