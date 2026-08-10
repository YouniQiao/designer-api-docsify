# DomainPluginGetAuthStatusInfoFunc (System API)

```TypeScript
type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<AuthStatusInfo>) => void
```

查询指定域账号的认证状态信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<AuthStatusInfo>) => void--><!--Device-osAccount-type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<AuthStatusInfo>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 表示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;AuthStatusInfo&gt; | Yes | 表示查询结果回调。 |

