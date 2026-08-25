# @ohos.userIAM.userAuth(用户认证)

**userAuth**模块是OpenHarmony系统中用于用户身份认证的核心模块，提供了设备解锁、支付验证、应用登录等场景下的身份认证能力。该模块支持多种生物特征认证方式（人脸、指纹）和密码认证（PIN），并提供不同级别的安全信任等级。从API版本26.0.0开始，新增伴随设备认证的方式。该模块主要用于以下场景：  
- 设备解锁认证。 - 金融支付验证。 - 应用登录保护。 - 敏感操作确认。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAuthenticator(用户认证)](arkts-userauthentication-userauth-getauthenticator-f.md) |
| [getAuthInstance(用户认证)](arkts-userauthentication-userauth-getauthinstance-f.md) |
| [getAuthLockState(用户认证)](arkts-userauthentication-userauth-getauthlockstate-f.md) |
| [getAvailableStatus(用户认证)](arkts-userauthentication-userauth-getavailablestatus-f.md) |
| [getEnrolledState(用户认证)](arkts-userauthentication-userauth-getenrolledstate-f.md) |
| [getUserAuthInstance(用户认证)](arkts-userauthentication-userauth-getuserauthinstance-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getUserAuthWidgetMgr(用户认证)](arkts-userauthentication-userauth-getuserauthwidgetmgr-f-sys.md) |
| [queryReusableAuthResult(用户认证)](arkts-userauthentication-userauth-queryreusableauthresult-f-sys.md) |
| [registerRemoteAuthCallback(用户认证)](arkts-userauthentication-userauth-registerremoteauthcallback-f-sys.md) |
| [sendNotice(用户认证)](arkts-userauthentication-userauth-sendnotice-f-sys.md) |
| [unregisterRemoteAuthCallback(用户认证)](arkts-userauthentication-userauth-unregisterremoteauthcallback-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [UserAuth(用户认证)](arkts-userauthentication-userauth-userauth-c.md) |

### 接口

| 名称 |
| --- |
| [Authenticator(用户认证)](arkts-userauthentication-userauth-authenticator-i.md) |
| [AuthEvent(用户认证)](arkts-userauthentication-userauth-authevent-i.md) |
| [AuthInstance(用户认证)](arkts-userauthentication-userauth-authinstance-i.md) |
| [AuthLockState(用户认证)](arkts-userauthentication-userauth-authlockstate-i.md) |
| [AuthParam(用户认证)](arkts-userauthentication-userauth-authparam-i.md) |
| [AuthResult(用户认证)](arkts-userauthentication-userauth-authresult-i.md) |
| [AuthResultInfo(用户认证)](arkts-userauthentication-userauth-authresultinfo-i.md) |
| [AuthTipInfo(用户认证)](arkts-userauthentication-userauth-authtipinfo-i.md) |
| [EnrolledState(用户认证)](arkts-userauthentication-userauth-enrolledstate-i.md) |
| [IAuthCallback(用户认证)](arkts-userauthentication-userauth-iauthcallback-i.md) |
| [IUserAuthCallback(用户认证)](arkts-userauthentication-userauth-iuserauthcallback-i.md) |
| [ReuseUnlockResult(用户认证)](arkts-userauthentication-userauth-reuseunlockresult-i.md) |
| [TipInfo(用户认证)](arkts-userauthentication-userauth-tipinfo-i.md) |
| [UserAuthInstance(用户认证)](arkts-userauthentication-userauth-userauthinstance-i.md) |
| [UserAuthResult(用户认证)](arkts-userauthentication-userauth-userauthresult-i.md) |
| [WidgetParam(用户认证)](arkts-userauthentication-userauth-widgetparam-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AuthParam(用户认证)](arkts-userauthentication-userauth-authparam-i-sys.md) |
| [IAuthWidgetCallback(用户认证)](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) |
| [IRemoteAuthCallback(用户认证)](arkts-userauthentication-userauth-iremoteauthcallback-i-sys.md) |
| [UserAuthWidgetMgr(用户认证)](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) |
| [WidgetParam(用户认证)](arkts-userauthentication-userauth-widgetparam-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AuthenticationResult(用户认证)](arkts-userauthentication-userauth-authenticationresult-e.md) |
| [AuthTrustLevel(用户认证)](arkts-userauthentication-userauth-authtrustlevel-e.md) |
| [FaceTips(用户认证)](arkts-userauthentication-userauth-facetips-e.md) |
| [FingerprintTips(用户认证)](arkts-userauthentication-userauth-fingerprinttips-e.md) |
| [ResultCode(用户认证)](arkts-userauthentication-userauth-resultcode-e.md) |
| [ReuseMode(用户认证)](arkts-userauthentication-userauth-reusemode-e.md) |
| [UserAuthResultCode(用户认证)](arkts-userauthentication-userauth-userauthresultcode-e.md) |
| [UserAuthTipCode(用户认证)](arkts-userauthentication-userauth-userauthtipcode-e.md) |
| [UserAuthType(用户认证)](arkts-userauthentication-userauth-userauthtype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [NoticeType(用户认证)](arkts-userauthentication-userauth-noticetype-e-sys.md) |
| [UserAuthResultCode(用户认证)](arkts-userauthentication-userauth-userauthresultcode-e-sys.md) |
| [UserAuthType(用户认证)](arkts-userauthentication-userauth-userauthtype-e-sys.md) |
| [WindowModeType(用户认证)](arkts-userauthentication-userauth-windowmodetype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AuthCallbackOnResultFunc(用户认证)](arkts-userauthentication-userauth-authcallbackonresultfunc-t.md) |
| [AuthEventKey(用户认证)](arkts-userauthentication-userauth-autheventkey-t.md) |
| [AuthTipCallback(用户认证)](arkts-userauthentication-userauth-authtipcallback-t.md) |
| [AuthType(用户认证)](arkts-userauthentication-userauth-authtype-t.md) |
| [EventInfo(用户认证)](arkts-userauthentication-userauth-eventinfo-t.md) |
| [SecureLevel(用户认证)](arkts-userauthentication-userauth-securelevel-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AuthWidgetCallbackSendCommandFunc(用户认证)](arkts-userauthentication-userauth-authwidgetcallbacksendcommandfunc-t-sys.md) |
| [ResultCallback(用户认证)](arkts-userauthentication-userauth-resultcallback-t-sys.md) |
| [WidgetParamCallback(用户认证)](arkts-userauthentication-userauth-widgetparamcallback-t-sys.md) |
<!--DelEnd-->

### 常量

| 名称 |
| --- |
| [MAX_ALLOWABLE_REUSE_DURATION(用户认证)](arkts-userauthentication-userauth-con.md#max_allowable_reuse_duration) |
| [PERMANENT_LOCKOUT_DURATION(用户认证)](arkts-userauthentication-userauth-con.md#permanent_lockout_duration) |
