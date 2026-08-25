# updateTimer（系统接口）

## 导入模块

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## updateTimer

```TypeScript
function updateTimer(bundleName: string, timeout: number): boolean
```

设置应用备份或恢复的时长。

**起始版本：** 12

**需要权限：** ohos.permission.BACKUP

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| timeout | number | 是 |

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
