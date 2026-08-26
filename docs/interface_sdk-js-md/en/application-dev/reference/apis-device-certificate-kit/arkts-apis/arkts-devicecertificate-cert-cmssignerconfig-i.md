# CmsSignerConfig

Represents the configuration of the CMS signer.

**Since:** 18

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
```

## addAttr

```TypeScript
addAttr?: boolean
```

Whether to add the signature attribute. The default value is **true**. **true**: yes; **false**: no.

**Type:** boolean

**Default:** true

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

## addCert

```TypeScript
addCert?: boolean
```

Whether to add a certificate. The default value is **true**. **true**: yes; **false**: no.

**Type:** boolean

**Default:** true

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

**Examples**

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certData = '-----BEGIN CERTIFICATE-----\n' +
  'MIICXjCCAcegAwIBAgIGAXKnJjrAMA0GCSqGSIb3DQEBCwUAMEgxCzAJBgNVBAYT\n' +
  'AkNOMQwwCgYDVQQIDANzaGExDTALBgNVBAcMBHhpYW4xDTALBgNVBAoMBHRlc3Qx\n' +
  'DTALBgNVBAMMBHRlc3QwHhcNMjQxMTIyMDkwNTIyWhcNMzQxMTIwMDkwNTIyWjBI\n' +
  'MQswCQYDVQQGEwJDTjEMMAoGA1UECAwDc2hhMQ0wCwYDVQQHDAR4aWFuMQ0wCwYD\n' +
  'VQQKDAR0ZXN0MQ0wCwYDVQQDDAR0ZXN0MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n' +
  'iQKBgQC6nCZTM16Rk2c4P/hwfVm++jqe6GCA/PXXGe4YL218q1dTKMHBGEw8kXi0\n' +
  'XLDcyyC2yUn8ywN2QSyly6ke9EE6PGfZywStLp4g2PTTWB04sS3aXT2y+fToiTXQ\n' +
  '3AxfFYRpB+EgSdSCkJs6jKXVwbzu54kEtQTfs8UdBQ9nVKaJLwIDAQABo1MwUTAd\n' +
  'BgNVHQ4EFgQU6QXnt1smb2HRSO/2zuRQnz/SDxowHwYDVR0jBBgwFoAU6QXnt1sm\n' +
  'b2HRSO/2zuRQnz/SDxowDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOB\n' +
  'gQBPR/+5xzFG1XlTdgwWVvqVxvhGUkbMTGW0IviJ+jbKsi57vnVsOtFzEA6y+bYx\n' +
  'xG/kEOcwLtzeVHOQA+ZU5SVcc+qc0dfFiWjL2PSAG4bpqSTjujpuUk+g8ugixbG1\n' +
  'a26pkDJhNeB/E3eBIbeydSY0A/dIGb6vbGo6BSq2KvnWAA==\n' +
  '-----END CERTIFICATE-----\n';

// Convert the string into a Uint8Array.
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function testAddCert() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // Assign a value based on the encodingData format. FORMAT_PEM and FORMAT_DER are supported.
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
        try {
          let cmsContentType = cert.CmsContentType.SIGNED_DATA;
          let cmsGenerator = cert.createCmsGenerator(cmsContentType);
          console.info('testAddCert createCmsGenerator result: success.');
          // If the same certificate is added, an error will be reported.
          cmsGenerator.addCert(x509Cert);
          console.info('testAddCert addCert result: success.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error(`testAddCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
        }
    }
  });
}
```

## addSmimeCapAttr

```TypeScript
addSmimeCapAttr?: boolean
```

Whether to add the SMIME capability to the CMS object. The default value is **true**. **true**: yes; **false**: no.

**Type:** boolean

**Default:** true

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

## mdName

```TypeScript
mdName: string
```

Message digest algorithm, for example, **SHA384**. Currently, **SHA1**, **SHA256**, **SHA384**, and **SHA512** are supported.

**Type:** string

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Security.Cert

## rsaSignaturePadding

```TypeScript
rsaSignaturePadding?: CmsRsaSignaturePadding
```

Padding mode for an RSA signature. The default value is **PKCS1_PADDING**. When **PKCS1_PSS_PADDING** is set, **mdName** must be set to **SHA256**, **SHA384**, or **SHA512**.

> **NOTE：**
> 
> This parameter is valid only when the private key type of the signature is RSA.

**Type:** [CmsRsaSignaturePadding](arkts-devicecertificate-cert-cmsrsasignaturepadding-e.md)

**Default:** CmsRsaSignaturePadding.PKCS1_PADDING

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Security.Cert
