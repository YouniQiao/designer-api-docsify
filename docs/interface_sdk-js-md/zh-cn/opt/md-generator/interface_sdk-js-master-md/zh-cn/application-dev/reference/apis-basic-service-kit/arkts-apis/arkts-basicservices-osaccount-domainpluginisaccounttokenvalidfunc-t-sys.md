# DomainPluginIsAccountTokenValidFunc（系统接口）

```TypeScript
type DomainPluginIsAccountTokenValidFunc = (
    domainAccountInfo: DomainAccountInfo,
    token: Uint8Array,
    callback: AsyncCallback<boolean>
  ) => void
```

检查指定的域账号令牌是否有效。

**起始版本：** 23

**废弃版本：** -1

<!--Device-osAccount-type DomainPluginIsAccountTokenValidFunc = (    domainAccountInfo: DomainAccountInfo,    token: Uint8Array,    callback: AsyncCallback<boolean>  ) => void--><!--Device-osAccount-type DomainPluginIsAccountTokenValidFunc = (    domainAccountInfo: DomainAccountInfo,    token: Uint8Array,    callback: AsyncCallback<boolean>  ) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| token | Uint8Array | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |
