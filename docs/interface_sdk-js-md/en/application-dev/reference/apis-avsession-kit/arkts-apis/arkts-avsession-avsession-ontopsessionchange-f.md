# onTopSessionChange

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## onTopSessionChange

```TypeScript
function onTopSessionChange(callback: Callback<AVSessionDescriptor>): void
```

Register top session changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC

<!--Device-avSession-function onTopSessionChange(callback: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function onTopSessionChange(callback: Callback<AVSessionDescriptor>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md)&gt; | Yes | Used to handle ('topSessionChange' command) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |

