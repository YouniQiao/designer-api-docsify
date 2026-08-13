# isCaptured

## isCaptured

```TypeScript
function isCaptured(): boolean
```

检查设备的屏幕显示信息是否被获取。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-display-function isCaptured(): boolean--><!--Device-display-function isCaptured(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
let ret: boolean = false;
// 检查屏幕显示信息是否被获取
ret = display.isCaptured();
```


## isCaptured

```TypeScript
function isCaptured(bundleNameList: Array<string>): boolean
```

检查该设备是否被bundle名称列表中的任何应用抓拍、投影或录制。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-display-function isCaptured(bundleNameList: Array<string>): boolean--><!--Device-display-function isCaptured(bundleNameList: Array<string>): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleNameList | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1400004](../errorcode-display.md#1400004-参数异常) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
try {
  const bundleList: Array<string> = ['com.example.app'];
  let ret = display.isCaptured(bundleList);
  console.info(`The screen is captured or not: ${ret}`);
} catch (err) {
  console.error(`Failed to get display isCaptured. Code: ${err.code}, message: ${err.message}`);
}
```
