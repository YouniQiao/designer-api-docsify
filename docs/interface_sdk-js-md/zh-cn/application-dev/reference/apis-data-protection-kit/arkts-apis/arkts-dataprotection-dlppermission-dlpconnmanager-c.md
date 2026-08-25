# DlpConnManager

用于调用registerPlugin和unregisterPlugin接口，在SA（System Ability）中注册或注销回调能力。

> **说明：**&gt;
> registerPlugin接口将回调能力注册进SA（System Ability），而unregisterPlugin接口将回调能力从SA（System Ability）中注销。

**起始版本：** 21

**系统能力：** SystemCapability.Security.DataLossPrevention

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## constructor

```TypeScript
constructor()
```

[DlpConnManager](#dlpconnmanager) 实例化时的构造函数。

**起始版本：** 21

**需要权限：** 
- API版本26.0.0+：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API版本21 - 24：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## registerPlugin

```TypeScript
static registerPlugin(plugin: DlpConnPlugin): number
```

该接口提供将回调注册到SA（System Ability）侧的功能。

> **说明：**&gt;
> registerPlugin将plugin注册到SA（System Ability）侧，待SA（System Ability）调用。

**起始版本：** 21

**需要权限：** 
- API版本26.0.0+：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API版本21 - 24：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plugin | [DlpConnPlugin](arkts-dataprotection-dlppermission-dlpconnplugin-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |

## unregisterPlugin

```TypeScript
static unregisterPlugin(): void
```

提供将回调从SA（System Ability）侧注销的能力。该接口可用于应用退出时注销回调释放资源，确保回调能力正确释放。

> **说明：**&gt;
> unregisterPlugin将plugin从SA（System Ability）侧注销。

**起始版本：** 21

**需要权限：** 
- API版本26.0.0+：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API版本21 - 24：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |
