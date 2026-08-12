# convertGlobalToRelativeCoordinate

## convertGlobalToRelativeCoordinate

```TypeScript
function convertGlobalToRelativeCoordinate(position: Position, displayId?: number): RelativePosition
```

将主屏左上角为原点的全局坐标转换成displayId指定屏幕左上角为原点的相对坐标。若未传入displayId，默认转换为全局坐标所在屏幕的相对坐标系。若全局坐标不在任何屏幕上，默认转换成主屏的相对坐标。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-display-function convertGlobalToRelativeCoordinate(position: Position, displayId?: long): RelativePosition--><!--Device-display-function convertGlobalToRelativeCoordinate(position: Position, displayId?: long): RelativePosition-End-->

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
| [1400004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400004-参数异常) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
// 定义需要转换的全局坐标
let position: display.Position = {
    x: 100,
    y: 200
};

try {
  // 将全局坐标转换为相对坐标
  let relPos: display.RelativePosition = display.convertGlobalToRelativeCoordinate(position, 0);
  console.info(`The relative coordinate is ${relPos.displayId}, ${relPos.position.x}, ${relPos.position.y}`);
} catch (exception) {
  console.error(`Failed to convert the global coordinate to the relative coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```
