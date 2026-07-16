# LimitAction (System API)

The action when quota policy hit the limit.

**Since:** 10

<!--Device-policy-export enum LimitAction--><!--Device-policy-export enum LimitAction-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## LIMIT_ACTION_NONE

```TypeScript
LIMIT_ACTION_NONE = -1
```

Default action, do nothing.

**Since:** 10

<!--Device-LimitAction-LIMIT_ACTION_NONE = -1--><!--Device-LimitAction-LIMIT_ACTION_NONE = -1-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## LIMIT_ACTION_ACCESS_DISABLED

```TypeScript
LIMIT_ACTION_ACCESS_DISABLED = 0
```

When the quota policy reaches the limit, the system prohibits users from accessing the network.

**Since:** 10

<!--Device-LimitAction-LIMIT_ACTION_ACCESS_DISABLED = 0--><!--Device-LimitAction-LIMIT_ACTION_ACCESS_DISABLED = 0-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## LIMIT_ACTION_ALERT_ONLY

```TypeScript
LIMIT_ACTION_ALERT_ONLY = 1
```

When the quota policy reaches the upper limit, the system notifies the user.

**Since:** 10

<!--Device-LimitAction-LIMIT_ACTION_ALERT_ONLY = 1--><!--Device-LimitAction-LIMIT_ACTION_ALERT_ONLY = 1-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

