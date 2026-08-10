# offRemove

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offRemove

```TypeScript
function offRemove(callback?: Callback<long>): void
```

Unregister the callback for display remove events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-display-function offRemove(callback?: Callback<long>): void--><!--Device-display-function offRemove(callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

