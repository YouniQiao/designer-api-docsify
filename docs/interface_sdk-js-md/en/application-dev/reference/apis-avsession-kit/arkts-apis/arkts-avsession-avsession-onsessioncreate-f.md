# onSessionCreate

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## onSessionCreate

```TypeScript
function onSessionCreate(callback: Callback<AVSessionDescriptor>): void
```

Register session create callback

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC

<!--Device-avSession-function onSessionCreate(callback: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function onSessionCreate(callback: Callback<AVSessionDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt; | Yes | Used to handle ('sessionCreate' command) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |

