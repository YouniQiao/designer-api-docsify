# @ohos.account.appAccount

本模块提供应用账号信息的添加、删除、修改和查询基础能力，并支持应用间鉴权和分布式数据同步功能。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace appAccount--><!--Device-unnamed-declare namespace appAccount-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createAppAccountManager](arkts-basicservices-appaccount-createappaccountmanager-f.md#createappaccountmanager) | 创建应用账号管理器对象。 |

### Classes

| Name | Description |
| --- | --- |
| [Authenticator](arkts-basicservices-appaccount-authenticator-c.md) | 认证器基类。 |

### Interfaces

| Name | Description |
| --- | --- |
| [AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md) | 表示应用账号信息。 |
| [AppAccountManager](arkts-basicservices-appaccount-appaccountmanager-i.md) | 应用账号管理器，可用于管理应用自身的账号信息。 |
| [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 认证器回调类。 |
| [AuthResult](arkts-basicservices-appaccount-authresult-i.md) | 表示认证结果信息。 |
| [AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md) | 表示Auth令牌信息。 |
| [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | OAuth认证器回调接口。 |
| [AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md) | 表示OAuth认证器信息。 |
| [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | 表示隐式创建账号的选项。 |
| [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | 表示创建账号的选项。 |
| [OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md) | 表示OAuth令牌信息。 |
| [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | 表示用于选择账号的选项。 |
| [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | 表示用于设置属性的选项。 |
| [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | 表示用于验证凭据的选项。 |

### Enums

| Name | Description |
| --- | --- |
| [Constants](arkts-basicservices-appaccount-constants-e.md) | 表示常量的枚举。 |
| [ResultCode](arkts-basicservices-appaccount-resultcode-e.md) | 表示返回码的枚举。 |

