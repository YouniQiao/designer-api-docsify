# OnClientAuthenticationEvent

Defines the triggered callback when needs ssl client certificate from the user.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface OnClientAuthenticationEvent--><!--Device-unnamed-export declare interface OnClientAuthenticationEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: ClientAuthenticationHandler
```

Notifies the user of the operation behavior of the web component.

**Type:** [ClientAuthenticationHandler](arkts-web-clientauthenticationhandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-OnClientAuthenticationEvent-handler: ClientAuthenticationHandler--><!--Device-OnClientAuthenticationEvent-handler: ClientAuthenticationHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## host

```TypeScript
host: string
```

The hostname of the requesting certificate server.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-OnClientAuthenticationEvent-host: string--><!--Device-OnClientAuthenticationEvent-host: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## issuers

```TypeScript
issuers: Array<string>
```

Certificates that match the private key are acceptable to the issuer.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-OnClientAuthenticationEvent-issuers: Array<string>--><!--Device-OnClientAuthenticationEvent-issuers: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## keyTypes

```TypeScript
keyTypes: Array<string>
```

Acceptable asymmetric key types.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-OnClientAuthenticationEvent-keyTypes: Array<string>--><!--Device-OnClientAuthenticationEvent-keyTypes: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## port

```TypeScript
port: int
```

The port number of the request certificate server.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-OnClientAuthenticationEvent-port: int--><!--Device-OnClientAuthenticationEvent-port: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

