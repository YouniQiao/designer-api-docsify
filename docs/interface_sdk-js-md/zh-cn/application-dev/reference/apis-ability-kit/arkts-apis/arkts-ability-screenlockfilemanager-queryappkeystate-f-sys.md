# queryAppKeyState（系统接口）

## 导入模块

```TypeScript
import { screenLockFileManager } from 'kits/@kit.AbilityKit';
```

## queryAppKeyState

```TypeScript
function queryAppKeyState(dataType: DataType): KeyStatus
```

以同步方法查询锁屏下指定类型敏感数据密钥的状态。

**起始版本：** 18

**需要权限：** ohos.permission.ACCESS_SCREEN_LOCK_MEDIA_DATA or ohos.permission.ACCESS_SCREEN_LOCK_ALL_DATA

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataType | [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [29300001](../errorcode-screenLockFileManager.md#29300001-入参错误) |
| [29300002](../errorcode-screenLockFileManager.md#29300002-系统服务工作异常) |
