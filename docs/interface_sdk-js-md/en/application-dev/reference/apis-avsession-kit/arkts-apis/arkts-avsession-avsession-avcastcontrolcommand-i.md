# AVCastControlCommand

The definition of cast command to be sent to the session

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVCastControlCommand--><!--Device-avSession-interface AVCastControlCommand-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## command

```TypeScript
command: AVCastControlCommandType
```

The command value \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_

**Type:** AVCastControlCommandType

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastControlCommand-command: AVCastControlCommandType--><!--Device-AVCastControlCommand-command: AVCastControlCommandType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## parameter

```TypeScript
parameter?: media.PlaybackSpeed | double | string | LoopMode
```

Parameter carried in the command.The seek command must carry the number parameter.The setVolume command must carry the number parameter.The toggleFavorite command must carry the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ parameter.The setSpeed command must carry the \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ parameter.The setLoopMode command must carry the \_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ parameter.Other commands do not need to carry parameters.

**Type:** media.PlaybackSpeed \| double \| string \| LoopMode

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastControlCommand-parameter?: media.PlaybackSpeed | double | string | LoopMode--><!--Device-AVCastControlCommand-parameter?: media.PlaybackSpeed | double | string | LoopMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

