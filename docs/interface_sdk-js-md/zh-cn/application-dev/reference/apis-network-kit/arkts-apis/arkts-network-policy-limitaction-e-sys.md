# LimitAction（系统接口）

The action when quota policy hit the limit.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-policy-export enum LimitAction--><!--Device-policy-export enum LimitAction-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## LIMIT_ACTION_NONE

```TypeScript
LIMIT_ACTION_NONE = -1
```

Default action, do nothing.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-LimitAction-LIMIT_ACTION_NONE = -1--><!--Device-LimitAction-LIMIT_ACTION_NONE = -1-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## LIMIT_ACTION_ACCESS_DISABLED

```TypeScript
LIMIT_ACTION_ACCESS_DISABLED = 0
```

When the quota policy reaches the limit, the system prohibits users from accessing the network.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-LimitAction-LIMIT_ACTION_ACCESS_DISABLED = 0--><!--Device-LimitAction-LIMIT_ACTION_ACCESS_DISABLED = 0-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## LIMIT_ACTION_ALERT_ONLY

```TypeScript
LIMIT_ACTION_ALERT_ONLY = 1
```

When the quota policy reaches the upper limit, the system notifies the user.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-LimitAction-LIMIT_ACTION_ALERT_ONLY = 1--><!--Device-LimitAction-LIMIT_ACTION_ALERT_ONLY = 1-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

