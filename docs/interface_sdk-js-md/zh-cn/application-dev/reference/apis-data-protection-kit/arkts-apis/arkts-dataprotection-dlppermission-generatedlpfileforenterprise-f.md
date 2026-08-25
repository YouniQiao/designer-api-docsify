# generateDlpFileForEnterprise

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## generateDlpFileForEnterprise

```TypeScript
function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>
```

将明文文件加密生成企业账号DLP文件，仅支持企业账号调用。使用Promise异步回调。用于将明文文件加密生成企业账号的DLP权限受控文件，实现企业级的文件权限管理。

> **说明：**&gt;
> 该接口仅支持企业账号调用，需要企业自行搭建企业账号服务器配套使用。使用该接口可以将明文文件加密生成权限受控文件，由企业服务器管控账号是否有权限解密该文件。

**起始版本：** 21

**需要权限：** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| plaintextFd | number | 是 |
| dlpFd | number | 是 |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | 是 |
| [customProperty](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | [CustomProperty](arkts-dataprotection-dlppermission-customproperty-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100002](../errorcode-dlp.md#19100002-加解密出错) |
| [19100003](../errorcode-dlp.md#19100003-加解密超时) |
| [19100004](../errorcode-dlp.md#19100004-凭据服务错误) |
| [19100005](../errorcode-dlp.md#19100005-凭据认证服务器错误) |
| [19100009](../errorcode-dlp.md#19100009-操作dlp文件失败) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100014](../errorcode-dlp.md#19100014-账号未登录) |
