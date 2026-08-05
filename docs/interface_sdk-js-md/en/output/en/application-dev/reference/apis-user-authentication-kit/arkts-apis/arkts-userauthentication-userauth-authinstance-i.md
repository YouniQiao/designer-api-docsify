# AuthInstance

Implements user authentication.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [userAuth.UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md)

<!--Device-userAuth-interface AuthInstance--><!--Device-userAuth-interface AuthInstance-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## cancel

```TypeScript
cancel: () => void
```

Cancels this authentication. > **NOTE** > > Use the obtained [AuthInstance]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ object to call this API to cancel authentication. > This [AuthInstance]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ must be the object that is currently performing > authentication.

**Type:** () =&gt; void

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [userAuth.UserAuthInstance.cancel](arkts-userauthentication-userauth-userauthinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-AuthInstance-cancel: () => void--><!--Device-AuthInstance-cancel: () => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## off

```TypeScript
off: (name: AuthEventKey) => void
```

Unsubscribes from the user authentication events of the specified type. - **name**: indicates the authentication event type. The value **result** means to unsubscribe from the authentication result, and the value **tip** means to unsubscribe from the authentication tip information. For details, see [AuthEventKey]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. > **NOTE** > > The [AuthInstance]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ instance used to invoke this API must be the one used to > subscribe to the event.

**Type:** (name: AuthEventKey) =&gt; void

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** userAuth.UserAuthInstance.off

<!--Device-AuthInstance-off: (name: AuthEventKey) => void--><!--Device-AuthInstance-off: (name: AuthEventKey) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## on

```TypeScript
on: (name: AuthEventKey, callback: AuthEvent) => void
```

Subscribes to the user authentication events of the specified type. - **name**: indicates the authentication event type. The value **result** means that the callback returns the authentication result, and the value **tip** means that the callback returns the authentication tip information. For details, see [AuthEventKey]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. - **callback**: callback used to return the authentication result or tip information. For details, see [AuthEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. > **NOTE** > > Use the [AuthInstance]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ instance obtained to call this API.

**Type:** (name: AuthEventKey, callback: AuthEvent) =&gt; void

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** userAuth.UserAuthInstance.on

<!--Device-AuthInstance-on: (name: AuthEventKey, callback: AuthEvent) => void--><!--Device-AuthInstance-on: (name: AuthEventKey, callback: AuthEvent) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## start

```TypeScript
start: () => void
```

Starts authentication. > **NOTE** > > Use the obtained [AuthInstance]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ object to call this API for authentication.

**Type:** () =&gt; void

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [userAuth.UserAuthInstance.start](arkts-userauthentication-userauth-userauthinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-AuthInstance-start: () => void--><!--Device-AuthInstance-start: () => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

