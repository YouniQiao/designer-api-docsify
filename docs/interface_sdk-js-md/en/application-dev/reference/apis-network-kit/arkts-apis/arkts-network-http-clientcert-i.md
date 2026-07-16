# ClientCert

The clientCert field of the client certificate, which includes 4 attributes:client certificate (cert), client certificate type (certType), certificate private key (key), and passphrase (keyPassword).

**Since:** 12

<!--Device-http-export interface ClientCert--><!--Device-http-export interface ClientCert-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
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

## certType

```TypeScript
certType?: CertType
```

The type of the client certificate.

**Type:** CertType

**Since:** 12

<!--Device-ClientCert-certType?: CertType--><!--Device-ClientCert-certType?: CertType-End-->

**System capability:** SystemCapability.Communication.NetStack

## keyPassword

```TypeScript
keyPassword?: string
```

Password required to use the client certificate private key.

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

