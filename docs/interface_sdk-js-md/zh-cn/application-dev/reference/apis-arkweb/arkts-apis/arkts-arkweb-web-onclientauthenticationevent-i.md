# OnClientAuthenticationEvent

Defines the triggered callback when needs ssl client certificate from the user.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: ClientAuthenticationHandler
```

Notifies the user of the operation behavior of the web component.

**类型：** [ClientAuthenticationHandler](arkts-arkweb-web-clientauthenticationhandler-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## host

```TypeScript
host: string
```

The hostname of the requesting certificate server.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## issuers

```TypeScript
issuers: Array<string>
```

Certificates that match the private key are acceptable to the issuer.

**类型：** Array&lt;string&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## keyTypes

```TypeScript
keyTypes: Array<string>
```

Acceptable asymmetric key types.

**类型：** Array&lt;string&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## port

```TypeScript
port: int
```

The port number of the request certificate server.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core
