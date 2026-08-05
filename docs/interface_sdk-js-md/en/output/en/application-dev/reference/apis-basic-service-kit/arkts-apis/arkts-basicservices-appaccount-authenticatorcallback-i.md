# AuthenticatorCallback

Provides OAuth authenticator callbacks. > **NOTE** > > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [AuthCallback]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instead.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appAccount.AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)

<!--Device-appAccount-interface AuthenticatorCallback--><!--Device-appAccount-interface AuthenticatorCallback-End-->

**System capability:** SystemCapability.Account.AppAccount

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

Called to redirect a request. > **NOTE** > > This API is supported since API version 8 and deprecated since API version 9. Use \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instead.

**Type:** (request: Want) =&gt; void

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [AppAccount.AuthCallback.onRequestRedirected](arkts-basicservices-appaccount-authcallback-i.md#onrequestredirected)

<!--Device-AuthenticatorCallback-onRequestRedirected: (request: Want) => void--><!--Device-AuthenticatorCallback-onRequestRedirected: (request: Want) => void-End-->

**System capability:** SystemCapability.Account.AppAccount

## onResult

```TypeScript
onResult: (code: number, result: { [key: string]: any }) => void
```

Called to return the result of an authentication request. > **NOTE** > > This API is supported since API version 8 and deprecated since API version 9. Use \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instead.

**Type:** (code: number, result: { [key: string]: any }) =&gt; void

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [AppAccount.AuthCallback.onResult](arkts-basicservices-appaccount-authcallback-i.md#onresult)

<!--Device-AuthenticatorCallback-onResult: (code: number, result: { [key: string]: any }) => void--><!--Device-AuthenticatorCallback-onResult: (code: number, result: { [key: string]: any }) => void-End-->

**System capability:** SystemCapability.Account.AppAccount

