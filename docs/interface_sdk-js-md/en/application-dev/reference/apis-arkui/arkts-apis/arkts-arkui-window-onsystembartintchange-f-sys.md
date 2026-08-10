# onSystemBarTintChange (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## onSystemBarTintChange

```TypeScript
function onSystemBarTintChange(callback: Callback<SystemBarTintState>): void
```

开启状态栏、导航栏属性变化的监听。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-window-function onSystemBarTintChange(callback: Callback<SystemBarTintState>): void--><!--Device-window-function onSystemBarTintChange(callback: Callback<SystemBarTintState>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;SystemBarTintState&gt; | Yes | 回调函数。返回当前的状态栏、导航栏信息集合。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

