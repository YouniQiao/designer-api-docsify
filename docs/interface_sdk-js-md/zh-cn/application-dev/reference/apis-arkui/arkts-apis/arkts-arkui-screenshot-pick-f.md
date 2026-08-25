# pick

## 导入模块

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## pick

```TypeScript
function pick(): Promise<PickInfo>
```

获取屏幕截图，当前仅支持获取displayId为0的屏幕截图（如果需要对扩展屏截图，可以通过[capture](arkts-arkui-screenshot-capture-f.md)接口实现），使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PickInfo](arkts-arkui-screenshot-pickinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
