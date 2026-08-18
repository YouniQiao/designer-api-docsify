# @ohos.multimedia.systemSoundManager

系统声音管理提供管理系统声音的基础能力，包括对系统音效类型的定义、获取系统音效播放器等。

**起始版本：** 23

<!--Device-unnamed-declare namespace systemSoundManager--><!--Device-unnamed-declare namespace systemSoundManager-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [createSystemSoundPlayer](arkts-audio-systemsoundmanager-createsystemsoundplayer-f.md#createsystemsoundplayer) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createCustomizedToneAttrs](arkts-audio-systemsoundmanager-createcustomizedtoneattrs-f-sys.md#createcustomizedtoneattrs系统接口) |
| [getSystemSoundManager](arkts-audio-systemsoundmanager-getsystemsoundmanager-f-sys.md#getsystemsoundmanager系统接口) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [SystemSoundManager](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md) |
| [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i-sys.md) |
| [ToneHapticsAttrs](arkts-audio-systemsoundmanager-tonehapticsattrs-i-sys.md) |
| [ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SystemSoundType](arkts-audio-systemsoundmanager-systemsoundtype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [MediaType](arkts-audio-systemsoundmanager-mediatype-e-sys.md) |
| [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e-sys.md) |
| [SystemSoundError](arkts-audio-systemsoundmanager-systemsounderror-e-sys.md) |
| [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e-sys.md) |
| [ToneCustomizedType](arkts-audio-systemsoundmanager-tonecustomizedtype-e-sys.md) |
| [ToneHapticsFeature](arkts-audio-systemsoundmanager-tonehapticsfeature-e-sys.md) | 枚举，系统振动风格定义。 \| 名称 \| 值 \| 说明 \| \| ----------------------------- \| -- \| -------------------- \| \| STANDARD\| 0 \| 标准振动风格。 \| \| GENTLE \| 1 \| 轻柔振动风格。 \|
| [ToneHapticsMode](arkts-audio-systemsoundmanager-tonehapticsmode-e-sys.md) | 枚举，系统铃音场景的振动模式。 \| 名称 \| 值 \| 说明 \| \| ----------------------------- \| -- \| -------------------- \| \| NONE \| 0 \| 无振动模式。 \| \| SYNC \| 1 \| 与铃音同步模式。 \| \| NON_SYNC \| 2 \| 非同步模式。 \|
| [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [SystemSoundPlayer](arkts-audio-systemsoundmanager-systemsoundplayer-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [RingtoneOptions](arkts-audio-systemsoundmanager-ringtoneoptions-t-sys.md) |
| [RingtonePlayer](arkts-audio-systemsoundmanager-ringtoneplayer-t-sys.md) |
| [SystemToneOptions](arkts-audio-systemsoundmanager-systemtoneoptions-t-sys.md) |
| [SystemTonePlayer](arkts-audio-systemsoundmanager-systemtoneplayer-t-sys.md) |
| [ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t-sys.md) |
| [ToneHapticsAttrsArray](arkts-audio-systemsoundmanager-tonehapticsattrsarray-t-sys.md) |
<!--DelEnd-->

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [TONE_CATEGORY_ALARM](arkts-audio-systemsoundmanager-con-sys.md#tonecategoryalarm) |
| [TONE_CATEGORY_CONTACTS](arkts-audio-systemsoundmanager-con-sys.md#tonecategorycontacts) |
| [TONE_CATEGORY_NOTIFICATION](arkts-audio-systemsoundmanager-con-sys.md#tonecategorynotification) |
| [TONE_CATEGORY_NOTIFICATION_APP](arkts-audio-systemsoundmanager-con-sys.md#tonecategorynotificationapp) |
| [TONE_CATEGORY_RINGTONE](arkts-audio-systemsoundmanager-con-sys.md#tonecategoryringtone) |
| [TONE_CATEGORY_TEXT_MESSAGE](arkts-audio-systemsoundmanager-con-sys.md#tonecategorytextmessage) |
<!--DelEnd-->
