# DomainPluginAuthWithTokenFunc (System API)

```TypeScript
type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,
    token: Uint8Array, callback: IUserAuthCallback) => void
```

Authenticates the specified domain account with an authorization token.

**Since:** 23

<!--Device-osAccount-type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,    token: Uint8Array, callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,    token: Uint8Array, callback: IUserAuthCallback) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Indicates the domain account information for authentication. |
| token | Uint8Array | Yes | Indicates the authorization token generated when PIN or biometric authentication is successful. |
| callback | IUserAuthCallback | Yes | Indicates the callback for notifying the authentication result. |

