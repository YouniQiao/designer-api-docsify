# @ohos.security.cert

证书算法库框架提供证书相关接口。其中，依赖加解密算法库框架的基础算法能力的部分，详细接口说明可参考 [cryptoFramework API参考](../../apis-crypto-architecture-kit/arkts-apis/arkts-security-cryptoframework.md)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Security.Cert

## 导入模块

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [buildX509CertChain](arkts-devicecertificate-cert-buildx509certchain-f.md) |
| [createCertChainValidator](arkts-devicecertificate-cert-createcertchainvalidator-f.md) |
| [createCertCRLCollection](arkts-devicecertificate-cert-createcertcrlcollection-f.md) |
| [createCertExtension](arkts-devicecertificate-cert-createcertextension-f.md) |
| [createCertExtension](arkts-devicecertificate-cert-createcertextension-f.md) |
| [createCmsGenerator](arkts-devicecertificate-cert-createcmsgenerator-f.md) |
| [createCmsParser](arkts-devicecertificate-cert-createcmsparser-f.md) |
| [createPkcs12](arkts-devicecertificate-cert-createpkcs12-f.md) |
| [createPkcs12Sync](arkts-devicecertificate-cert-createpkcs12sync-f.md) |
| [createTrustAnchorsWithKeyStore](arkts-devicecertificate-cert-createtrustanchorswithkeystore-f.md) |
| [createX500DistinguishedName](arkts-devicecertificate-cert-createx500distinguishedname-f.md) |
| [createX500DistinguishedName](arkts-devicecertificate-cert-createx500distinguishedname-f.md) |
| [createX509Cert](arkts-devicecertificate-cert-createx509cert-f.md) |
| [createX509Cert](arkts-devicecertificate-cert-createx509cert-f.md) |
| [createX509CertChain](arkts-devicecertificate-cert-createx509certchain-f.md) |
| [createX509CertChain](arkts-devicecertificate-cert-createx509certchain-f.md) |
| [createX509CertChain](arkts-devicecertificate-cert-createx509certchain-f.md) |
| [createX509Crl](arkts-devicecertificate-cert-createx509crl-f.md) |
| [createX509Crl](arkts-devicecertificate-cert-createx509crl-f.md) |
| [createX509CRL](arkts-devicecertificate-cert-createx509crl-f.md) |
| [createX509CRL](arkts-devicecertificate-cert-createx509crl-f.md) |
| [generateCsr](arkts-devicecertificate-cert-generatecsr-f.md) |
| [parsePkcs12](arkts-devicecertificate-cert-parsepkcs12-f.md) |
| [parsePkcs12](arkts-devicecertificate-cert-parsepkcs12-f.md) |

### 接口

| 名称 |
| --- |
| [CertChainBuildParameters](arkts-devicecertificate-cert-certchainbuildparameters-i.md) |
| [CertChainBuildResult](arkts-devicecertificate-cert-certchainbuildresult-i.md) |
| [CertChainData](arkts-devicecertificate-cert-certchaindata-i.md) |
| [CertChainValidationParameters](arkts-devicecertificate-cert-certchainvalidationparameters-i.md) |
| [CertChainValidationResult](arkts-devicecertificate-cert-certchainvalidationresult-i.md) |
| [CertChainValidator](arkts-devicecertificate-cert-certchainvalidator-i.md) |
| [CertCRLCollection](arkts-devicecertificate-cert-certcrlcollection-i.md) |
| [CertExtension](arkts-devicecertificate-cert-certextension-i.md) |
| [CertValidationParams](arkts-devicecertificate-cert-certvalidationparams-i.md) |
| [CertValidationResult](arkts-devicecertificate-cert-certvalidationresult-i.md) |
| [CmsEnvelopedDecryptionConfig](arkts-devicecertificate-cert-cmsenvelopeddecryptionconfig-i.md) |
| [CmsGenerator](arkts-devicecertificate-cert-cmsgenerator-i.md) |
| [CmsGeneratorOptions](arkts-devicecertificate-cert-cmsgeneratoroptions-i.md) |
| [CmsKeyAgreeRecipientInfo](arkts-devicecertificate-cert-cmskeyagreerecipientinfo-i.md) |
| [CmsKeyTransRecipientInfo](arkts-devicecertificate-cert-cmskeytransrecipientinfo-i.md) |
| [CmsParser](arkts-devicecertificate-cert-cmsparser-i.md) |
| [CmsRecipientInfo](arkts-devicecertificate-cert-cmsrecipientinfo-i.md) |
| [CmsSignerConfig](arkts-devicecertificate-cert-cmssignerconfig-i.md) |
| [CmsVerificationConfig](arkts-devicecertificate-cert-cmsverificationconfig-i.md) |
| [CsrAttribute](arkts-devicecertificate-cert-csrattribute-i.md) |
| [CsrGenerationConfig](arkts-devicecertificate-cert-csrgenerationconfig-i.md) |
| [DataArray](arkts-devicecertificate-cert-dataarray-i.md) |
| [DataBlob](arkts-devicecertificate-cert-datablob-i.md) |
| [EncodingBlob](arkts-devicecertificate-cert-encodingblob-i.md) |
| [GeneralName](arkts-devicecertificate-cert-generalname-i.md) |
| [PbesParams](arkts-devicecertificate-cert-pbesparams-i.md) |
| [Pkcs12CreationConfig](arkts-devicecertificate-cert-pkcs12creationconfig-i.md) |
| [Pkcs12Data](arkts-devicecertificate-cert-pkcs12data-i.md) |
| [Pkcs12ParsingConfig](arkts-devicecertificate-cert-pkcs12parsingconfig-i.md) |
| [PrivateKeyInfo](arkts-devicecertificate-cert-privatekeyinfo-i.md) |
| [RevocationCheckParameter](arkts-devicecertificate-cert-revocationcheckparameter-i.md) |
| [X500DistinguishedName](arkts-devicecertificate-cert-x500distinguishedname-i.md) |
| [X509Cert](arkts-devicecertificate-cert-x509cert-i.md) |
| [X509CertChain](arkts-devicecertificate-cert-x509certchain-i.md) |
| [X509CertMatchParameters](arkts-devicecertificate-cert-x509certmatchparameters-i.md) |
| [X509CertRevokedParams](arkts-devicecertificate-cert-x509certrevokedparams-i.md) |
| [X509Crl](arkts-devicecertificate-cert-x509crl-i.md) |
| [X509CRL](arkts-devicecertificate-cert-x509crl-i.md) |
| [X509CrlEntry](arkts-devicecertificate-cert-x509crlentry-i.md) |
| [X509CRLEntry](arkts-devicecertificate-cert-x509crlentry-i.md) |
| [X509CRLMatchParameters](arkts-devicecertificate-cert-x509crlmatchparameters-i.md) |
| [X509TrustAnchor](arkts-devicecertificate-cert-x509trustanchor-i.md) |

### 枚举

| 名称 |
| --- |
| [CertItemType](arkts-devicecertificate-cert-certitemtype-e.md) |
| [CertResult](arkts-devicecertificate-cert-certresult-e.md) |
| [CertRevocationFlag](arkts-devicecertificate-cert-certrevocationflag-e.md) |
| [CmsCertType](arkts-devicecertificate-cert-cmscerttype-e.md) |
| [CmsContentDataFormat](arkts-devicecertificate-cert-cmscontentdataformat-e.md) |
| [CmsContentType](arkts-devicecertificate-cert-cmscontenttype-e.md) |
| [CmsFormat](arkts-devicecertificate-cert-cmsformat-e.md) |
| [CmsKeyAgreeRecipientDigestAlgorithm](arkts-devicecertificate-cert-cmskeyagreerecipientdigestalgorithm-e.md) |
| [CmsRecipientEncryptionAlgorithm](arkts-devicecertificate-cert-cmsrecipientencryptionalgorithm-e.md) |
| [CmsRsaSignaturePadding](arkts-devicecertificate-cert-cmsrsasignaturepadding-e.md) |
| [EncodingBaseFormat](arkts-devicecertificate-cert-encodingbaseformat-e.md) |
| [EncodingFormat](arkts-devicecertificate-cert-encodingformat-e.md) |
| [EncodingType](arkts-devicecertificate-cert-encodingtype-e.md) |
| [ExtensionEntryType](arkts-devicecertificate-cert-extensionentrytype-e.md) |
| [ExtensionOidType](arkts-devicecertificate-cert-extensionoidtype-e.md) |
| [GeneralNameType](arkts-devicecertificate-cert-generalnametype-e.md) |
| [KeyUsageType](arkts-devicecertificate-cert-keyusagetype-e.md) |
| [OcspDigest](arkts-devicecertificate-cert-ocspdigest-e.md) |
| [PbesEncryptionAlgorithm](arkts-devicecertificate-cert-pbesencryptionalgorithm-e.md) |
| [Pkcs12MacDigestAlgorithm](arkts-devicecertificate-cert-pkcs12macdigestalgorithm-e.md) |
| [RevocationCheckOptions](arkts-devicecertificate-cert-revocationcheckoptions-e.md) |
| [ValidationPolicyType](arkts-devicecertificate-cert-validationpolicytype-e.md) |
