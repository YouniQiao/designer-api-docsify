# offSystemCommonEvent (System API)

## offSystemCommonEvent

```TypeScript
function offSystemCommonEvent(callback?: EventProcess): void
```

Unregister system common event callback

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function offSystemCommonEvent(callback?: EventProcess): void--><!--Device-avSession-function offSystemCommonEvent(callback?: EventProcess): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Used to handle event when the common command is received |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

