# onSystemCommonEvent (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## onSystemCommonEvent

```TypeScript
function onSystemCommonEvent(callback: EventProcess): void
```

Register system common event callback

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function onSystemCommonEvent(callback: EventProcess): void--><!--Device-avSession-function onSystemCommonEvent(callback: EventProcess): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
