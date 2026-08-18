# DomainPluginGetAccountInfoFunc（系统接口）

```TypeScript
type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,
    callback: AsyncCallback<DomainAccountInfo>) => void
```

查询指定域账号的信息。

**起始版本：** 23

<!--Device-osAccount-type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,    callback: AsyncCallback<DomainAccountInfo>) => void--><!--Device-osAccount-type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,    callback: AsyncCallback<DomainAccountInfo>) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GetDomainAccountInfoPluginOptions](arkts-basicservices-osaccount-getdomainaccountinfopluginoptions-i-sys.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; | 是 |
