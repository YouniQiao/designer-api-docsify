# offGestureNavigationEnabledChange（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## offGestureNavigationEnabledChange

```TypeScript
function offGestureNavigationEnabledChange(callback?: Callback<boolean>): void
```

移除手势导航启用状态变化的监听。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-window-function offGestureNavigationEnabledChange(callback?: Callback<boolean>): void--><!--Device-window-function offGestureNavigationEnabledChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | 否 | 已注册的回调函数。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有手势导航启用状态变化的监听。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1300003 | This window manager service works abnormally. |
| 1300002 | This window state is abnormal. |
| 202 | Permission verification failed. A non-system application calls a system API. |

