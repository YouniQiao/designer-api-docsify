# offRotateChange（系统接口）

## 导入模块

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## offRotateChange

```TypeScript
function offRotateChange(callback?: Callback<RotateEvent>): void
```

Unsubscribe to rotate sensor event.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-motion-function offRotateChange(callback?: Callback<RotateEvent>): void--><!--Device-motion-function offRotateChange(callback?: Callback<RotateEvent>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;RotateEvent&gt; | 否 | Callback used for rotate event unsubscription. &lt;br&gt; If this parameter is not specified, all callbacks of the rotate event are unsubscribed from. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, &lt;br&gt; container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 202 | Permission verification failed. A non-system application calls a system API. |

