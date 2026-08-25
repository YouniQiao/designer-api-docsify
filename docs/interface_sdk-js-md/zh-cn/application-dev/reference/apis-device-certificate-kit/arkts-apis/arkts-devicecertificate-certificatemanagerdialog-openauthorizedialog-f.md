# openAuthorizeDialog

## 导入模块

```TypeScript
import { certificateManagerDialog } from 'kits/@kit.DeviceCertificateKit';
```

## openAuthorizeDialog

```TypeScript
function openAuthorizeDialog(context: common.Context): Promise<string>
```

打开证书管理对话框的证书凭据授权页面。在弹出的页面中，用户可以为应用授权使用证书凭据。调用成功后，应用可通过接口返回的授权证书凭据uri进行签名、验签和查询详情操作。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29700001](../errorcode-certManagerDialog.md#29700001-内部错误) |
| [29700002](../errorcode-certManagerDialog.md#29700002-操作取消) |


## openAuthorizeDialog

```TypeScript
function openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>
```

打开证书管理对话框的证书凭据授权页面。在弹出的页面中，用户可以为应用授权使用证书凭据。调用成功后，应用可通过接口返回的授权证书凭据uri进行签名、验签和查询详情操作。可授权的证书类型包括应用证书凭据、用户证书凭据和USB Key证书凭据。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.CertificateManagerDialog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.Context | 是 |
| authorizeRequest | [AuthorizeRequest](arkts-devicecertificate-certificatemanagerdialog-authorizerequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CertReference](arkts-devicecertificate-certificatemanagerdialog-certreference-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29700001](../errorcode-certManagerDialog.md#29700001-内部错误) |
| [29700002](../errorcode-certManagerDialog.md#29700002-操作取消) |
| [29700006](../errorcode-certManagerDialog.md#29700006-入参校验失败) |
| [29700007](../errorcode-certManagerDialog.md#29700007-无可用授权证书) |
