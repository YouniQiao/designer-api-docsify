# DomainPluginGetAccessTokenFunc (System API)

```TypeScript
type DomainPluginGetAccessTokenFunc = (options: GetDomainAccessTokenOptions,
    callback: AsyncCallback<Uint8Array>) => void
```

根据指定的选项获取域访问令牌。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginGetAccessTokenFunc = (options: GetDomainAccessTokenOptions,    callback: AsyncCallback<Uint8Array>) => void--><!--Device-osAccount-type DomainPluginGetAccessTokenFunc = (options: GetDomainAccessTokenOptions,    callback: AsyncCallback<Uint8Array>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetDomainAccessTokenOptions](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Yes | 表示获取域访问令牌的选项。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | Yes | 表示结果回调。 |

