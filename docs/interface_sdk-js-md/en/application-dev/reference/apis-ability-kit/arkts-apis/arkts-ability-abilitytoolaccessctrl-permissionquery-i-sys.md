# PermissionQuery (System API)

权限查询信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-abilityToolAccessCtrl-interface PermissionQuery--><!--Device-abilityToolAccessCtrl-interface PermissionQuery-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## callerTokenId

```TypeScript
callerTokenId?: long
```

主叫token标识。取值范围：(-∞,+∞)。

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-PermissionQuery-callerTokenId?: long--><!--Device-PermissionQuery-callerTokenId?: long-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## domainId

```TypeScript
domainId?: string
```

域ID。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-PermissionQuery-domainId?: string--><!--Device-PermissionQuery-domainId?: string-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## needTicket

```TypeScript
needTicket?: boolean
```

是否需要ticket

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-PermissionQuery-needTicket?: boolean--><!--Device-PermissionQuery-needTicket?: boolean-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## operationInfo

```TypeScript
operationInfo: OperationInfo[]
```

操作信息列表。

**Type:** [OperationInfo](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsubscribe-operationinfo-i-sys.md)[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-PermissionQuery-operationInfo: OperationInfo[]--><!--Device-PermissionQuery-operationInfo: OperationInfo[]-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## remoteInfo

```TypeScript
remoteInfo?: RemoteInfo
```

远端设备信息。

**Type:** [RemoteInfo](arkts-ability-abilitytoolaccessctrl-remoteinfo-i-sys.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

<!--Device-PermissionQuery-remoteInfo?: RemoteInfo--><!--Device-PermissionQuery-remoteInfo?: RemoteInfo-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## ticketExpireTimeMs

```TypeScript
ticketExpireTimeMs?: long
```

凭据过期时间，单位为毫秒。取值范围：(-∞,+∞)。

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-PermissionQuery-ticketExpireTimeMs?: long--><!--Device-PermissionQuery-ticketExpireTimeMs?: long-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

