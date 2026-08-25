# convertGlobalToRelativeCoordinate

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## convertGlobalToRelativeCoordinate

```TypeScript
function convertGlobalToRelativeCoordinate(position: Position, displayId?: number): RelativePosition
```

将主屏左上角为原点的全局坐标转换成displayId指定屏幕左上角为原点的相对坐标。若未传入displayId，默认转换为全局坐标所在屏幕的相对坐标系。若全局坐标不在任何屏幕上，默认转换成主屏的相对坐标。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | [Position](arkts-arkui-display-position-i.md) | 是 |
| displayId | number | 否 |

**返回值：**

| 类型 |
| --- |
| [RelativePosition](arkts-arkui-display-relativeposition-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
