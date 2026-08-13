# sendControlEvent (System API)

## Modules to Import

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
```

## sendControlEvent

```TypeScript
function sendControlEvent(event: ControlEvent): Promise<void>
```

If the target window is displayed on the screen, you can use this API to send screen control events based on the paragraph information obtained via [onScreen.getPageContent](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md#getPageContent-(System-API)).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.SIMULATE_USER_INPUT

<!--Device-onScreen-function sendControlEvent(event: ControlEvent): Promise<void>--><!--Device-onScreen-function sendControlEvent(event: ControlEvent): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ControlEvent](arkts-multimodalawareness-onscreen-controlevent-i-sys.md) | Yes | Onscreen control event. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [34000005](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000005-target-not-found) | The target is not found. |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) | Service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. An attempt was made to get page content forbidden by &lt;br&gt; permission: ohos.permission.SIMULATE_USER_INPUT. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission check failed. A non-system application uses the system API. |

