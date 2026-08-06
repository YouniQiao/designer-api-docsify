# AVRecorderConfig

Describes the audio and video recording parameters.

The **audioSourceType** and **videoSourceType** parameters are used to distinguish audio-only recording,video-only recording, and audio and video recording. For audio-only recording, set only **audioSourceType**.For video-only recording, set only **videoSourceType**. For audio and video recording, set both **audioSourceType**  
and **videoSourceType**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-media-interface AVRecorderConfig--><!--Device-media-interface AVRecorderConfig-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## audioSourceType

```TypeScript
audioSourceType?: AudioSourceType
```

Type of the audio source to record. This parameter is mandatory for audio recording.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**Atomic service API**:  
This API can be used in atomic services since API version 12.

**Type:** AudioSourceType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderConfig-audioSourceType?: AudioSourceType--><!--Device-AVRecorderConfig-audioSourceType?: AudioSourceType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## fileGenerationMode

```TypeScript
fileGenerationMode?: FileGenerationMode
```

Mode for creating the file, which is used together with on('photoAssetAvailable').

**Type:** FileGenerationMode

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-fileGenerationMode?: FileGenerationMode--><!--Device-AVRecorderConfig-fileGenerationMode?: FileGenerationMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## location

```TypeScript
location?: Location
```

Geographical location of the recorded video. By default, the geographical location information is not recorded.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This API is supported since API version 6 and deprecated since API version 12. You are advised to use  
**AVMetadata.location** instead. If both parameters are set, **AVMetadata.location** is used.

**Type:** Location

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** ohos.multimedia.media/media.AVMetadata#location

<!--Device-AVRecorderConfig-location?: Location--><!--Device-AVRecorderConfig-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## maxDuration

```TypeScript
maxDuration?: int
```

Maximum recording duration, in seconds. The value range is [1, 2^31-1]. If an invalid value is provided,it is reset to the maximum allowed duration. Once the recording reaches the specified duration,it stops automatically and notifies via the **stateChange** callback that the recording has stopped:AVRecorderState = 'stopped', StateChangeReason = BACKGROUND.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-maxDuration?: int--><!--Device-AVRecorderConfig-maxDuration?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## metadata

```TypeScript
metadata?: AVMetadata
```

Metadata. For details, see @AVMetadata.

**Type:** AVMetadata

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-metadata?: AVMetadata--><!--Device-AVRecorderConfig-metadata?: AVMetadata-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## profile

```TypeScript
profile: AVRecorderProfile
```

Recording profile. This parameter is mandatory.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**Atomic service API**: This API can be used in atomic services since API version 12.

**Type:** AVRecorderProfile

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderConfig-profile: AVRecorderProfile--><!--Device-AVRecorderConfig-profile: AVRecorderProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## rotation

```TypeScript
rotation?: number
```

Rotation angle of the recorded video, in degrees. The value can be 0 (default), 90, 180, or 270 for MP4 videos.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This API is supported since API version 6 and deprecated since API version 12. You are advised to use.  
**AVMetadata.videoOrientation** instead. If both parameters are set, **AVMetadata.videoOrientation** is used.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** ohos.multimedia.media/media.AVMetadata#videoOrientation

<!--Device-AVRecorderConfig-rotation?: number--><!--Device-AVRecorderConfig-rotation?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## url

```TypeScript
url: string
```

Recording output URL: fd://xx (fd number).\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This parameter is mandatory.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**Atomic service API**:  
This API can be used in atomic services since API version 12.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderConfig-url: string--><!--Device-AVRecorderConfig-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoSourceType

```TypeScript
videoSourceType?: VideoSourceType
```

Type of the video source to record. This parameter is mandatory for video recording.

**Type:** VideoSourceType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-videoSourceType?: VideoSourceType--><!--Device-AVRecorderConfig-videoSourceType?: VideoSourceType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

