# @ohos.userIAM.userAuth

**userAuth**模块是OpenHarmony系统中用于用户身份认证的核心模块，提供了设备解锁、支付验证、应用登录等场景下的身份认证能力。 该模块支持多种生物特征认证方式（人脸、指纹）和密码认证（PIN），并提供不同级别的安全信任等级。从API版本26.0.0开始，新增伴随设备认证的方式。 该模块主要用于以下场景： - 设备解锁认证。 - 金融支付验证。 - 应用登录保护。 - 敏感操作确认。

**起始版本：** 23

<!--Device-unnamed-declare namespace userAuth--><!--Device-unnamed-declare namespace userAuth-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getauthinstance) |
| [getAuthLockState](arkts-userauthentication-userauth-getauthlockstate-f.md#getauthlockstate) |
| [getAuthenticator](arkts-userauthentication-userauth-getauthenticator-f.md#getauthenticator) |
| [getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md#getavailablestatus) |
| [getEnrolledState](arkts-userauthentication-userauth-getenrolledstate-f.md#getenrolledstate) |
| [getUserAuthInstance](arkts-userauthentication-userauth-getuserauthinstance-f.md#getuserauthinstance) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getUserAuthWidgetMgr](arkts-userauthentication-userauth-getuserauthwidgetmgr-f-sys.md#getuserauthwidgetmgr系统接口) |
| [queryReusableAuthResult](arkts-userauthentication-userauth-queryreusableauthresult-f-sys.md#queryreusableauthresult系统接口) |
| [registerRemoteAuthCallback](arkts-userauthentication-userauth-registerremoteauthcallback-f-sys.md#registerremoteauthcallback系统接口) |
| [sendNotice](arkts-userauthentication-userauth-sendnotice-f-sys.md#sendnotice系统接口) |
| [unregisterRemoteAuthCallback](arkts-userauthentication-userauth-unregisterremoteauthcallback-f-sys.md#unregisterremoteauthcallback系统接口) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [UserAuth](arkts-userauthentication-userauth-userauth-c.md) |

### 接口

| 名称 |
| --- |
| [AuthEvent](arkts-userauthentication-userauth-authevent-i.md) |
| [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md) |
| [AuthLockState](arkts-userauthentication-userauth-authlockstate-i.md) |
| [AuthParam](arkts-userauthentication-userauth-authparam-i.md) |
| [AuthResult](arkts-userauthentication-userauth-authresult-i.md) |
| [AuthResultInfo](arkts-userauthentication-userauth-authresultinfo-i.md) |
| [AuthTipInfo](arkts-userauthentication-userauth-authtipinfo-i.md) |
| [Authenticator](arkts-userauthentication-userauth-authenticator-i.md) |
| [EnrolledState](arkts-userauthentication-userauth-enrolledstate-i.md) |
| [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md) |
| [IUserAuthCallback](arkts-userauthentication-userauth-iuserauthcallback-i.md) |
| [ReuseUnlockResult](arkts-userauthentication-userauth-reuseunlockresult-i.md) |
| [TipInfo](arkts-userauthentication-userauth-tipinfo-i.md) |
| [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md) |
| [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AuthParam](arkts-userauthentication-userauth-authparam-i-sys.md) |
| [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) |
| [IRemoteAuthCallback](arkts-userauthentication-userauth-iremoteauthcallback-i-sys.md) |
| [UserAuthWidgetMgr](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AuthTrustLevel](arkts-userauthentication-userauth-authtrustlevel-e.md) |
| [AuthenticationResult](arkts-userauthentication-userauth-authenticationresult-e.md) |
| [FaceTips](arkts-userauthentication-userauth-facetips-e.md) |
| [FingerprintTips](arkts-userauthentication-userauth-fingerprinttips-e.md) |
| [ResultCode](arkts-userauthentication-userauth-resultcode-e.md) |
| [ReuseMode](arkts-userauthentication-userauth-reusemode-e.md) |
| [UserAuthResultCode](arkts-userauthentication-userauth-userauthresultcode-e.md) |
| [UserAuthTipCode](arkts-userauthentication-userauth-userauthtipcode-e.md) |
| [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [NoticeType](arkts-userauthentication-userauth-noticetype-e-sys.md) |
| [UserAuthResultCode](arkts-userauthentication-userauth-userauthresultcode-e-sys.md) |
| [UserAuthType](arkts-userauthentication-userauth-userauthtype-e-sys.md) |
| [WindowModeType](arkts-userauthentication-userauth-windowmodetype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AuthCallbackOnResultFunc](arkts-userauthentication-userauth-authcallbackonresultfunc-t.md) |
| [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md) |
| [AuthTipCallback](arkts-userauthentication-userauth-authtipcallback-t.md) |
| [AuthType](arkts-userauthentication-userauth-authtype-t.md) |
| [EventInfo](arkts-userauthentication-userauth-eventinfo-t.md) |
| [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AuthWidgetCallbackSendCommandFunc](arkts-userauthentication-userauth-authwidgetcallbacksendcommandfunc-t-sys.md) |
| [ResultCallback](arkts-userauthentication-userauth-resultcallback-t-sys.md) |
| [WidgetParamCallback](arkts-userauthentication-userauth-widgetparamcallback-t-sys.md) |
<!--DelEnd-->

### 常量

| 名称 |
| --- |
| [MAX_ALLOWABLE_REUSE_DURATION](arkts-userauthentication-userauth-con.md#maxallowablereuseduration) |
| [PERMANENT_LOCKOUT_DURATION](arkts-userauthentication-userauth-con.md#permanentlockoutduration) |
