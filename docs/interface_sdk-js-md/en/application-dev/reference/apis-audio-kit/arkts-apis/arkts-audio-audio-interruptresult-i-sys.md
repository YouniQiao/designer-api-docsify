# InterruptResult (System API)

Describes audio interrupt operation results.

**Since:** 23

<!--Device-audio-interface InterruptResult--><!--Device-audio-interface InterruptResult-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## interruptNode

```TypeScript
interruptNode: int
```

Interrupt node as a unit to receive interrupt change event.

**Type:** int

**Since:** 23

<!--Device-InterruptResult-interruptNode: int--><!--Device-InterruptResult-interruptNode: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**System API:** This is a system API.

## requestResult

```TypeScript
requestResult: InterruptRequestResultType
```

Interrupt request or abandon result.

**Type:** [InterruptRequestResultType](arkts-audio-audio-interruptrequestresulttype-e-sys.md)

**Since:** 23

<!--Device-InterruptResult-requestResult: InterruptRequestResultType--><!--Device-InterruptResult-requestResult: InterruptRequestResultType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Interrupt

**System API:** This is a system API.

