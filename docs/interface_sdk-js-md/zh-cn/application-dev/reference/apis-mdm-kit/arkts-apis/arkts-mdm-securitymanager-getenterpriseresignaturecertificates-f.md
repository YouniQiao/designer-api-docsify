# getEnterpriseReSignatureCertificates

## 导入模块

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getEnterpriseReSignatureCertificates

```TypeScript
function getEnterpriseReSignatureCertificates(accountId: number): Array<ReSignatureCertificateInfo>
```

根据账号ID获取企业重签名证书信息。该接口返回信息同步，企业可通过该接口查询企业重签名证书详情的管理和有效性监控。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-securityManager-function getEnterpriseReSignatureCertificates(accountId: number): Array<ReSignatureCertificateInfo>--><!--Device-securityManager-function getEnterpriseReSignatureCertificates(accountId: number): Array<ReSignatureCertificateInfo>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountId | number | 是 | 用户ID，必须大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[ReSignatureCertificateInfo](arkts-mdm-securitymanager-resignaturecertificateinfo-i.md)&gt; | 获取的企业重签名证书信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |
| [9200006](../errorcode-enterpriseDeviceManager.md#9200006-指定的用户id非法) | The specified account ID is invalid. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) | Service timeout. |
