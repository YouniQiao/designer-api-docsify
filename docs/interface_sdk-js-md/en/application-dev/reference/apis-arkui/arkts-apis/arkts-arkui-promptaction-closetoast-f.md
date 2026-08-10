# closeToast

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## closeToast

```TypeScript
export function closeToast(toastId: int): void
```

关闭即时反馈。

> **说明：**
> 
> 直接使用closeToast可能导致[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题，建议使用UIContext中的getPromptAction
> 方法获取到PromptAction对象，再通过该对象调用
> [closeToast](../../../reference/apis-arkui/arkts-apis-uicontext-promptaction.md#closetoast18)实现。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-promptAction-export function closeToast(toastId: int): void--><!--Device-promptAction-export function closeToast(toastId: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toastId | int | Yes | openToast返回的id。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 103401 | Cannot find the toast. |

