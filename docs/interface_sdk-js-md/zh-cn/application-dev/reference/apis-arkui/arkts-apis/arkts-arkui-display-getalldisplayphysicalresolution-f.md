# getAllDisplayPhysicalResolution

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplayPhysicalResolution

```TypeScript
function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>
```

获取当前设备支持的所有显示模式及其对应的物理屏幕分辨率信息对象。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DisplayPhysicalResolution](arkts-arkui-display-displayphysicalresolution-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
