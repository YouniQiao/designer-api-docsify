# isFoldable

## 导入模块

```TypeScript
```

## isFoldable

```TypeScript
function isFoldable(): boolean
```

判断设备是否可折叠。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function isFoldable(): boolean--><!--Device-display-function isFoldable(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

**示例**

```TypeScript
let ret: boolean = false;
ret = display.isFoldable();
```
