# NetUidRule（系统接口）

Rules whether an uid can access to a metered or non-metered network.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-policy-export enum NetUidRule--><!--Device-policy-export enum NetUidRule-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_RULE_NONE

```TypeScript
NET_RULE_NONE = 0
```

Default uid rule.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidRule-NET_RULE_NONE = 0--><!--Device-NetUidRule-NET_RULE_NONE = 0-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_RULE_ALLOW_METERED_FOREGROUND

```TypeScript
NET_RULE_ALLOW_METERED_FOREGROUND = 1 << 0
```

Allow traffic on metered networks while app is foreground.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidRule-NET_RULE_ALLOW_METERED_FOREGROUND = 1 << 0--><!--Device-NetUidRule-NET_RULE_ALLOW_METERED_FOREGROUND = 1 << 0-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_RULE_ALLOW_METERED

```TypeScript
NET_RULE_ALLOW_METERED = 1 << 1
```

Allow traffic on metered network.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidRule-NET_RULE_ALLOW_METERED = 1 << 1--><!--Device-NetUidRule-NET_RULE_ALLOW_METERED = 1 << 1-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_RULE_REJECT_METERED

```TypeScript
NET_RULE_REJECT_METERED = 1 << 2
```

Reject traffic on metered network.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidRule-NET_RULE_REJECT_METERED = 1 << 2--><!--Device-NetUidRule-NET_RULE_REJECT_METERED = 1 << 2-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_RULE_ALLOW_ALL

```TypeScript
NET_RULE_ALLOW_ALL = 1 << 5
```

Allow traffic on all network (metered or non-metered).

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidRule-NET_RULE_ALLOW_ALL = 1 << 5--><!--Device-NetUidRule-NET_RULE_ALLOW_ALL = 1 << 5-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

## NET_RULE_REJECT_ALL

```TypeScript
NET_RULE_REJECT_ALL = 1 << 6
```

Reject traffic on all network.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-NetUidRule-NET_RULE_REJECT_ALL = 1 << 6--><!--Device-NetUidRule-NET_RULE_REJECT_ALL = 1 << 6-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

