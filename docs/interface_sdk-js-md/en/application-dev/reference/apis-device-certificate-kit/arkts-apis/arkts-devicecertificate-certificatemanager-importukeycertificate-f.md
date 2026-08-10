# importUkeyCertificate

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## importUkeyCertificate

```TypeScript
function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>
```

导入证书到USB Key

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_CERT_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-certificateManager-function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>--><!--Device-certificateManager-function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>-End-->

**System capability:** SystemCapability.Security.CertificateManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyUri | string | Yes | 表示USB Key证书凭据的uri. &lt;br&gt;最大长度为256且不能为空。 &lt;br&gt;keyUri参数用于标识证书实体，可以通过调用[getUkeyCertificateList](arkts-devicecertificate-certificatemanager-getukeycertificatelist-f.md#getukeycertificatelist)接口得到。 |
| cert | Uint8Array | Yes | 表示待导入的证书数据。 &lt;br&gt;最大长度为10240且不能为空。 &lt;br&gt;证书数据格式遵循SKF（Smart Key Framework）规范的定义。 |
| ukeyInfo | [UkeyInfo](arkts-devicecertificate-certificatemanager-ukeyinfo-i.md) | Yes | 表示USB Key证书属性信息。 &lt;br&gt;UkeyInfo.CertificatePurpose只能取值为PURPOSE_SIGN、PURPOSE_ENCRYPT或PURPOSE_DEFAULT。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17500011 | Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid. |
| 801 | Capability not supported. |
| 17500010 | Indicates that access USB Key service failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 17500002 | The certificate identified by keyUri does not exist |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; &lt;br&gt;2. Memory operation error; 3. File operation error. Please try again. |

## Examples

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* keyUri and cert must be assigned based on the service. The data in this example is for reference only. */
let keyUri: string = 'test'; /* URI of the USB key certificate, which can be obtained using the getUkeyCertificateList API. */
let certData: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let ukeyInfo: certificateManager.UkeyInfo = {
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_SIGN,
};
try {
  certificateManager.importUkeyCertificate(keyUri, certData, ukeyInfo).then(() => {
    console.info('Succeeded in importing USB key certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to import USB key certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to import USB key certificate. Code: ${error.code}, message: ${error.message}`);
}
```

