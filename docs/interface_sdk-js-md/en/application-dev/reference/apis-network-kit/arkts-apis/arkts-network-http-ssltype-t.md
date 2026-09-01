# SslType

```TypeScript
export type SslType = 'TLS' | 'TLCP'
```

Defines the secure communications protocol.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Communication.NetStack

| Type | Description |
| --- | --- |
| 'TLS' | TLS protocol. The value is fixed to **TLS**. |
| 'TLCP' | TLCP protocol. The value is fixed to **TLCP**.    **NOTE：**(1) The certificate supports the following string specifications: - UTF8String (English character set) - PrintableString - IA5String Supported since API Version 22:     - TeletexString    (2) The certificate supports the following extended specifications:     - BasicConstraints (OID 2.5.29.19)     - KeyUsage (OID2.5.29.15)     - SubjectKeyIdentifier (OID2.5.29.14)     - AuthorityKeyIdentifier (OID2.5.29.35)    Supported since API Version 22:     - SubjectAltName (OID 2.5.29.17)     - ExtendedKeyUsage (OID 2.5.29.37) |
