# offSessionServiceDie (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## offSessionServiceDie

```TypeScript
function offSessionServiceDie(callback?: NoParamCallback): void
```

Unregister Session service death callback, notifying the application to clean up resources.

**Since:** 23

**Deprecated since:** -1

<!--Device-avSession-function offSessionServiceDie(callback?: NoParamCallback): void--><!--Device-avSession-function offSessionServiceDie(callback?: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
