# IAuthCallback

Provides callbacks to return the authentication result. This API defines the authentication result callback method, which is used to obtain the authentication result after the authentication is complete. By implementing the **onResult** method, the application can obtain the authentication token when the authentication is successful, or obtain the error code and related information when the authentication fails.

**Since:** 23

<!--Device-userAuth-interface IAuthCallback--><!--Device-userAuth-interface IAuthCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
```

## onResult

```TypeScript
onResult(result: UserAuthResult): void
```

Called to return the authentication result. If the authentication is successful, you can obtain the token information through **UserAuthResult** for subsequent security operation verification. If the authentication fails, you can obtain the error code through the **result** field and take corresponding measures (for example, prompting the user to perform authentication again or guiding the user to register a credential).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IAuthCallback-onResult(result: UserAuthResult): void--><!--Device-IAuthCallback-onResult(result: UserAuthResult): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) | Yes |

## onResult

```TypeScript
onResult: AuthCallbackOnResultFunc
```

Called to return the authentication result. If the authentication is successful, UserAuthResult contains the token information.

**Type:** [AuthCallbackOnResultFunc](arkts-userauthentication-userauth-authcallbackonresultfunc-t.md)

**Since:** 23

<!--Device-IAuthCallback-onResult: AuthCallbackOnResultFunc--><!--Device-IAuthCallback-onResult: AuthCallbackOnResultFunc-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core
