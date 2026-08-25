# revokePermission（系统接口）

## 导入模块

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
```

## revokePermission

```TypeScript
function revokePermission(tokenID: number): Promise<void>
```

撤销指定应用的全部持久化文件授权，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

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
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| 13900020 |


## revokePermission

```TypeScript
function revokePermission(tokenID: number, policies: Array<PolicyInfo>): Promise<void>
```

撤销指定应用对URI的持久化授权，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.REVOKE_FILE_ACCESS_PERSIST

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 13900001 |
| 13900011 |
| 13900020 |
