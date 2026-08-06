# AVControlCommand

The definition of command to be sent to the session

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVControlCommand--><!--Device-avSession-interface AVControlCommand-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## command

```TypeScript
command: AVControlCommandType
```

The command value \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_

**Type:** AVControlCommandType

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVControlCommand-command: AVControlCommandType--><!--Device-AVControlCommand-command: AVControlCommandType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## commandInfo

```TypeScript
commandInfo?: CommandInfo
```

The command value \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_

**Type:** CommandInfo

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-AVControlCommand-commandInfo?: CommandInfo--><!--Device-AVControlCommand-commandInfo?: CommandInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## parameter

```TypeScript
parameter?: LoopMode | string | double
```

parameter of the command. Whether this command requires parameters, see \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_seek command requires a number parameter setSpeed command requires a number parameter setLoopMode command requires a \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ parameter.toggleFavorite command requires assetId \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ parameter other commands need no parameter

**Type:** LoopMode \| string \| double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVControlCommand-parameter?: LoopMode | string | double--><!--Device-AVControlCommand-parameter?: LoopMode | string | double-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

