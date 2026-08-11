# subscribe (System API)

## Modules to Import

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## subscribe

```TypeScript
function subscribe(capability: OnscreenAwarenessCap,
                     callback: Callback<OnscreenAwarenessInfo[]>, 
                     options?: OnscreenAwarenessOptions): void
```

Enables proactive awareness on screen content and subscribes to a screen awareness result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** 
- API version 26.0.0+: ohos.permission.GET_SCREEN_CONTENT or ohos.permission.ONSCREEN_AWARENESS
- API version 23 - 24: ohos.permission.GET_SCREEN_CONTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-onScreen-function subscribe(capability: OnscreenAwarenessCap,                     callback: Callback<OnscreenAwarenessInfo[]>,                      options?: OnscreenAwarenessOptions): void--><!--Device-onScreen-function subscribe(capability: OnscreenAwarenessCap,                     callback: Callback<OnscreenAwarenessInfo[]>,                      options?: OnscreenAwarenessOptions): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capability | [OnscreenAwarenessCap](arkts-multimodalawareness-onscreen-onscreenawarenesscap-i-sys.md) | Yes | Onscreen awareness capability list. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OnscreenAwarenessInfo[]&gt; | Yes | Callback function, which returns the onscreen &lt;br&gt; awareness result. The returned onscreen awareness information list **OnscreenAwarenessInfo[]** &lt;br&gt; contains a maximum of two awareness information items. |
| options | [OnscreenAwarenessOptions](arkts-multimodalawareness-onscreen-onscreenawarenessoptions-i-sys.md) | No | Onscreen awareness parameter list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [34000002](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000002-unsupported-application-or-page) | The application or page is not supported. |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) | Service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to get page content forbidden by &lt;br&gt; permission: ohos.permission.GET_SCREEN_CONTENT or ohos.permission.ONSCREEN_AWARENESS. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission check failed. A non-system application uses the system API. |

