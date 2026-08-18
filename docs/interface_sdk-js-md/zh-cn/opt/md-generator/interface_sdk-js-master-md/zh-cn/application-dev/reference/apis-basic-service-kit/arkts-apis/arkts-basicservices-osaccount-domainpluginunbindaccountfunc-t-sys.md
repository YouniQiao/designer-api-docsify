# DomainPluginUnbindAccountFunc（系统接口）

```TypeScript
type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<void>) => void
```

解绑指定的域账号。

**起始版本：** 23

<!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void--><!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
