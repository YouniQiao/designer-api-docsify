# getListenerCount

## 导入模块

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## getListenerCount

```TypeScript
function getListenerCount(eventId: number | string): number
```

获取指定事件的订阅数。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventId | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| number |
