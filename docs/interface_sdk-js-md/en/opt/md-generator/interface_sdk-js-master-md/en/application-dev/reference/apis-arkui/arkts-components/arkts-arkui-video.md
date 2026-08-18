# Video

The **Video** component is used to play a video and control its playback. > **NOTE** > > The **Video** component provides only simple video playback features. For complex video playback control > scenarios, consider using the [AVPlayer](../../apis-media-kit/arkts-apis/arkts-media-media-avplayer-i.md#avplayer) APIs in conjunction with the > XComponent component. > When using **expandSafeArea** to extend into safe areas, the **Video** component's content display area does not > support expansion. > > **Required Permissions** > > To use online videos, you must apply for the ohos.permission.INTERNET permission. For details about how to apply > for a permission, see [Declaring Permissions](../../../security/AccessToken/declare-permissions.md). > > **Child Components** > > Not supported.

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [VideoOptions](arkts-arkui-videooptions-i.md) | Yes |

## Summary

- [FullscreenInfo](arkts-arkui-fullscreeninfo-i.md)
- [PlaybackInfo](arkts-arkui-playbackinfo-i.md)
- [PosterOptions](arkts-arkui-posteroptions-i.md)
- [PreparedInfo](arkts-arkui-preparedinfo-i.md)
- [VideoOptions](arkts-arkui-videooptions-i.md)
- [PlaybackSpeed](arkts-arkui-playbackspeed-e.md)
- [SeekMode](arkts-arkui-seekmode-e.md)
