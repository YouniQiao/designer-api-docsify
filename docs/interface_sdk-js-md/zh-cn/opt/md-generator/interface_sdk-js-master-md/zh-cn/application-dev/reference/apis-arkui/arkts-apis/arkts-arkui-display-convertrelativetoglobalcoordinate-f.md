# convertRelativeToGlobalCoordinate

## convertRelativeToGlobalCoordinate

```TypeScript
function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position
```

将指定屏幕左上角为原点的相对坐标转换成主屏左上角为原点的全局坐标，仅支持主屏和扩展屏的坐标转换。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position--><!--Device-display-function convertRelativeToGlobalCoordinate(relativePosition: RelativePosition): Position-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relativePosition | [RelativePosition](arkts-arkui-display-relativeposition-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Position](arkts-arkui-display-position-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [1400004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400004-参数异常) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
// 定义需要转换的相对坐标
let relativePosition: display.RelativePosition = {
  displayId: 0,
  position: {
    x: 100,
    y: 200
  }
};

try {
   // 将相对坐标转换为全局坐标
  let position: display.Position = display.convertRelativeToGlobalCoordinate(relativePosition);
  console.info(`The global coordinate is ${position.x}, ${position.y}`);
} catch (exception) {
  console.error(`Failed to convert the relative coordinate to the global coordinate. Code: ${exception.code}, message: ${exception.message}`);
}
```
