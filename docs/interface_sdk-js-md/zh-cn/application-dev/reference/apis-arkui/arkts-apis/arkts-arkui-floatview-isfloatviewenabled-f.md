# isFloatViewEnabled

## 导入模块

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## isFloatViewEnabled

```TypeScript
function isFloatViewEnabled(): boolean
```

判断当前设备是否支持标准悬浮窗功能。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let enable: boolean = floatView.isFloatViewEnabled();
console.info('Float view enabled is: ' + enable);
```
