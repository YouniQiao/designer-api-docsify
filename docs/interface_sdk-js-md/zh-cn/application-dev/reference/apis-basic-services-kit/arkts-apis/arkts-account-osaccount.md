# @ohos.account.osAccount

本模块提供管理系统账号的基础能力，包括系统账号的添加、删除、查询、设置、订阅、启动等功能。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAccountManager](arkts-basicservices-osaccount-getaccountmanager-f.md) |
| [isDomainAccountSupported](arkts-basicservices-osaccount-isdomainaccountsupported-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getAuthorizationManager](arkts-basicservices-osaccount-getauthorizationmanager-f-sys.md) |
| [getOsAccountSubProfileManager](arkts-basicservices-osaccount-getosaccountsubprofilemanager-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [DomainAccountManager](arkts-basicservices-osaccount-domainaccountmanager-c.md) |
| [DomainServerConfigManager](arkts-basicservices-osaccount-domainserverconfigmanager-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [DomainAccountManager](arkts-basicservices-osaccount-domainaccountmanager-c-sys.md) |
| [InputerManager](arkts-basicservices-osaccount-inputermanager-c-sys.md) |
| [PINAuth](arkts-basicservices-osaccount-pinauth-c-sys.md) |
| [UserAuth](arkts-basicservices-osaccount-userauth-c-sys.md) |
| [UserIdentityManager](arkts-basicservices-osaccount-useridentitymanager-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AccountManager](arkts-basicservices-osaccount-accountmanager-i.md) |
| [CreateOsAccountForDomainOptions](arkts-basicservices-osaccount-createosaccountfordomainoptions-i.md) |
| [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) |
| [DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md) |
| [OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AccountManager](arkts-basicservices-osaccount-accountmanager-i-sys.md) |
| [AcquireAuthorizationOptions](arkts-basicservices-osaccount-acquireauthorizationoptions-i-sys.md) |
| [AcquireAuthorizationResult](arkts-basicservices-osaccount-acquireauthorizationresult-i-sys.md) |
| [AuthOptions](arkts-basicservices-osaccount-authoptions-i-sys.md) |
| [AuthorizationManager](arkts-basicservices-osaccount-authorizationmanager-i-sys.md) |
| [AuthResult](arkts-basicservices-osaccount-authresult-i-sys.md) |
| [AuthStatusInfo](arkts-basicservices-osaccount-authstatusinfo-i-sys.md) |
| [ConstraintChangeInfo](arkts-basicservices-osaccount-constraintchangeinfo-i-sys.md) |
| [ConstraintSourceTypeInfo](arkts-basicservices-osaccount-constraintsourcetypeinfo-i-sys.md) |
| [CreateOsAccountOptions](arkts-basicservices-osaccount-createosaccountoptions-i-sys.md) |
| [CredentialChangeInfo](arkts-basicservices-osaccount-credentialchangeinfo-i-sys.md) |
| [CredentialInfo](arkts-basicservices-osaccount-credentialinfo-i-sys.md) |
| [DomainAccountAuthOptions](arkts-basicservices-osaccount-domainaccountauthoptions-i-sys.md) |
| [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) |
| [DomainPlugin](arkts-basicservices-osaccount-domainplugin-i-sys.md) |
| [EnrolledCredInfo](arkts-basicservices-osaccount-enrolledcredinfo-i-sys.md) |
| [ExecutorProperty](arkts-basicservices-osaccount-executorproperty-i-sys.md) |
| [GetAuthInfoOptions](arkts-basicservices-osaccount-getauthinfooptions-i-sys.md) |
| [GetDomainAccessTokenOptions](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) |
| [GetDomainAccountInfoOptions](arkts-basicservices-osaccount-getdomainaccountinfooptions-i-sys.md) |
| [GetDomainAccountInfoPluginOptions](arkts-basicservices-osaccount-getdomainaccountinfopluginoptions-i-sys.md) |
| [GetInputDataOptions](arkts-basicservices-osaccount-getinputdataoptions-i-sys.md) |
| [GetPropertyRequest](arkts-basicservices-osaccount-getpropertyrequest-i-sys.md) |
| [IIdmCallback](arkts-basicservices-osaccount-iidmcallback-i-sys.md) |
| [IInputData](arkts-basicservices-osaccount-iinputdata-i-sys.md) |
| [IInputer](arkts-basicservices-osaccount-iinputer-i-sys.md) |
| [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) |
| [OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i-sys.md) |
| [OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md) |
| [OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) |
| [OsAccountSubProfileManager](arkts-basicservices-osaccount-osaccountsubprofilemanager-i-sys.md) |
| [OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md) |
| [RemoteAuthOptions](arkts-basicservices-osaccount-remoteauthoptions-i-sys.md) |
| [RemoveOsAccountOptions](arkts-basicservices-osaccount-removeosaccountoptions-i-sys.md) |
| [RequestResult](arkts-basicservices-osaccount-requestresult-i-sys.md) |
| [SetOsAccountTypeOptions](arkts-basicservices-osaccount-setosaccounttypeoptions-i-sys.md) |
| [SetPropertyRequest](arkts-basicservices-osaccount-setpropertyrequest-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AuthIntent](arkts-basicservices-osaccount-authintent-e-sys.md) |
| [AuthorizationResultCode](arkts-basicservices-osaccount-authorizationresultcode-e-sys.md) |
| [AuthSubType](arkts-basicservices-osaccount-authsubtype-e-sys.md) |
| [AuthTrustLevel](arkts-basicservices-osaccount-authtrustlevel-e-sys.md) |
| [AuthType](arkts-basicservices-osaccount-authtype-e-sys.md) |
| [ConstraintSourceType](arkts-basicservices-osaccount-constraintsourcetype-e-sys.md) |
| [CredentialChangeType](arkts-basicservices-osaccount-credentialchangetype-e-sys.md) |
| [FaceTipsCode](arkts-basicservices-osaccount-facetipscode-e-sys.md) |
| [FingerprintTips](arkts-basicservices-osaccount-fingerprinttips-e-sys.md) |
| [GetPropertyType](arkts-basicservices-osaccount-getpropertytype-e-sys.md) |
| [Module](arkts-basicservices-osaccount-module-e-sys.md) |
| [OsAccountSubProfileEvent](arkts-basicservices-osaccount-osaccountsubprofileevent-e-sys.md) |
| [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e-sys.md) |
| [ResultCode](arkts-basicservices-osaccount-resultcode-e-sys.md) |
| [SetPropertyType](arkts-basicservices-osaccount-setpropertytype-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [DomainPluginAuthFunc](arkts-basicservices-osaccount-domainpluginauthfunc-t-sys.md) |
| [DomainPluginAuthWithPopupFunc](arkts-basicservices-osaccount-domainpluginauthwithpopupfunc-t-sys.md) |
| [DomainPluginAuthWithTokenFunc](arkts-basicservices-osaccount-domainpluginauthwithtokenfunc-t-sys.md) |
| [DomainPluginBindAccountFunc](arkts-basicservices-osaccount-domainpluginbindaccountfunc-t-sys.md) |
| [DomainPluginGetAccessTokenFunc](arkts-basicservices-osaccount-domainplugingetaccesstokenfunc-t-sys.md) |
| [DomainPluginGetAccountInfoFunc](arkts-basicservices-osaccount-domainplugingetaccountinfofunc-t-sys.md) |
| [DomainPluginGetAuthStatusInfoFunc](arkts-basicservices-osaccount-domainplugingetauthstatusinfofunc-t-sys.md) |
| [DomainPluginIsAccountTokenValidFunc](arkts-basicservices-osaccount-domainpluginisaccounttokenvalidfunc-t-sys.md) |
| [DomainPluginUnbindAccountFunc](arkts-basicservices-osaccount-domainpluginunbindaccountfunc-t-sys.md) |
<!--DelEnd-->
