# getCredentialId

## 导入模块

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getCredentialId

```TypeScript
function getCredentialId(authToken: Uint8Array, allowableDuration: number): Promise<bigint>
```

根据认证Token获取凭证ID。该接口使用promise返回结果。企业可以通过该接口解析和查询用户凭证ID（如人脸、指纹ID等）。企业设备安全审计、身份认证等场景。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-securityManager-function getCredentialId(authToken: Uint8Array, allowableDuration: number): Promise<bigint>--><!--Device-securityManager-function getCredentialId(authToken: Uint8Array, allowableDuration: number): Promise<bigint>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authToken | Uint8Array | 是 | 认证令牌，认证成功后颁发。最大的长度为1024字节。 |
| allowableDuration | number | 是 | 允许解析认证token的时长，单位为毫秒。且小于等于86400000。<br>取值应&gt;0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;bigint&gt; | Promise对象，返回凭证ID。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) | Service timeout. |
| [9201057](../errorcode-enterpriseDeviceManager.md#9201057-认证令牌无效) | Invalid authentication token. |
| [9201058](../errorcode-enterpriseDeviceManager.md#9201058-认证令牌解析时长超出允许范围) | The authentication token parsing duration is out of the allowed range. |
