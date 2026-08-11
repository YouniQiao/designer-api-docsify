# isFloatingBallEnabled

## isFloatingBallEnabled

```TypeScript
function isFloatingBallEnabled(): boolean
```

判断当前设备是否支持闪控球功能。

**起始版本：** 20

<!--Device-floatingBall-function isFloatingBallEnabled(): boolean--><!--Device-floatingBall-function isFloatingBallEnabled(): boolean-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
// 判断当前设备是否支持闪控球功能
let enable: boolean = floatingBall.isFloatingBallEnabled();
console.info('Floating ball enabled is: ' + enable);
```
