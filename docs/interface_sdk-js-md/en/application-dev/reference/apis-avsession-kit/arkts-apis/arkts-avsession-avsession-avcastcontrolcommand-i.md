# AVCastControlCommand

投播控制器接受的命令的对象描述。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVCastControlCommand--><!--Device-avSession-interface AVCastControlCommand-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## command

```TypeScript
command: AVCastControlCommandType
```

命令。每种命令对应的参数不同，具体的对应关系可查阅[AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)。

**Type:** [AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastControlCommand-command: AVCastControlCommandType--><!--Device-AVCastControlCommand-command: AVCastControlCommandType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## parameter

```TypeScript
parameter?: media.PlaybackSpeed | double | string | LoopMode
```

命令对应的参数。

**Type:** ArkTS-Dyn: media.PlaybackSpeed \| number \| string \| LoopMode  <br>ArkTS-Sta：media.PlaybackSpeed \| double \| string \| LoopMode

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVCastControlCommand-parameter?: media.PlaybackSpeed | double | string | LoopMode--><!--Device-AVCastControlCommand-parameter?: media.PlaybackSpeed | double | string | LoopMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

