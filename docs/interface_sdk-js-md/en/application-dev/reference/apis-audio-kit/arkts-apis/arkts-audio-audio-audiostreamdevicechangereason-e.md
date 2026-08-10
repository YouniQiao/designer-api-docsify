# AudioStreamDeviceChangeReason

表示流设备变更原因的枚举。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-audio-enum AudioStreamDeviceChangeReason--><!--Device-audio-enum AudioStreamDeviceChangeReason-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## REASON_UNKNOWN

```TypeScript
REASON_UNKNOWN = 0
```

未知原因。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioStreamDeviceChangeReason-REASON_UNKNOWN = 0--><!--Device-AudioStreamDeviceChangeReason-REASON_UNKNOWN = 0-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## REASON_NEW_DEVICE_AVAILABLE

```TypeScript
REASON_NEW_DEVICE_AVAILABLE = 1
```

新设备可用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioStreamDeviceChangeReason-REASON_NEW_DEVICE_AVAILABLE = 1--><!--Device-AudioStreamDeviceChangeReason-REASON_NEW_DEVICE_AVAILABLE = 1-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## REASON_OLD_DEVICE_UNAVAILABLE

```TypeScript
REASON_OLD_DEVICE_UNAVAILABLE = 2
```

旧设备不可用。报告此原因时，应考虑暂停音频播放。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioStreamDeviceChangeReason-REASON_OLD_DEVICE_UNAVAILABLE = 2--><!--Device-AudioStreamDeviceChangeReason-REASON_OLD_DEVICE_UNAVAILABLE = 2-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## REASON_OVERRODE

```TypeScript
REASON_OVERRODE = 3
```

强选。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AudioStreamDeviceChangeReason-REASON_OVERRODE = 3--><!--Device-AudioStreamDeviceChangeReason-REASON_OVERRODE = 3-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## REASON_SESSION_ACTIVATED

```TypeScript
REASON_SESSION_ACTIVATED = 4
```

音频会话已激活。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioStreamDeviceChangeReason-REASON_SESSION_ACTIVATED = 4--><!--Device-AudioStreamDeviceChangeReason-REASON_SESSION_ACTIVATED = 4-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## REASON_STREAM_PRIORITY_CHANGED

```TypeScript
REASON_STREAM_PRIORITY_CHANGED = 5
```

更高优先级的音频流出现导致的系统设备切换。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioStreamDeviceChangeReason-REASON_STREAM_PRIORITY_CHANGED = 5--><!--Device-AudioStreamDeviceChangeReason-REASON_STREAM_PRIORITY_CHANGED = 5-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

