# NetUidPolicy（系统接口）

Uid Specifies the Internet access policy in background mode.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-policy-export enum NetUidPolicy--><!--Device-policy-export enum NetUidPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_POLICY_NONE

```TypeScript
NET_POLICY_NONE = 0
```

Default net policy.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidPolicy-NET_POLICY_NONE = 0--><!--Device-NetUidPolicy-NET_POLICY_NONE = 0-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_POLICY_ALLOW_METERED_BACKGROUND

```TypeScript
NET_POLICY_ALLOW_METERED_BACKGROUND = 1 << 0
```

Allow on metered networks when app in background.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidPolicy-NET_POLICY_ALLOW_METERED_BACKGROUND = 1 << 0--><!--Device-NetUidPolicy-NET_POLICY_ALLOW_METERED_BACKGROUND = 1 << 0-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_POLICY_REJECT_METERED_BACKGROUND

```TypeScript
NET_POLICY_REJECT_METERED_BACKGROUND = 1 << 1
```

Reject on metered networks when app in background.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidPolicy-NET_POLICY_REJECT_METERED_BACKGROUND = 1 << 1--><!--Device-NetUidPolicy-NET_POLICY_REJECT_METERED_BACKGROUND = 1 << 1-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

