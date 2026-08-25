# @ohos.router

The **Router** module provides APIs to access pages through URLs. You can use the APIs to navigate to a specified page in an application, replace the current page with another one in the same application, and return to the previous page or a specified page.For routing management, it is recommended that you use the [Navigation](../../../ui/arkts-navigation-architecture.md) component instead as your application routing framework.

> **NOTE：**&gt;
> - Page routing APIs can be invoked only after page rendering is complete. Do not call these APIs in **onInit** and
> **onReady** when the page is still in the rendering phase.&gt;
> - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
> where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md).&gt;
> - When using
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)
> or
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)
> with a callback to return the result, be aware that the stack information obtained through the callback using APIs
> such as [getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength) represents an intermediate state during the
> navigation operation. This temporary state might differ from the final stack information available after the stack
> operation is complete.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [back](arkts-arkui-router-back-f.md) |
| [back](arkts-arkui-router-back-f.md) |
| [clear](arkts-arkui-router-clear-f.md) |
| [disableAlertBeforeBackPage](arkts-arkui-router-disablealertbeforebackpage-f.md) |
| [enableAlertBeforeBackPage](arkts-arkui-router-enablealertbeforebackpage-f.md) |
| [getLength](arkts-arkui-router-getlength-f.md) |
| [getParams](arkts-arkui-router-getparams-f.md) |
| [getState](arkts-arkui-router-getstate-f.md) |
| [getStateByIndex](arkts-arkui-router-getstatebyindex-f.md) |
| [getStateByUrl](arkts-arkui-router-getstatebyurl-f.md) |
| [hideAlertBeforeBackPage](arkts-arkui-router-hidealertbeforebackpage-f.md) |
| [push](arkts-arkui-router-push-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [pushUrl](arkts-arkui-router-pushurl-f.md) |
| [replace](arkts-arkui-router-replace-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) |
| [showAlertBeforeBackPage](arkts-arkui-router-showalertbeforebackpage-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EnableAlertOptions](arkts-arkui-router-enablealertoptions-i.md) |
| [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) |
| [RouterOptions](arkts-arkui-router-routeroptions-i.md) |
| [RouterState](arkts-arkui-router-routerstate-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RouterMode](arkts-arkui-router-routermode-e.md) |
