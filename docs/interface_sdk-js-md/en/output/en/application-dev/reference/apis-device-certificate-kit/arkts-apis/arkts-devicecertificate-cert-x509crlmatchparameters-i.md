# X509CRLMatchParameters

Represents the parameters used to match a certificate revocation list (CRL). If no parameter is specified, all CRLs are matched.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface X509CRLMatchParameters--><!--Device-cert-interface X509CRLMatchParameters-End-->

**System capability:** SystemCapability.Security.Cert

## issuer

```TypeScript
issuer?: Array<Uint8Array>
```

CRL issuer, in DER format.

**Type:** Array&lt;Uint8Array&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-issuer?: Array<Uint8Array>--><!--Device-X509CRLMatchParameters-issuer?: Array<Uint8Array>-End-->

**System capability:** SystemCapability.Security.Cert

## maxCRL

```TypeScript
maxCRL?: bigint
```

Maximum value of the CRL number.

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-maxCRL?: bigint--><!--Device-X509CRLMatchParameters-maxCRL?: bigint-End-->

**System capability:** SystemCapability.Security.Cert

## minCRL

```TypeScript
minCRL?: bigint
```

Minimum value of the CRL number.

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-minCRL?: bigint--><!--Device-X509CRLMatchParameters-minCRL?: bigint-End-->

**System capability:** SystemCapability.Security.Cert

## updateDateTime

```TypeScript
updateDateTime?: string
```

CRL update time.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-updateDateTime?: string--><!--Device-X509CRLMatchParameters-updateDateTime?: string-End-->

**System capability:** SystemCapability.Security.Cert

## x509Cert

```TypeScript
x509Cert?: X509Cert
```

Certificate object.

**Type:** X509Cert

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-X509CRLMatchParameters-x509Cert?: X509Cert--><!--Device-X509CRLMatchParameters-x509Cert?: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

