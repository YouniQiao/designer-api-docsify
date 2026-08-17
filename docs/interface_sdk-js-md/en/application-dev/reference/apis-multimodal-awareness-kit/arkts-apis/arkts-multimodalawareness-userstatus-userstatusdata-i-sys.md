# UserStatusData (System API)

Defines user status data.

**Since:** 26.0.0

<!--Device-userStatus-export interface UserStatusData--><!--Device-userStatus-export interface UserStatusData-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { userStatus } from 'userStatus';
```

## errCode

```TypeScript
errCode: int
```

Business error code. The value `0` indicates success, and other values indicate failure.

**Type:** int

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserStatusData-errCode: int--><!--Device-UserStatusData-errCode: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## feature

```TypeScript
feature: UserStatusFeature
```

User status detection feature type.

**Type:** [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserStatusData-feature: UserStatusFeature--><!--Device-UserStatusData-feature: UserStatusFeature-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## result

```TypeScript
result: int
```

User status detection result. The value `0` indicates success, and other values indicate failure.

**Type:** int

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserStatusData-result: int--><!--Device-UserStatusData-result: int-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

## status

```TypeScript
status: string
```

Multi-stage detection states under a single perception feature.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserStatusData-status: string--><!--Device-UserStatusData-status: string-End-->

**System capability:** SystemCapability.MultimodalAwareness.UserStatus

**System API:** This is a system API.

