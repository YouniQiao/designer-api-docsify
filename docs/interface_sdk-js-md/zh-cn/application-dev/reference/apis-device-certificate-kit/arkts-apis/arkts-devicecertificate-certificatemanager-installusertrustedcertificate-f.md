# installUserTrustedCertificate

## 导入模块

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## installUserTrustedCertificate

```TypeScript
function installUserTrustedCertificate(certificate: CertBlob) : Promise<CMResult>
```

安装用户CA证书。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| certificate | [CertBlob](arkts-devicecertificate-certificatemanager-certblob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500003](../errorcode-certManager.md#17500003-证书或凭据无效) |
| [17500004](../errorcode-certManager.md#17500004-证书或凭据数量达到上限) |
| [17500007](../errorcode-certManager.md#17500007-设备进入坚盾守护模式) |
