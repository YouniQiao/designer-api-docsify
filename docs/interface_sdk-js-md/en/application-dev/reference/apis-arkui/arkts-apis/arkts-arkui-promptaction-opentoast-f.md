# openToast

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## openToast

```TypeScript
export function openToast(options: ShowToastOptions): Promise<int>
```

显示即时反馈并通过Promise返回其id。

> **说明：**
> 
> - 不支持在输入法类型窗口中使用子窗（showMode设置为TOP_MOST或者SYSTEM_TOP_MOST）的openToast，详情见输入法框架的约束与限制说明
> [createPanel](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-inputmethodability-i.md/arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel)
> 。
> 
> - 直接使用openToast可能导致[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题，建议使用UIContext中的
> getPromptAction方法获取到PromptAction对象，再通过该对象调用
> [openToast](../../../reference/apis-arkui/arkts-apis-uicontext-promptaction.md#opentoast18)实现。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-promptAction-export function openToast(options: ShowToastOptions): Promise<int>--><!--Device-promptAction-export function openToast(options: ShowToastOptions): Promise<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | Yes | Toast选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | 返回即时反馈的id，可供closeToast使用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

