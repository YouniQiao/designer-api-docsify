# VerifyPinHandler

VerifyPinHandler is a class in the Web component that handles PIN code verification requests. It is used to enhance app security in scenarios requiring identity authentication on web pages (such as secure payment, sensitive operation confirmation, etc.). When user PIN authentication is required, this handler is provided to the app through the onVerifyPin event callback, allowing the app to respond to the PIN verification result, effectively preventing unauthorized access and protecting user privacy. For sample code, see [onVerifyPin](arkts-arkweb-web-attribute.md#onverifypin).

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## confirm

```TypeScript
confirm(result: PinVerifyResult): void
```

Notifies the Web component of the PIN authentication result. The app calls this method to return the PIN verification result to the Web component, which then continues the subsequent authentication process based on the result. If the verification is successful, the Web component allows access to protected content; if the verification fails, the Web component denies access and may prompt the user to retry.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [PinVerifyResult](arkts-arkweb-pinverifyresult-e.md) | Yes |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **VerifyPinHandler** instance.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core
