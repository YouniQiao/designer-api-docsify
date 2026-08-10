# DomainPluginGetAccountInfoFunc (System API)

```TypeScript
type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,
    callback: AsyncCallback<DomainAccountInfo>) => void
```

查询指定域账号的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,    callback: AsyncCallback<DomainAccountInfo>) => void--><!--Device-osAccount-type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,    callback: AsyncCallback<DomainAccountInfo>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetDomainAccountInfoPluginOptions](arkts-basicservices-osaccount-getdomainaccountinfopluginoptions-i-sys.md) | Yes | 表示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DomainAccountInfo&gt; | Yes | 表示查询结果回调。 |

