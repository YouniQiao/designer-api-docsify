# getListenerCount

## 导入模块

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## getListenerCount

```TypeScript
function getListenerCount(eventId: long | string): long
```

获取指定事件的订阅数。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | ArkTS-Dyn: number \| string<br>ArkTS-Sta：long \ | string | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：long |

**示例**

ArkTS-Dyn示例：

```TypeScript
let count: number = emitter.getListenerCount("eventId");
```

ArkTS-Sta示例：

```TypeScript
let count: long = emitter.getListenerCount("eventId");
```

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
let count = emitter1.getListenerCount("eventId");
```
