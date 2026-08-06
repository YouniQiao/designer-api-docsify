# @ohos.multimedia.systemSoundManager

This module provides basic capabilities for managing system sound effects, including defining system sound effect types and obtaining system sound effect players.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace systemSoundManager--><!--Device-unnamed-declare namespace systemSoundManager-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createCustomizedToneAttrs](arkts-audio-systemsoundmanager-createcustomizedtoneattrs-f.md#createcustomizedtoneattrs) | Create customized tone attributes. |
| [createSystemSoundPlayer](arkts-audio-systemsoundmanager-createsystemsoundplayer-f.md#createsystemsoundplayer) | Creates a SystemSoundPlayer instance. This function uses a promise to return the result.This player can be used to play some system sounds for media or camera actions. |
| [getSystemSoundManager](arkts-audio-systemsoundmanager-getsystemsoundmanager-f.md#getsystemsoundmanager) | Gets system sound manager for all type sound. |

### Interfaces

| Name | Description |
| --- | --- |
| [SystemSoundManager](arkts-audio-systemsoundmanager-systemsoundmanager-i.md) | System sound manager object. |
| [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) | Tone attributes. |
| [ToneHapticsAttrs](arkts-audio-systemsoundmanager-tonehapticsattrs-i.md) | Haptics attributes in tone scenario. |
| [ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i.md) | Haptics settings in tone scenario. |

### Enums

| Name | Description |
| --- | --- |
| [MediaType](arkts-audio-systemsoundmanager-mediatype-e.md) | Enum for media type. |
| [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Enum for ringtone type. |
| [SystemSoundError](arkts-audio-systemsoundmanager-systemsounderror-e.md) | Error enum for system sound. |
| [SystemSoundType](arkts-audio-systemsoundmanager-systemsoundtype-e.md) | Enumerates the system sound effect types. |
| [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | Enum for system tone type. |
| [ToneCustomizedType](arkts-audio-systemsoundmanager-tonecustomizedtype-e.md) | Enum for tone customized type. |
| [ToneHapticsFeature](arkts-audio-systemsoundmanager-tonehapticsfeature-e.md) | Definition of haptics feature in tone scenario. |
| [ToneHapticsMode](arkts-audio-systemsoundmanager-tonehapticsmode-e.md) | Enum for haptics mode in tone scenario. |
| [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e.md) | Enum for haptics in tone scenario. |

### Types

| Name | Description |
| --- | --- |
| [RingtoneOptions](arkts-audio-systemsoundmanager-ringtoneoptions-t.md) | Interface for ringtone options. |
| [RingtonePlayer](arkts-audio-systemsoundmanager-ringtoneplayer-t.md) | Ringtone player object. |
| [SystemSoundPlayer](arkts-audio-systemsoundmanager-systemsoundplayer-t.md) | Represents the system sound effect player object. |
| [SystemToneOptions](arkts-audio-systemsoundmanager-systemtoneoptions-t.md) | System tone options. |
| [SystemTonePlayer](arkts-audio-systemsoundmanager-systemtoneplayer-t.md) | SystemTone player object. |
| [ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t.md) | Array of tone attributes. |
| [ToneHapticsAttrsArray](arkts-audio-systemsoundmanager-tonehapticsattrsarray-t.md) | Type definition of tone haptics array. |

<!--Del-->
### Constants（系统接口）

| Name | Description |
| --- | --- |
| [TONE_CATEGORY_ALARM](arkts-audio-systemsoundmanager-con-sys.md#tone_category_alarm) | Define the alarm tone category. |
| [TONE_CATEGORY_CONTACTS](arkts-audio-systemsoundmanager-con-sys.md#tone_category_contacts) | Define the contact tone category. |
| [TONE_CATEGORY_NOTIFICATION](arkts-audio-systemsoundmanager-con-sys.md#tone_category_notification) | Define the notification tone category. |
| [TONE_CATEGORY_NOTIFICATION_APP](arkts-audio-systemsoundmanager-con-sys.md#tone_category_notification_app) | Define the app notification tone category. |
| [TONE_CATEGORY_RINGTONE](arkts-audio-systemsoundmanager-con-sys.md#tone_category_ringtone) | Define the ringtone category. |
| [TONE_CATEGORY_TEXT_MESSAGE](arkts-audio-systemsoundmanager-con-sys.md#tone_category_text_message) | Define the text message tone category. |
<!--DelEnd-->

