# AuthTipCallback

```TypeScript
type AuthTipCallback = (authTipInfo: AuthTipInfo) => void
```

Defines the callback to return the intermediate authentication status. This callback is used to obtain various intermediate status information during authentication, including authentication failure, lockout, and loading and release of the authentication screen. By subscribing to these intermediate statuses, the application can provide more refined user interaction and status management during the authentication process.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-userAuth-type AuthTipCallback = (authTipInfo: AuthTipInfo) => void--><!--Device-userAuth-type AuthTipCallback = (authTipInfo: AuthTipInfo) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authTipInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Intermediate authentication status. It contains the authentication type ( **tipType**) and status code (**tipCode**). The application should perform the corresponding processing based on the value of **tipCode**: \_\_\_HTML\_TAG\_USD\_0\_\_\_- **COMPARE\_FAILURE(1)**: Prompt the user to try again. \_\_\_HTML\_TAG\_USD\_1\_\_\_- **TIMEOUT(2)**: Prompt the user that the operation has timed out. \_\_\_HTML\_TAG\_USD\_2\_\_\_- **TEMPORARILY\_LOCKED(3)**: Prompt the user to wait for unlocking. \_\_\_HTML\_TAG\_USD\_3\_\_\_- **PERMANENTLY\_LOCKED(4)**: Prompt the user to use PIN authentication. \_\_\_HTML\_TAG\_USD\_4\_\_\_- **WIDGET\_LOADED(5)**: The authentication screen has been loaded and initialization can be performed. \_\_\_HTML\_TAG\_USD\_5\_\_\_- **WIDGET\_RELEASED(6)**: The authentication screen has been released, and the subsequent operations can be performed. \_\_\_HTML\_TAG\_USD\_6\_\_\_- **COMPARE\_FAILURE\_WITH\_FROZEN(7)**: Prompt the user that the authentication fails and the authenticator is locked.  |

