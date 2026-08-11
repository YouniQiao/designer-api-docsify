# ToneHapticsSettings

Haptics settings in tone scenario.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-systemSoundManager-interface ToneHapticsSettings--><!--Device-systemSoundManager-interface ToneHapticsSettings-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## Modules to Import

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## hapticsUri

```TypeScript
hapticsUri?: string
```

Haptics uri. Users can set/get this parameter when {@link ToneHapticsSettings#mode} is{@link ToneHapticsMode#NON_SYC}. In other cases, this uri is useless and should be ignored.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ToneHapticsSettings-hapticsUri?: string--><!--Device-ToneHapticsSettings-hapticsUri?: string-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## mode

```TypeScript
mode: ToneHapticsMode
```

Haptics mode.

**Type:** [ToneHapticsMode](arkts-audio-systemsoundmanager-tonehapticsmode-e.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-ToneHapticsSettings-mode: ToneHapticsMode--><!--Device-ToneHapticsSettings-mode: ToneHapticsMode-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

