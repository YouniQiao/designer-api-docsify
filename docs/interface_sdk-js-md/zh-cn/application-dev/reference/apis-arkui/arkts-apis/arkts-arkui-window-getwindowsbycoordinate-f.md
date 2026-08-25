# getWindowsByCoordinate

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getWindowsByCoordinate

```TypeScript
function getWindowsByCoordinate(displayId: number, windowNumber?: number, x?: number, y?: number):
      Promise<Array<Window>>
```

查询本应用指定坐标下的可见窗口数组，按当前窗口层级排列，层级最高的窗口对应数组下标为0，使用Promise异步回调。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |
| windowNumber | number | 否 |
| x | number | 否 |
| y | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Window](arkts-arkui-window-window-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
