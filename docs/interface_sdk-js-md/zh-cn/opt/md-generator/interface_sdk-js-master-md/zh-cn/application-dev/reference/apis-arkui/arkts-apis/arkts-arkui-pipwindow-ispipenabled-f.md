# isPiPEnabled

## 导入模块

```TypeScript
```

## isPiPEnabled

```TypeScript
function isPiPEnabled(): boolean
```

判断当前设备是否支持画中画功能。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PiPWindow-function isPiPEnabled(): boolean--><!--Device-PiPWindow-function isPiPEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let enable: boolean = PiPWindow.isPiPEnabled(); // 获取当前系统是否支持画中画功能
console.info('isPiPEnabled:' + enable);
```
