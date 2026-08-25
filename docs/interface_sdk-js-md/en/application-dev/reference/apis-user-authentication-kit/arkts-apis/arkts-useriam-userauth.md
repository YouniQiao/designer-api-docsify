# @ohos.userIAM.userAuth(User Authentication)

The **userAuth** module is the core module for user authentication in OpenHarmony. It provides authentication capabilities in scenarios such as device unlocking, payment verification, and application login.This module supports multiple biometric authentication methods (face, fingerprint) and password authentication (PIN), and provides various security trust levels. Since API version 26.0.0, the companion device authentication mode is added.This module applies to the following scenarios:  
- Device unlocking authentication. - Financial payment verification. - Application login protection. - Confirmation for sensitive operations.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAuthenticator(User Authentication)](arkts-userauthentication-userauth-getauthenticator-f.md) |
| [getAuthInstance(User Authentication)](arkts-userauthentication-userauth-getauthinstance-f.md) |
| [getAuthLockState(User Authentication)](arkts-userauthentication-userauth-getauthlockstate-f.md) |
| [getAvailableStatus(User Authentication)](arkts-userauthentication-userauth-getavailablestatus-f.md) |
| [getEnrolledState(User Authentication)](arkts-userauthentication-userauth-getenrolledstate-f.md) |
| [getUserAuthInstance(User Authentication)](arkts-userauthentication-userauth-getuserauthinstance-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getUserAuthWidgetMgr(User Authentication)](arkts-userauthentication-userauth-getuserauthwidgetmgr-f-sys.md) |
| [queryReusableAuthResult(User Authentication)](arkts-userauthentication-userauth-queryreusableauthresult-f-sys.md) |
| [registerRemoteAuthCallback(User Authentication)](arkts-userauthentication-userauth-registerremoteauthcallback-f-sys.md) |
| [sendNotice(User Authentication)](arkts-userauthentication-userauth-sendnotice-f-sys.md) |
| [unregisterRemoteAuthCallback(User Authentication)](arkts-userauthentication-userauth-unregisterremoteauthcallback-f-sys.md) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UserAuth(User Authentication)](arkts-userauthentication-userauth-userauth-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Authenticator(User Authentication)](arkts-userauthentication-userauth-authenticator-i.md) |
| [AuthEvent(User Authentication)](arkts-userauthentication-userauth-authevent-i.md) |
| [AuthInstance(User Authentication)](arkts-userauthentication-userauth-authinstance-i.md) |
| [AuthLockState(User Authentication)](arkts-userauthentication-userauth-authlockstate-i.md) |
| [AuthParam(User Authentication)](arkts-userauthentication-userauth-authparam-i.md) |
| [AuthResult(User Authentication)](arkts-userauthentication-userauth-authresult-i.md) |
| [AuthResultInfo(User Authentication)](arkts-userauthentication-userauth-authresultinfo-i.md) |
| [AuthTipInfo(User Authentication)](arkts-userauthentication-userauth-authtipinfo-i.md) |
| [EnrolledState(User Authentication)](arkts-userauthentication-userauth-enrolledstate-i.md) |
| [IAuthCallback(User Authentication)](arkts-userauthentication-userauth-iauthcallback-i.md) |
| [IUserAuthCallback(User Authentication)](arkts-userauthentication-userauth-iuserauthcallback-i.md) |
| [ReuseUnlockResult(User Authentication)](arkts-userauthentication-userauth-reuseunlockresult-i.md) |
| [TipInfo(User Authentication)](arkts-userauthentication-userauth-tipinfo-i.md) |
| [UserAuthInstance(User Authentication)](arkts-userauthentication-userauth-userauthinstance-i.md) |
| [UserAuthResult(User Authentication)](arkts-userauthentication-userauth-userauthresult-i.md) |
| [WidgetParam(User Authentication)](arkts-userauthentication-userauth-widgetparam-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthParam(User Authentication)](arkts-userauthentication-userauth-authparam-i-sys.md) |
| [IAuthWidgetCallback(User Authentication)](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) |
| [IRemoteAuthCallback(User Authentication)](arkts-userauthentication-userauth-iremoteauthcallback-i-sys.md) |
| [UserAuthWidgetMgr(User Authentication)](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) |
| [WidgetParam(User Authentication)](arkts-userauthentication-userauth-widgetparam-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthenticationResult(User Authentication)](arkts-userauthentication-userauth-authenticationresult-e.md) |
| [AuthTrustLevel(User Authentication)](arkts-userauthentication-userauth-authtrustlevel-e.md) |
| [FaceTips(User Authentication)](arkts-userauthentication-userauth-facetips-e.md) |
| [FingerprintTips(User Authentication)](arkts-userauthentication-userauth-fingerprinttips-e.md) |
| [ResultCode(User Authentication)](arkts-userauthentication-userauth-resultcode-e.md) |
| [ReuseMode(User Authentication)](arkts-userauthentication-userauth-reusemode-e.md) |
| [UserAuthResultCode(User Authentication)](arkts-userauthentication-userauth-userauthresultcode-e.md) |
| [UserAuthTipCode(User Authentication)](arkts-userauthentication-userauth-userauthtipcode-e.md) |
| [UserAuthType(User Authentication)](arkts-userauthentication-userauth-userauthtype-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NoticeType(User Authentication)](arkts-userauthentication-userauth-noticetype-e-sys.md) |
| [UserAuthResultCode(User Authentication)](arkts-userauthentication-userauth-userauthresultcode-e-sys.md) |
| [UserAuthType(User Authentication)](arkts-userauthentication-userauth-userauthtype-e-sys.md) |
| [WindowModeType(User Authentication)](arkts-userauthentication-userauth-windowmodetype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthCallbackOnResultFunc(User Authentication)](arkts-userauthentication-userauth-authcallbackonresultfunc-t.md) |
| [AuthEventKey(User Authentication)](arkts-userauthentication-userauth-autheventkey-t.md) |
| [AuthTipCallback(User Authentication)](arkts-userauthentication-userauth-authtipcallback-t.md) |
| [AuthType(User Authentication)](arkts-userauthentication-userauth-authtype-t.md) |
| [EventInfo(User Authentication)](arkts-userauthentication-userauth-eventinfo-t.md) |
| [SecureLevel(User Authentication)](arkts-userauthentication-userauth-securelevel-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthWidgetCallbackSendCommandFunc(User Authentication)](arkts-userauthentication-userauth-authwidgetcallbacksendcommandfunc-t-sys.md) |
| [ResultCallback(User Authentication)](arkts-userauthentication-userauth-resultcallback-t-sys.md) |
| [WidgetParamCallback(User Authentication)](arkts-userauthentication-userauth-widgetparamcallback-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_ALLOWABLE_REUSE_DURATION(User Authentication)](arkts-userauthentication-userauth-con.md#max_allowable_reuse_duration) |
| [PERMANENT_LOCKOUT_DURATION(User Authentication)](arkts-userauthentication-userauth-con.md#permanent_lockout_duration) |
