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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-avSession-function offSessionServiceDie(callback?: NoParamCallback): void--><!--Device-avSession-function offSessionServiceDie(callback?: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | No | Used to unregister listener for ('sessionServiceDie') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-avsession-kit/errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

