# Video

The **Video** component is used to play a video and control its playback. > **NOTE** > > The **Video** component provides only simple video playback features. For complex video playback control > scenarios, consider using the [AVPlayer](../../apis-media-kit/arkts-apis/arkts-media-media-avplayer-i.md) APIs in conjunction with the > XComponent component. > When using **expandSafeArea** to extend into safe areas, the **Video** component's content display area does not > support expansion. > > **Required Permissions** > > To use online videos, you must apply for the ohos.permission.INTERNET permission. For details about how to apply > for a permission, see [Declaring Permissions](../../../security/AccessToken/declare-permissions.md). > > **Child Components** > > Not supported.

## Video

```TypeScript
Video(value: VideoOptions)
```

Defines the constructor of video component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoInterface-(value: VideoOptions): VideoAttribute--><!--Device-VideoInterface-(value: VideoOptions): VideoAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [VideoOptions](arkts-arkui-videooptions-i.md) | Yes | Video information. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [FullscreenInfo](arkts-arkui-fullscreeninfo-i.md) | Describes whether the video is in full-screen playback mode. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer > element's @since version number is higher than inner elements'. This does not affect interface usability. |
| [PlaybackInfo](arkts-arkui-playbackinfo-i.md) | Describes the current progress of video playback. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer > element's @since version number is higher than inner elements'. This does not affect interface usability. |
| [PosterOptions](arkts-arkui-posteroptions-i.md) | Defines display options for the first frame of the video. |
| [PreparedInfo](arkts-arkui-preparedinfo-i.md) | Describes the duration of the video. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer > element's @since version number is higher than inner elements'. This does not affect interface usability. |
| [VideoOptions](arkts-arkui-videooptions-i.md) | Defines the options of the **Video** component. |

### Enums

| Name | Description |
| --- | --- |
| [PlaybackSpeed](arkts-arkui-playbackspeed-e.md) | Enumerates video playback speed options. |
| [SeekMode](arkts-arkui-seekmode-e.md) | Enumerates video seek modes. |

