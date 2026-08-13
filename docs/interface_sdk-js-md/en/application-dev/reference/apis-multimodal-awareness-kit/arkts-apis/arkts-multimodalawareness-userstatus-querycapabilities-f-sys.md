# queryCapabilities (System API)

## Modules to Import

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## queryCapabilities

```TypeScript
function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]
```

Queries device-supported atomic capabilities.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-userStatus-function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]--><!--Device-userStatus-function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capabilities | [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md)[] | Yes | List of atomic capabilities to query. |

**Return value:**

| Type | Description |
| --- | --- |
| [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md)[] | Returns the list of device-supported atomic capabilities. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) | Service exception. Possible causes: &lt;br&gt;1. System error, such as a null pointer and container-related exception. &lt;br&gt;2. Node-API invocation exception, such as invalid Node-API status. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

