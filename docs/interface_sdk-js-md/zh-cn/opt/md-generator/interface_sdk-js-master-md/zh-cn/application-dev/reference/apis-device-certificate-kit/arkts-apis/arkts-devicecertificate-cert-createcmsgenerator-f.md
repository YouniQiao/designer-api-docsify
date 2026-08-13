# createCmsGenerator

## createCmsGenerator

```TypeScript
function createCmsGenerator(contentType: CmsContentType): CmsGenerator
```

表示创建CmsGenerator对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-cert-function createCmsGenerator(contentType: CmsContentType): CmsGenerator--><!--Device-cert-function createCmsGenerator(contentType: CmsContentType): CmsGenerator-End-->

**系统能力：** SystemCapability.Security.Cert

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| contentType | [CmsContentType](arkts-devicecertificate-cert-cmscontenttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CmsGenerator](arkts-devicecertificate-cert-cmsgenerator-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [19020002](../errorcode-cert.md#19020002-运行时错误) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19020001](../errorcode-cert.md#19020001-内存错误) |
| [19030001](../errorcode-cert.md#19030001-调用三方算法库api出错) |

## 示例

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

// string转Uint8Array
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function testcreateCmsGenerator() {
  let certEncodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  cert.createX509Cert(certEncodingBlob, (error, x509Cert) => {
    if (error) {
      console.error(`createX509Cert failed, errCode: ${error.code}, errMsg: ${error.message}`);
    } else {
        try {
          let cmsContentType = cert.CmsContentType.SIGNED_DATA;
          let cmsGenerator = cert.createCmsGenerator(cmsContentType);
          console.info('testcreateCmsGenerator createCmsGenerator result: success.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          console.error(`createCmsGenerator failed, errCode: ${e.code}, errMsg: ${e.message}`);
        }
    }
  });
}
```
