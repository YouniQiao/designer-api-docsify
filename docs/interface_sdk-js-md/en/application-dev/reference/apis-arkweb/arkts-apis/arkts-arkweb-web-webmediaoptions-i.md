# WebMediaOptions

Web媒体策略的配置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WebMediaOptions--><!--Device-unnamed-export declare interface WebMediaOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## audioExclusive

```TypeScript
audioExclusive?: boolean
```

应用内多个Web实例的音频是否独占。

true表示应用内多个Web实例的音频独占，false表示应用内多个Web实例的音频不独占。

默认值：true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebMediaOptions-audioExclusive?: boolean--><!--Device-WebMediaOptions-audioExclusive?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## audioSessionType

```TypeScript
audioSessionType?: AudioSessionType
```

应用中Web音频类型。默认值对应[系统音频流类型](../../../reference/apis-audio-kit/arkts-apis-audio-e.md#streamusage)STREAM_USAGE_MUSIC。设置该参数会改变组件音频类型与系统音频类型映射关系，进而影响ArkWeb音频焦点策略。

**Type:** [AudioSessionType](arkts-arkweb-web-audiosessiontype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebMediaOptions-audioSessionType?: AudioSessionType--><!--Device-WebMediaOptions-audioSessionType?: AudioSessionType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## resumeInterval

```TypeScript
resumeInterval?: int
```

被其他应用暂停的Web音视频能够自动续播的有效期，单位：秒。取值范围：[-2147483648, 2147483647]。resumeInterval值为0时，不自动续播；大于0时，将在该时间内尝试续播；小于0时，将在无限时间内尝试续播。由于近似值原因，该有效期可能存在一秒内的误差。

**说明：**

HLS视频被打断后，回到前台将自动续播，不受该时间控制。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebMediaOptions-resumeInterval?: int--><!--Device-WebMediaOptions-resumeInterval?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

