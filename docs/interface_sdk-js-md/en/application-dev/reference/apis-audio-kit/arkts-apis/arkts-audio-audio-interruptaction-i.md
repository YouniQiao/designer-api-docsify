# InterruptAction

音频打断/获取焦点事件的回调方法。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.InterruptEvent

<!--Device-audio-interface InterruptAction--><!--Device-audio-interface InterruptAction-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## actionType

```TypeScript
actionType: InterruptActionType
```

事件返回类型。TYPE_ACTIVATED为焦点触发事件，TYPE_INTERRUPT为音频打断事件。

**Type:** [InterruptActionType](arkts-audio-audio-interruptactiontype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.InterruptEvent#eventType

<!--Device-InterruptAction-actionType: InterruptActionType--><!--Device-InterruptAction-actionType: InterruptActionType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## activated

```TypeScript
activated?: boolean
```

焦点获取/释放是否成功。true表示焦点获取/释放成功，false表示焦点获得/释放失败。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.InterruptEvent#hintType

<!--Device-InterruptAction-activated?: boolean--><!--Device-InterruptAction-activated?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## hint

```TypeScript
hint?: InterruptHint
```

打断事件提示。

**Type:** [InterruptHint](arkts-audio-audio-interrupthint-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.InterruptEvent#hintType

<!--Device-InterruptAction-hint?: InterruptHint--><!--Device-InterruptAction-hint?: InterruptHint-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## type

```TypeScript
type?: InterruptType
```

打断事件类型。

**Type:** [InterruptType](arkts-audio-audio-interrupttype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.InterruptEvent#eventType

<!--Device-InterruptAction-type?: InterruptType--><!--Device-InterruptAction-type?: InterruptType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

