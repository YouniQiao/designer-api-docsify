# getPersistentPolicy（系统接口）

## 导入模块

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## getPersistentPolicy

```TypeScript
function getPersistentPolicy(tokenID: number): Promise<Array<PolicyInfo>>
```

获取应用程序的持久化授权策略，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.GET_FILE_ACCESS_PERSIST

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| 13900011 |
| 13900020 |
