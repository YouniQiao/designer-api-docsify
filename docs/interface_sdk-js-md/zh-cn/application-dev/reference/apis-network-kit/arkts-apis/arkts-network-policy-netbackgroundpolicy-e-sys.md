# NetBackgroundPolicy（系统接口）

Indicate whether the application can use metered networks in background.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-policy-export enum NetBackgroundPolicy--><!--Device-policy-export enum NetBackgroundPolicy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_BACKGROUND_POLICY_NONE

```TypeScript
NET_BACKGROUND_POLICY_NONE = 0
```

Default value.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_NONE = 0--><!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_NONE = 0-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_BACKGROUND_POLICY_ENABLE

```TypeScript
NET_BACKGROUND_POLICY_ENABLE = 1
```

Apps can use metered networks on background.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_ENABLE = 1--><!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_ENABLE = 1-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_BACKGROUND_POLICY_DISABLE

```TypeScript
NET_BACKGROUND_POLICY_DISABLE = 2
```

Apps can't use metered networks on background.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_DISABLE = 2--><!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_DISABLE = 2-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_BACKGROUND_POLICY_TRUSTLIST

```TypeScript
NET_BACKGROUND_POLICY_TRUSTLIST = 3
```

Only apps in trustlist can use metered networks on background.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_TRUSTLIST = 3--><!--Device-NetBackgroundPolicy-NET_BACKGROUND_POLICY_TRUSTLIST = 3-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

