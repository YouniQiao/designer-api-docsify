# NetUidRule (System API)

Rules whether an uid can access to a metered or non-metered network.

**Since:** 10

<!--Device-policy-export enum NetUidRule--><!--Device-policy-export enum NetUidRule-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## NET_RULE_NONE

```TypeScript
NET_RULE_NONE = 0
```

Default uid rule.

**Since:** 10

<!--Device-NetUidRule-NET_RULE_NONE = 0--><!--Device-NetUidRule-NET_RULE_NONE = 0-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## NET_RULE_ALLOW_METERED_FOREGROUND

```TypeScript
NET_RULE_ALLOW_METERED_FOREGROUND = 1 << 0
```

Allow traffic on metered networks while app is foreground.

**Since:** 10

<!--Device-NetUidRule-NET_RULE_ALLOW_METERED_FOREGROUND = 1 << 0--><!--Device-NetUidRule-NET_RULE_ALLOW_METERED_FOREGROUND = 1 << 0-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## NET_RULE_ALLOW_METERED

```TypeScript
NET_RULE_ALLOW_METERED = 1 << 1
```

Allow traffic on metered network.

**Since:** 10

<!--Device-NetUidRule-NET_RULE_ALLOW_METERED = 1 << 1--><!--Device-NetUidRule-NET_RULE_ALLOW_METERED = 1 << 1-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## NET_RULE_REJECT_METERED

```TypeScript
NET_RULE_REJECT_METERED = 1 << 2
```

Reject traffic on metered network.

**Since:** 10

<!--Device-NetUidRule-NET_RULE_REJECT_METERED = 1 << 2--><!--Device-NetUidRule-NET_RULE_REJECT_METERED = 1 << 2-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## NET_RULE_ALLOW_ALL

```TypeScript
NET_RULE_ALLOW_ALL = 1 << 5
```

Allow traffic on all network (metered or non-metered).

**Since:** 10

<!--Device-NetUidRule-NET_RULE_ALLOW_ALL = 1 << 5--><!--Device-NetUidRule-NET_RULE_ALLOW_ALL = 1 << 5-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## NET_RULE_REJECT_ALL

```TypeScript
NET_RULE_REJECT_ALL = 1 << 6
```

Reject traffic on all network.

**Since:** 10

<!--Device-NetUidRule-NET_RULE_REJECT_ALL = 1 << 6--><!--Device-NetUidRule-NET_RULE_REJECT_ALL = 1 << 6-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

