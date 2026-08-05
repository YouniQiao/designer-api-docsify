# TlsConfig

TLS config.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-http-export interface TlsConfig--><!--Device-http-export interface TlsConfig-End-->

**System capability:** SystemCapability.Communication.NetStack

## cipherSuites

```TypeScript
cipherSuites?: CipherSuite[]
```

CipherSuites, cipherSuits must match tsl version, otherswise will set all system-supported cipherSuits.

**Type:** CipherSuite[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TlsConfig-tlsVersionMin: TlsVersion--><!--Device-TlsConfig-tlsVersionMin: TlsVersion-End-->

**System capability:** SystemCapability.Communication.NetStack

