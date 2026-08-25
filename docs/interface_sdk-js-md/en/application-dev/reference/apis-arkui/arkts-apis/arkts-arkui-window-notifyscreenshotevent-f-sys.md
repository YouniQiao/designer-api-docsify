# notifyScreenshotEvent (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## notifyScreenshotEvent

```TypeScript
function notifyScreenshotEvent(eventType: ScreenshotEventType): Promise<void>
```

Notifies a screenshot event. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | [ScreenshotEventType](arkts-arkui-window-screenshoteventtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
