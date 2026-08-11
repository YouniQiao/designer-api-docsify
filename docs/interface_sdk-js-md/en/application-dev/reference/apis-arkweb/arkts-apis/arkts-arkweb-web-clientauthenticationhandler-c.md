# ClientAuthenticationHandler

Defines the client certificate request result, related to {@link onClientAuthenticationRequest} method.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ClientAuthenticationHandler--><!--Device-unnamed-export declare class ClientAuthenticationHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## cancel

```TypeScript
cancel(): void
```

Cancel this certificate request.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ClientAuthenticationHandler-cancel(): void--><!--Device-ClientAuthenticationHandler-cancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## confirm

```TypeScript
confirm(priKeyFile: string, certChainFile: string): void
```

Confirm to use the specified private key and client certificate chain.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ClientAuthenticationHandler-confirm(priKeyFile: string, certChainFile: string): void--><!--Device-ClientAuthenticationHandler-confirm(priKeyFile: string, certChainFile: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| priKeyFile | string | Yes | The file that store private key. |
| certChainFile | string | Yes | The file that store client certificate chain. |

## confirm

```TypeScript
confirm(authUri: string): void
```

Confirm to use the authUri.The authUri can be obtained from certificate management.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ClientAuthenticationHandler-confirm(authUri: string): void--><!--Device-ClientAuthenticationHandler-confirm(authUri: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authUri | string | Yes | is the key of credentials.The credentials contain sign info and client certificates info. |

## confirm

```TypeScript
confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void
```

Confirm to use the identify of the certificate. The identify can be obtained from certificate management.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ClientAuthenticationHandler-confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void--><!--Device-ClientAuthenticationHandler-confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identity | string | Yes | The identify of the credential. |
| credentialTypeOrCertChainFile | [CredentialType](arkts-arkweb-web-credentialtype-e.md) \| string | Yes | The type of the credential or the file that store client certificate chain. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ClientAuthenticationHandler-constructor()--><!--Device-ClientAuthenticationHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ignore

```TypeScript
ignore(): void
```

Ignore this certificate request temporarily.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ClientAuthenticationHandler-ignore(): void--><!--Device-ClientAuthenticationHandler-ignore(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

