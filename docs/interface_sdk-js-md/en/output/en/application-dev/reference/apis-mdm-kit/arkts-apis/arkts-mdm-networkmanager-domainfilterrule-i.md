# DomainFilterRule

Represents a domain name filtering rule. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is supported since API version 23.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-networkManager-interface DomainFilterRule--><!--Device-networkManager-interface DomainFilterRule-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## action

```TypeScript
action?: Action
```

Action to take, that is, receive or discard the data packets. This parameter is mandatory when a domain name filtering rule is added. This parameter is optional when a domain name filtering rule is removed. If this parameter is left empty, all [Action]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ chains are cleared, and **domainName** and **appUid** must be also left empty.

**Type:** Action

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainFilterRule-action?: Action--><!--Device-DomainFilterRule-action?: Action-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appUid

```TypeScript
appUid?: string
```

UID of the application.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainFilterRule-appUid?: string--><!--Device-DomainFilterRule-appUid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## direction

```TypeScript
direction?: Direction
```

Direction chains to which the rule applies. This parameter is optional when a domain name filtering rule is added. If this parameter is null or set to output chain or input chain, the output chain takes effect. If this parameter is set to a forward chain, **appUid** must be empty. Otherwise, error code 401 will be returned. This parameter is optional when a domain name filtering rule is removed. If the value is empty, all [Direction]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ chains are cleared, and **domainName** and **appUid** must be empty.

**Type:** Direction

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainFilterRule-direction?: Direction--><!--Device-DomainFilterRule-direction?: Direction-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## domainName

```TypeScript
domainName?: string
```

Domain name. This parameter is mandatory when a domain name filtering rule is added. Segment domain name matching is supported. For example, if \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ is set to \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, then \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_, \_\_\_INLINE\_CODE\_DESC\_USD\_3\_\_\_, and \_\_\_INLINE\_CODE\_DESC\_USD\_4\_\_\_ will be matched, while \_\_\_INLINE\_CODE\_DESC\_USD\_5\_\_\_ will not.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainFilterRule-domainName?: string--><!--Device-DomainFilterRule-domainName?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## family

```TypeScript
family?: number
```

IP protocol version. The value can be **1** (IPv4) or **2** (IPv6).

**Type:** number

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainFilterRule-family?: number--><!--Device-DomainFilterRule-family?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## logType

```TypeScript
logType?: LogType
```

Log type. Currently, only **NFLOG** is supported. This parameter applies only to PCs/2-in-1 devices. This parameter is optional when you add a domain name filtering rule. If configured, it only takes effect when data packets are dropped or rejected. When removing domain name filter rules, this parameter is optional if a chain is cleared. The clearing of the entire chain is not affected. When removing a single rule, the value of this parameter must be the same as that of the rule. Otherwise, the filter rule may have been removed, but logs are still recorded. When removing the same filter rule, you must remove the rule in the sequence in which the rule is added. When obtaining domain name filter rules, the **logType** field can be obtained only when logs take effect.

**Type:** LogType

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DomainFilterRule-logType?: LogType--><!--Device-DomainFilterRule-logType?: LogType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

