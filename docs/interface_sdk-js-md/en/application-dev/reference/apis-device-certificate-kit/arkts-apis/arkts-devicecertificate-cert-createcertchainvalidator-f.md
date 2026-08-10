# createCertChainValidator

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## createCertChainValidator

```TypeScript
function createCertChainValidator(algorithm: string): CertChainValidator
```

表示创建证书链校验器对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cert-function createCertChainValidator(algorithm: string): CertChainValidator--><!--Device-cert-function createCertChainValidator(algorithm: string): CertChainValidator-End-->

**System capability:** SystemCapability.Security.Cert

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algorithm | string | Yes | 表示证书链校验器算法。当前仅支持输入"PKIX"。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CertChainValidator](arkts-devicecertificate-cert-certchainvalidator-i.md) | 表示证书链校验器对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19020002 | 运行时外部错误。可能的原因： &lt;br&gt;1. 内存拷贝失败； &lt;br&gt;2. 系统内部出现空指针； &lt;br&gt;3. 获取Native对象失败或参数转换失败。 |
| 401 | 参数错误。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数校验失败。 |
| 801 | 不支持该操作。 |
| 19020001 | 内存错误。 |
| 19030001 | 调用三方算法库API出错。 |

## Examples

```TypeScript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validator = cert.createCertChainValidator('PKIX');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`createCertChainValidator failed, errCode: ${e.code}, errMsg: ${e.message}`);
}
```

