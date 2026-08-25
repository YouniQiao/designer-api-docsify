# init

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## init

```TypeScript
function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void
```

使用凭据进行签名、验签的初始化操作，是签名验签流程的第一步，后续需依次调用update和finish接口完成操作。使用Callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authUri | string | 是 |
| spec | [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CMHandle](arkts-devicecertificate-certificatemanager-cmhandle-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500002](../errorcode-certManager.md#17500002-证书不存在) |
| [17500005](../errorcode-certManager.md#17500005-应用未经用户授权) |


## init

```TypeScript
function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>
```

使用凭据进行签名、验签的初始化操作。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authUri | string | 是 |
| spec | [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMHandle](arkts-devicecertificate-certificatemanager-cmhandle-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500002](../errorcode-certManager.md#17500002-证书不存在) |
| [17500005](../errorcode-certManager.md#17500005-应用未经用户授权) |
