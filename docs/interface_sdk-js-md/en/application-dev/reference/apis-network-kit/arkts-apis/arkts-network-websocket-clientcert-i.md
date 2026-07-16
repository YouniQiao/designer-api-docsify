# ClientCert

The clientCert field of the client certificate, which includes three attributes:client certificate (certPath) and only support PEM format, certificate private key (keyPath),and passphrase (keyPassword).

**Since:** 12

<!--Device-webSocket-export interface ClientCert--><!--Device-webSocket-export interface ClientCert-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## certPath

```TypeScript
certPath: string
```

The path to the client certificate file.

**Type:** string

**Since:** 12

<!--Device-ClientCert-certPath: string--><!--Device-ClientCert-certPath: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## keyPassword

```TypeScript
keyPassword?: string
```

Client certificate password.

**Type:** string

**Since:** 12

<!--Device-ClientCert-keyPassword?: string--><!--Device-ClientCert-keyPassword?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## keyPath

```TypeScript
keyPath: string
```

The path of the client certificate private key file.

**Type:** string

**Since:** 12

<!--Device-ClientCert-keyPath: string--><!--Device-ClientCert-keyPath: string-End-->

**System capability:** SystemCapability.Communication.NetStack

