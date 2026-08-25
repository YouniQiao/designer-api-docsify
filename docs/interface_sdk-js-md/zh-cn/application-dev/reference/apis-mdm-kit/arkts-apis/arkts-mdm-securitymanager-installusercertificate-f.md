# installUserCertificate

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## installUserCertificate

```TypeScript
function installUserCertificate(admin: Want, certificate: CertBlob): Promise<string>
```

安装用户证书，使用Promise异步回调。企业可通过此接口将证书安装到设备上，用于企业VPN连接、安全认证、数字签名等场景，实现企业级的安全通信和数据保护。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| certificate | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201001](../errorcode-enterpriseDeviceManager.md#9201001-管理证书失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## installUserCertificate

```TypeScript
function installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string
```

支持按系统账户安装用户证书。企业可为不同用户账户安装独立的证书，实现多用户环境下的安全隔离和个性化证书管理，满足多用户设备的安全管控需求。

**起始版本：** 18

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| certificate | [CertBlob](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-certblob-i.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201001](../errorcode-enterpriseDeviceManager.md#9201001-管理证书失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
