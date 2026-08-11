# sendControlEvent (System API)

## Modules to Import

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## sendControlEvent

```TypeScript
function sendControlEvent(event: ControlEvent): Promise<void>
```

If the target window is displayed on the screen, you can use this API to send screen control events based on the paragraph information obtained via [onScreen.getPageContent](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md#getpagecontent).

**Since:** 20

**Required permissions:** ohos.permission.SIMULATE_USER_INPUT

<!--Device-onScreen-function sendControlEvent(event: ControlEvent): Promise<void>--><!--Device-onScreen-function sendControlEvent(event: ControlEvent): Promise<void>-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [ControlEvent](arkts-multimodalawareness-onscreen-controlevent-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [34000005](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000005-target-not-found) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
