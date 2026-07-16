# ServerCert

The serverCert field of the server certificate, which includes two attributes:File paths of server certificate (certPath) and certificate private key (keyPath). Only support PEM format.

**Since:** 24

<!--Device-webSocket-export interface ServerCert--><!--Device-webSocket-export interface ServerCert-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## certPath

```TypeScript
certPath: string
```

File path for the server cert.

**Type:** string

**Since:** 24

<!--Device-ServerCert-certPath: string--><!--Device-ServerCert-certPath: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## keyPath

```TypeScript
keyPath: string
```

The path of the server certificate private key file.

**Type:** string

**Since:** 24

<!--Device-ServerCert-keyPath: string--><!--Device-ServerCert-keyPath: string-End-->

**System capability:** SystemCapability.Communication.NetStack

