# offReadingScreenPermissionListener (System API)

## Modules to Import

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## offReadingScreenPermissionListener

```TypeScript
function offReadingScreenPermissionListener(callback?: Callback<ReadingScreenPermissionStatus>): void
```

Disables the screen content access permission monitoring.

**Since:** 23

**Required permissions:** ohos.permission.GET_SCREEN_CONTENT

**Model restriction:** This API can be used only in the stage model.

<!--Device-onScreen-function offReadingScreenPermissionListener(callback?: Callback<ReadingScreenPermissionStatus>): void--><!--Device-onScreen-function offReadingScreenPermissionListener(callback?: Callback<ReadingScreenPermissionStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ReadingScreenPermissionStatus&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import onScreen from "@ohos.multimodalAwareness.onScreen";
try {
  onScreen.offReadingScreenPermissionListener();
  console.info(`offReadingScreenPermissionListener succeeded.`);
} catch (err) {
  console.error('offReadingScreenPermissionListener failed, errCode = ' + err.code);
}
```
