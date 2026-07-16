# TlsConfig

TLS config.

**Since:** 18

<!--Device-http-export interface TlsConfig--><!--Device-http-export interface TlsConfig-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## cipherSuites

```TypeScript
cipherSuites?: CipherSuite[]
```

CipherSuites, cipherSuits must match tsl version, otherswise will set all system-supported cipherSuits.

**Type:** CipherSuite[]

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TlsConfig-cipherSuites?: CipherSuite[]--><!--Device-TlsConfig-cipherSuites?: CipherSuite[]-End-->

**System capability:** SystemCapability.Communication.NetStack

## tlsVersionMax

```TypeScript
tlsVersionMax: TlsVersion
```

Maximum version num of Tls protocol.

**Type:** TlsVersion

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TlsConfig-tlsVersionMax: TlsVersion--><!--Device-TlsConfig-tlsVersionMax: TlsVersion-End-->

**System capability:** SystemCapability.Communication.NetStack

## tlsVersionMin

```TypeScript
tlsVersionMin: TlsVersion
```

Minimum version num of Tls protocol.

**Type:** TlsVersion

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TlsConfig-tlsVersionMin: TlsVersion--><!--Device-TlsConfig-tlsVersionMin: TlsVersion-End-->

**System capability:** SystemCapability.Communication.NetStack

