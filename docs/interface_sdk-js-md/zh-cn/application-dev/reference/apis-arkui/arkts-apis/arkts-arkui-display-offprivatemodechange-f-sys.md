# offPrivateModeChange（系统接口）

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offPrivateModeChange

```TypeScript
function offPrivateModeChange(callback?: Callback<boolean>): void
```

Unregister the callback for private mode changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-display-function offPrivateModeChange(callback?: Callback<boolean>): void--><!--Device-display-function offPrivateModeChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

