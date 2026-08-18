# @ohos.userIAM.userAuth

The **userAuth** module is the core module for user authentication in OpenHarmony. It provides authentication capabilities in scenarios such as device unlocking, payment verification, and application login. This module supports multiple biometric authentication methods (face, fingerprint) and password authentication (PIN), and provides various security trust levels. Since API version 26.0.0, the companion device authentication mode is added. This module applies to the following scenarios: - Device unlocking authentication. - Financial payment verification. - Application login protection. - Confirmation for sensitive operations.

**Since:** 23

<!--Device-unnamed-declare namespace userAuth--><!--Device-unnamed-declare namespace userAuth-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getauthinstance) |
| [getAuthLockState](arkts-userauthentication-userauth-getauthlockstate-f.md#getauthlockstate) |
| [getAuthenticator](arkts-userauthentication-userauth-getauthenticator-f.md#getauthenticator) |
| [getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md#getavailablestatus) |
| [getEnrolledState](arkts-userauthentication-userauth-getenrolledstate-f.md#getenrolledstate) |
| [getUserAuthInstance](arkts-userauthentication-userauth-getuserauthinstance-f.md#getuserauthinstance) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getUserAuthWidgetMgr](arkts-userauthentication-userauth-getuserauthwidgetmgr-f-sys.md#getuserauthwidgetmgr-system-api) |
| [queryReusableAuthResult](arkts-userauthentication-userauth-queryreusableauthresult-f-sys.md#queryreusableauthresult-system-api) |
| [registerRemoteAuthCallback](arkts-userauthentication-userauth-registerremoteauthcallback-f-sys.md#registerremoteauthcallback-system-api) |
| [sendNotice](arkts-userauthentication-userauth-sendnotice-f-sys.md#sendnotice-system-api) |
| [unregisterRemoteAuthCallback](arkts-userauthentication-userauth-unregisterremoteauthcallback-f-sys.md#unregisterremoteauthcallback-system-api) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UserAuth](arkts-userauthentication-userauth-userauth-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthParam](arkts-userauthentication-userauth-authparam-i-sys.md) |
| [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) |
| [IRemoteAuthCallback](arkts-userauthentication-userauth-iremoteauthcallback-i-sys.md) |
| [UserAuthWidgetMgr](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NoticeType](arkts-userauthentication-userauth-noticetype-e-sys.md) |
| [UserAuthResultCode](arkts-userauthentication-userauth-userauthresultcode-e-sys.md) |
| [UserAuthType](arkts-userauthentication-userauth-userauthtype-e-sys.md) |
| [WindowModeType](arkts-userauthentication-userauth-windowmodetype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthCallbackOnResultFunc](arkts-userauthentication-userauth-authcallbackonresultfunc-t.md) |
| [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md) |
| [AuthTipCallback](arkts-userauthentication-userauth-authtipcallback-t.md) |
| [AuthType](arkts-userauthentication-userauth-authtype-t.md) |
| [EventInfo](arkts-userauthentication-userauth-eventinfo-t.md) |
| [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthWidgetCallbackSendCommandFunc](arkts-userauthentication-userauth-authwidgetcallbacksendcommandfunc-t-sys.md) |
| [ResultCallback](arkts-userauthentication-userauth-resultcallback-t-sys.md) |
| [WidgetParamCallback](arkts-userauthentication-userauth-widgetparamcallback-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_ALLOWABLE_REUSE_DURATION](arkts-userauthentication-userauth-con.md#maxallowablereuseduration) |
| [PERMANENT_LOCKOUT_DURATION](arkts-userauthentication-userauth-con.md#permanentlockoutduration) |
