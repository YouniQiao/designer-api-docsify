# setVirtualScreenSurface

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## setVirtualScreenSurface

```TypeScript
function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>
```

设置虚拟屏幕的surfaceId。使用Promise异步回调。

**起始版本：** 16

**需要权限：** ohos.permission.ACCESS_VIRTUAL_SCREEN

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| screenId | number | 是 |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
