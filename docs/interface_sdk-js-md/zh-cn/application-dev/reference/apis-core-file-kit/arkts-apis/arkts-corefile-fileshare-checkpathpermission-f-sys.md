# checkPathPermission（系统接口）

## 导入模块

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## checkPathPermission

```TypeScript
function checkPathPermission(tokenID: number, policies: Array<PathPolicyInfo>, policyType: PolicyType): Promise<Array<boolean>>
```

异步方法校验所选择的多个文件或目录是否有临时或持久化授权，使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.CHECK_SANDBOX_POLICY

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| policies | Array&lt;[PathPolicyInfo](arkts-corefile-fileshare-pathpolicyinfo-i.md)&gt; | 是 |
| [policyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-otaupdatepolicy-i.md) | [PolicyType](../../apis-mdm-kit/arkts-apis/arkts-mdm-systemmanager-policytype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;boolean & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900042 |
