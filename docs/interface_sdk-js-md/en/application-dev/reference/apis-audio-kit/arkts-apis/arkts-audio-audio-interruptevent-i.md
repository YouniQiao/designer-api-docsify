# InterruptEvent

音频中断时，应用接收的中断事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface InterruptEvent--><!--Device-audio-interface InterruptEvent-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## eventType

```TypeScript
eventType: InterruptType
```

音频中断事件类型，开始或是结束。

**Type:** [InterruptType](arkts-audio-audio-interrupttype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterruptEvent-eventType: InterruptType--><!--Device-InterruptEvent-eventType: InterruptType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## forceType

```TypeScript
forceType: InterruptForceType
```

操作是由系统强制执行或是由应用程序执行。

**Type:** [InterruptForceType](arkts-audio-audio-interruptforcetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterruptEvent-forceType: InterruptForceType--><!--Device-InterruptEvent-forceType: InterruptForceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## hintType

```TypeScript
hintType: InterruptHint
```

中断提示，用于提供中断事件的相关信息。

**Type:** [InterruptHint](arkts-audio-audio-interrupthint-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-InterruptEvent-hintType: InterruptHint--><!--Device-InterruptEvent-hintType: InterruptHint-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

