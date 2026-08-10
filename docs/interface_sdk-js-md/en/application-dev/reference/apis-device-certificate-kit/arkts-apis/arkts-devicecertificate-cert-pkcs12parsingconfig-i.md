# Pkcs12ParsingConfig

表示解析P12的配置。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cert-interface Pkcs12ParsingConfig--><!--Device-cert-interface Pkcs12ParsingConfig-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## needsCert

```TypeScript
needsCert?: boolean
```

表示是否获取证书。默认为true。true为获取，false为不获取。

**Type:** boolean

**Default:** true

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12ParsingConfig-needsCert?: boolean--><!--Device-Pkcs12ParsingConfig-needsCert?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## needsOtherCerts

```TypeScript
needsOtherCerts?: boolean
```

表示是否获取其他证书。默认为false。true为获取，false为不获取。

**Type:** boolean

**Default:** false

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12ParsingConfig-needsOtherCerts?: boolean--><!--Device-Pkcs12ParsingConfig-needsOtherCerts?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## needsPrivateKey

```TypeScript
needsPrivateKey?: boolean
```

表示是否获取私钥。默认为true。

true为获取，返回PKCS8编码的私钥数据；false为不获取。

**Type:** boolean

**Default:** true

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12ParsingConfig-needsPrivateKey?: boolean--><!--Device-Pkcs12ParsingConfig-needsPrivateKey?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## password

```TypeScript
password: string
```

密码。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12ParsingConfig-password: string--><!--Device-Pkcs12ParsingConfig-password: string-End-->

**System capability:** SystemCapability.Security.Cert

## privateKeyFormat

```TypeScript
privateKeyFormat?: EncodingBaseFormat
```

表示获取私钥的格式，当前支持PEM和DER格式。参数缺省时，默认为PEM格式。

> **说明：**
> 
> 当needsPrivateKey值为true时，该参数生效。

**Type:** [EncodingBaseFormat](arkts-devicecertificate-cert-encodingbaseformat-e.md)

**Default:** EncodingBaseFormat.PEM

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Pkcs12ParsingConfig-privateKeyFormat?: EncodingBaseFormat--><!--Device-Pkcs12ParsingConfig-privateKeyFormat?: EncodingBaseFormat-End-->

**System capability:** SystemCapability.Security.Cert

