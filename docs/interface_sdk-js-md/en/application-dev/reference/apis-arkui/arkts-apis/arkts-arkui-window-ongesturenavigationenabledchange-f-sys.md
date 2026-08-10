# onGestureNavigationEnabledChange (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## onGestureNavigationEnabledChange

```TypeScript
function onGestureNavigationEnabledChange(callback: Callback<boolean>): void
```

添加手势导航启用状态变化的监听。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-window-function onGestureNavigationEnabledChange(callback: Callback<boolean>): void--><!--Device-window-function onGestureNavigationEnabledChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | 回调函数。返回当前手势导航的启用状态。true表示手势导航状态变化为启用；false表示手势导航状态变化为禁用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300003 | This window manager service works abnormally. |
| 1300002 | This window state is abnormal. |
| 202 | Permission verification failed. A non-system application calls a system API. |

