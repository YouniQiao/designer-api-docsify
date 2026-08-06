# Constants

## AFFECTED_MODE_RINGER_STREAMS

```TypeScript
const AFFECTED_MODE_RINGER_STREAMS: string
```

Specifies which audio streams are affected by changes on the ringing mode and Do Not Disturb (DND) mode.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_If you want a specific audio stream to be affected by changes of the ringing mode and DDN mode, set the corresponding bit to {@code 1}.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const AFFECTED_MODE_RINGER_STREAMS: string--><!--Device-sound-const AFFECTED_MODE_RINGER_STREAMS: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## AFFECTED_MUTE_STREAMS

```TypeScript
const AFFECTED_MUTE_STREAMS: string
```

Specifies which audio streams are affected by the mute mode.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_If you want a specific audio stream to remain muted in mute mode, set the corresponding bit to {@code 1}.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const AFFECTED_MUTE_STREAMS: string--><!--Device-sound-const AFFECTED_MUTE_STREAMS: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## DEFAULT_ALARM_ALERT

```TypeScript
const DEFAULT_ALARM_ALERT: string
```

Indicates the storage area of the system default alarm.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can obtain the URI of the system default alarm.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const DEFAULT_ALARM_ALERT: string--><!--Device-sound-const DEFAULT_ALARM_ALERT: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## DEFAULT_NOTIFICATION_SOUND

```TypeScript
const DEFAULT_NOTIFICATION_SOUND: string
```

Indicates the storage area of the system default notification tone.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can obtain the URI of the system default notification tone.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const DEFAULT_NOTIFICATION_SOUND: string--><!--Device-sound-const DEFAULT_NOTIFICATION_SOUND: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## DEFAULT_RINGTONE

```TypeScript
const DEFAULT_RINGTONE: string
```

Indicates the storage area of the system default ringtone.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can obtain the URI of the system default ringtone.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const DEFAULT_RINGTONE: string--><!--Device-sound-const DEFAULT_RINGTONE: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## DTMF_TONE_TYPE_WHILE_DIALING

```TypeScript
const DTMF_TONE_TYPE_WHILE_DIALING: string
```

Indicates the type of the dual-tone multifrequency (DTMF) tone played when dialing.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_The value {@code 0} indicates the normal short sound effect, and {@code 1} indicates the long sound effect.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const DTMF_TONE_TYPE_WHILE_DIALING: string--><!--Device-sound-const DTMF_TONE_TYPE_WHILE_DIALING: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## DTMF_TONE_WHILE_DIALING

```TypeScript
const DTMF_TONE_WHILE_DIALING: string
```

Specifies whether the DTMF tone is played when dialing.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_If the value is {@code 1}, the DTMF tone is played. If the value is {@code 0}, the DTMF tone is not played.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const DTMF_TONE_WHILE_DIALING: string--><!--Device-sound-const DTMF_TONE_WHILE_DIALING: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## HAPTIC_FEEDBACK_STATUS

```TypeScript
const HAPTIC_FEEDBACK_STATUS: string
```

Indicates whether the device enables haptic feedback.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_The value is of the boolean type.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const HAPTIC_FEEDBACK_STATUS: string--><!--Device-sound-const HAPTIC_FEEDBACK_STATUS: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## SOUND_EFFECTS_STATUS

```TypeScript
const SOUND_EFFECTS_STATUS: string
```

Specifies whether the sound effects are enabled.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_If the value is {@code 0}, the sound effects are disabled. If the value is {@code 1}, the sound effects are enabled.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const SOUND_EFFECTS_STATUS: string--><!--Device-sound-const SOUND_EFFECTS_STATUS: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## VIBRATE_STATUS

```TypeScript
const VIBRATE_STATUS: string
```

Specifies whether the device vibrates for an event. This parameter is used inside the system.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_If the value is {@code 1}, the device vibrates for an event. If the value is {@code 0}, the device does not vibrate for an event.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const VIBRATE_STATUS: string--><!--Device-sound-const VIBRATE_STATUS: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## VIBRATE_WHILE_RINGING

```TypeScript
const VIBRATE_WHILE_RINGING: string
```

Indicates whether the device vibrates when it is ringing for an incoming call.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This constant will be used by Phone and Settings applications. The value is of the boolean type.This constant affects only the scenario where the device rings for an incoming call. It does not affect any other application or scenario.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 21

<!--Device-sound-const VIBRATE_WHILE_RINGING: string--><!--Device-sound-const VIBRATE_WHILE_RINGING: string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

