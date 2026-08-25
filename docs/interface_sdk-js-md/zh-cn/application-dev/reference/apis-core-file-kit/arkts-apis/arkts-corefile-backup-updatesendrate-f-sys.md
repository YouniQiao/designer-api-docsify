# updateSendRate（系统接口）

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## updateSendRate

```TypeScript
function updateSendRate(bundleName: string, sendRate: number): boolean
```

更新备份应用发送文件描述符的速率。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| sendRate | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
