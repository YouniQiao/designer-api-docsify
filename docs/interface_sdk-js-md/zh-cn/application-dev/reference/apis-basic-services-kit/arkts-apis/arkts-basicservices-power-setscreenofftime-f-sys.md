# setScreenOffTime（系统接口）

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## setScreenOffTime

```TypeScript
function setScreenOffTime(timeout: number): void
```

设置灭屏超时时间。例如，在自助终端或展示设备场景下可设置较长的超时时间以保持屏幕常亮，在低电量场景下可设置较短的超时时间以节省电量。

**起始版本：** 12

**需要权限：** 
- API版本19+：ohos.permission.POWER_MANAGER

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4900101](../errorcode-power.md#4900101-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
