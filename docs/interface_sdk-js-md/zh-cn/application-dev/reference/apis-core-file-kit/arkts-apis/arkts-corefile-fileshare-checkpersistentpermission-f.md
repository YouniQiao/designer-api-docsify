# checkPersistentPermission

## 导入模块

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## checkPersistentPermission

```TypeScript
function checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>
```

校验所选择的多个文件或目录URI是否已持久化授权，使用Promise异步回调。

**起始版本：** 17

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;boolean & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900042 |
