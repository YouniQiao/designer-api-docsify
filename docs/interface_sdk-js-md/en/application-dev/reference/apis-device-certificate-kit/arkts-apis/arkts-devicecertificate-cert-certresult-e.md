# CertResult

表示执行结果的枚举。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cert-enum CertResult--><!--Device-cert-enum CertResult-End-->

**System capability:** SystemCapability.Security.Cert

## INVALID_PARAMS

```TypeScript
INVALID_PARAMS = 401
```

非法入参。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-INVALID_PARAMS = 401--><!--Device-CertResult-INVALID_PARAMS = 401-End-->

**System capability:** SystemCapability.Security.Cert

## NOT_SUPPORT

```TypeScript
NOT_SUPPORT = 801
```

操作不支持。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-NOT_SUPPORT = 801--><!--Device-CertResult-NOT_SUPPORT = 801-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_OUT_OF_MEMORY

```TypeScript
ERR_OUT_OF_MEMORY = 19020001
```

内存错误。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_OUT_OF_MEMORY = 19020001--><!--Device-CertResult-ERR_OUT_OF_MEMORY = 19020001-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_RUNTIME_ERROR

```TypeScript
ERR_RUNTIME_ERROR = 19020002
```

运行时外部错误。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_RUNTIME_ERROR = 19020002--><!--Device-CertResult-ERR_RUNTIME_ERROR = 19020002-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_PARAMETER_CHECK_FAILED

```TypeScript
ERR_PARAMETER_CHECK_FAILED = 19020003
```

参数检查失败。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CertResult-ERR_PARAMETER_CHECK_FAILED = 19020003--><!--Device-CertResult-ERR_PARAMETER_CHECK_FAILED = 19020003-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CRYPTO_OPERATION

```TypeScript
ERR_CRYPTO_OPERATION = 19030001
```

调用三方算法库API出错。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_CRYPTO_OPERATION = 19030001--><!--Device-CertResult-ERR_CRYPTO_OPERATION = 19030001-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_SIGNATURE_FAILURE

```TypeScript
ERR_CERT_SIGNATURE_FAILURE = 19030002
```

证书签名验证错误。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_CERT_SIGNATURE_FAILURE = 19030002--><!--Device-CertResult-ERR_CERT_SIGNATURE_FAILURE = 19030002-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_NOT_YET_VALID

```TypeScript
ERR_CERT_NOT_YET_VALID = 19030003
```

证书尚未生效。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_CERT_NOT_YET_VALID = 19030003--><!--Device-CertResult-ERR_CERT_NOT_YET_VALID = 19030003-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_HAS_EXPIRED

```TypeScript
ERR_CERT_HAS_EXPIRED = 19030004
```

证书过期。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_CERT_HAS_EXPIRED = 19030004--><!--Device-CertResult-ERR_CERT_HAS_EXPIRED = 19030004-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY

```TypeScript
ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 19030005
```

无法获取证书的颁发者。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 19030005--><!--Device-CertResult-ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 19030005-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_KEYUSAGE_NO_CERTSIGN

```TypeScript
ERR_KEYUSAGE_NO_CERTSIGN = 19030006
```

证书的密钥用途不含证书签名。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_KEYUSAGE_NO_CERTSIGN = 19030006--><!--Device-CertResult-ERR_KEYUSAGE_NO_CERTSIGN = 19030006-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE

```TypeScript
ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 19030007
```

证书的密钥用途不含数字签名。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertResult-ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 19030007--><!--Device-CertResult-ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 19030007-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_MAYBE_WRONG_PASSWORD

```TypeScript
ERR_MAYBE_WRONG_PASSWORD = 19030008
```

私钥密码可能不正确。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CertResult-ERR_MAYBE_WRONG_PASSWORD = 19030008--><!--Device-CertResult-ERR_MAYBE_WRONG_PASSWORD = 19030008-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_UNTRUSTED

```TypeScript
ERR_CERT_UNTRUSTED = 19030009
```

证书不受信任。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CERT_UNTRUSTED = 19030009--><!--Device-CertResult-ERR_CERT_UNTRUSTED = 19030009-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_HAS_REVOKED

```TypeScript
ERR_CERT_HAS_REVOKED = 19030010
```

证书已被吊销。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CERT_HAS_REVOKED = 19030010--><!--Device-CertResult-ERR_CERT_HAS_REVOKED = 19030010-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_UNKNOWN_CRITICAL_EXTENSION

```TypeScript
ERR_UNKNOWN_CRITICAL_EXTENSION = 19030011
```

未知的关键扩展。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_UNKNOWN_CRITICAL_EXTENSION = 19030011--><!--Device-CertResult-ERR_UNKNOWN_CRITICAL_EXTENSION = 19030011-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_HOSTNAME_MISMATCH

```TypeScript
ERR_CERT_HOSTNAME_MISMATCH = 19030012
```

证书主机名不匹配。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CERT_HOSTNAME_MISMATCH = 19030012--><!--Device-CertResult-ERR_CERT_HOSTNAME_MISMATCH = 19030012-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_EMAIL_ADDRESS_MISMATCH

```TypeScript
ERR_CERT_EMAIL_ADDRESS_MISMATCH = 19030013
```

证书邮箱地址不匹配。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CERT_EMAIL_ADDRESS_MISMATCH = 19030013--><!--Device-CertResult-ERR_CERT_EMAIL_ADDRESS_MISMATCH = 19030013-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CERT_KEYUSAGE_MISMATCH

```TypeScript
ERR_CERT_KEYUSAGE_MISMATCH = 19030014
```

证书密钥用途不匹配。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CERT_KEYUSAGE_MISMATCH = 19030014--><!--Device-CertResult-ERR_CERT_KEYUSAGE_MISMATCH = 19030014-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CRL_NOT_FOUND

```TypeScript
ERR_CRL_NOT_FOUND = 19030015
```

无法获取证书吊销列表。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CRL_NOT_FOUND = 19030015--><!--Device-CertResult-ERR_CRL_NOT_FOUND = 19030015-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CRL_NOT_YET_VALID

```TypeScript
ERR_CRL_NOT_YET_VALID = 19030016
```

证书吊销列表尚未生效。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CRL_NOT_YET_VALID = 19030016--><!--Device-CertResult-ERR_CRL_NOT_YET_VALID = 19030016-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CRL_HAS_EXPIRED

```TypeScript
ERR_CRL_HAS_EXPIRED = 19030017
```

证书吊销列表已过期。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CRL_HAS_EXPIRED = 19030017--><!--Device-CertResult-ERR_CRL_HAS_EXPIRED = 19030017-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CRL_SIGNATURE_FAILURE

```TypeScript
ERR_CRL_SIGNATURE_FAILURE = 19030018
```

证书吊销列表签名验证失败。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CRL_SIGNATURE_FAILURE = 19030018--><!--Device-CertResult-ERR_CRL_SIGNATURE_FAILURE = 19030018-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_CRL_ISSUER_NOT_FOUND

```TypeScript
ERR_CRL_ISSUER_NOT_FOUND = 19030019
```

无法获取证书吊销列表颁发者。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_CRL_ISSUER_NOT_FOUND = 19030019--><!--Device-CertResult-ERR_CRL_ISSUER_NOT_FOUND = 19030019-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_OCSP_RESPONSE_NOT_FOUND

```TypeScript
ERR_OCSP_RESPONSE_NOT_FOUND = 19030020
```

无法获取在线证书状态协议（OCSP）响应。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_OCSP_RESPONSE_NOT_FOUND = 19030020--><!--Device-CertResult-ERR_OCSP_RESPONSE_NOT_FOUND = 19030020-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_OCSP_RESPONSE_INVALID

```TypeScript
ERR_OCSP_RESPONSE_INVALID = 19030021
```

OCSP响应无效。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_OCSP_RESPONSE_INVALID = 19030021--><!--Device-CertResult-ERR_OCSP_RESPONSE_INVALID = 19030021-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_OCSP_SIGNATURE_FAILURE

```TypeScript
ERR_OCSP_SIGNATURE_FAILURE = 19030022
```

OCSP签名验证失败。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_OCSP_SIGNATURE_FAILURE = 19030022--><!--Device-CertResult-ERR_OCSP_SIGNATURE_FAILURE = 19030022-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_OCSP_CERT_STATUS_UNKNOWN

```TypeScript
ERR_OCSP_CERT_STATUS_UNKNOWN = 19030023
```

OCSP证书状态未知。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_OCSP_CERT_STATUS_UNKNOWN = 19030023--><!--Device-CertResult-ERR_OCSP_CERT_STATUS_UNKNOWN = 19030023-End-->

**System capability:** SystemCapability.Security.Cert

## ERR_NETWORK_TIMEOUT

```TypeScript
ERR_NETWORK_TIMEOUT = 19030024
```

网络连接超时。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertResult-ERR_NETWORK_TIMEOUT = 19030024--><!--Device-CertResult-ERR_NETWORK_TIMEOUT = 19030024-End-->

**System capability:** SystemCapability.Security.Cert

