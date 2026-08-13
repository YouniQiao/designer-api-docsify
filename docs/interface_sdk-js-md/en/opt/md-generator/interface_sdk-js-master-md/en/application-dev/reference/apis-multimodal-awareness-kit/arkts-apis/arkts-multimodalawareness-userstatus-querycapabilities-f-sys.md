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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-userStatus-function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]--><!--Device-userStatus-function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| capabilities | [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-service-exception) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
