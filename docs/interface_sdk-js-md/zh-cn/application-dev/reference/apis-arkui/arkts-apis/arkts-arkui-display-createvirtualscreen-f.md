# createVirtualScreen

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## createVirtualScreen

```TypeScript
function createVirtualScreen(config: VirtualScreenConfig): Promise<number>
```

创建虚拟屏幕，使用Promise异步回调。

**起始版本：** 16

**需要权限：** ohos.permission.ACCESS_VIRTUAL_SCREEN

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [VirtualScreenConfig](arkts-arkui-display-virtualscreenconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
