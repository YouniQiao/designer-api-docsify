# activatePermission

## 导入模块

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## activatePermission

```TypeScript
function activatePermission(policies: Array<PolicyInfo>): Promise<void>
```

激活多个已持久化授权的文件或目录，使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.FILE_ACCESS_PERSIST

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| 13900042 |
