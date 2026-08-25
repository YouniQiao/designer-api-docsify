# getGlobalWindowMode

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getGlobalWindowMode

```TypeScript
function getGlobalWindowMode(displayId?: number): Promise<number>
```

Obtains the window mode of the window that is in the foreground lifecycle on the specified screen. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
