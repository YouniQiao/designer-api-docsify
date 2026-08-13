# unsubscribe (System API)

## Modules to Import

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
```

## unsubscribe

```TypeScript
function unsubscribe(capability: OnscreenAwarenessCap, callback?: Callback<OnscreenAwarenessInfo[]>): void
```

Disables proactive awareness on screen content and unsubscribes from a screen awareness result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.GET_SCREEN_CONTENT or ohos.permission.ONSCREEN_AWARENESS
- API version 23 - 24: ohos.permission.GET_SCREEN_CONTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-onScreen-function unsubscribe(capability: OnscreenAwarenessCap, callback?: Callback<OnscreenAwarenessInfo[]>): void--><!--Device-onScreen-function unsubscribe(capability: OnscreenAwarenessCap, callback?: Callback<OnscreenAwarenessInfo[]>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capability | [OnscreenAwarenessCap](arkts-multimodalawareness-onscreen-onscreenawarenesscap-i-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OnscreenAwarenessInfo](arkts-multimodalawareness-onscreen-onscreenawarenessinfo-i-sys.md)[]&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import onScreen from "@ohos.multimodalAwareness.onScreen";
let onscreenAwarenessCap: onScreen.OnscreenAwarenessCap = {
   groupId: 'SmartEdge'
}

try {
  onScreen.unsubscribe(onscreenAwarenessCap, (info: onScreen.OnscreenAwarenessInfo[]) => {
    console.info(`unsubscribe resultCode: ${info[0].resultCode}`);
  });
} catch (err) {
  console.error('unsubscribe failed, errCode = ' + err.code);
}
```
