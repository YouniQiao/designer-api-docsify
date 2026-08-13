# @ohos.router

The **Router** module provides APIs to access pages through URLs. You can use the APIs to navigate to a specified page in an application, replace the current page with another one in the same application, and return to the previous page or a specified page. For routing management, it is recommended that you use the [Navigation](../../../ui/arkts-navigation-architecture.md) component instead as your application routing framework. > **NOTE：**> > - Page routing APIs can be invoked only after page rendering is complete. Do not call these APIs in **onInit** and > **onReady** when the page is still in the rendering phase. > > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used > where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext). > > - When using > [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushUrl) > or > [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushNamedRoute) > with a callback to return the result, be aware that the stack information obtained through the callback using APIs > such as [getLength](arkts-arkui-arkui-uicontext-router-c.md#getLength) represents an intermediate state during the > navigation operation. This temporary state might differ from the final stack information available after the stack > operation is complete.

**Since:** 8

**Deprecated since:** -1

<!--Device-unnamed-declare namespace router--><!--Device-unnamed-declare namespace router-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [back](arkts-arkui-router-back-f.md#back) |
| [back](arkts-arkui-router-back-f.md#back) |
| [clear](arkts-arkui-router-clear-f.md#clear) |
| [disableAlertBeforeBackPage](arkts-arkui-router-disablealertbeforebackpage-f.md#disableAlertBeforeBackPage) |
| [enableAlertBeforeBackPage](arkts-arkui-router-enablealertbeforebackpage-f.md#enableAlertBeforeBackPage) |
| [getLength](arkts-arkui-router-getlength-f.md#getLength) |
| [getParams](arkts-arkui-router-getparams-f.md#getParams) |
| [getState](arkts-arkui-router-getstate-f.md#getState) |
| [getStateByIndex](arkts-arkui-router-getstatebyindex-f.md#getStateByIndex) |
| [getStateByUrl](arkts-arkui-router-getstatebyurl-f.md#getStateByUrl) |
| [hideAlertBeforeBackPage](arkts-arkui-router-hidealertbeforebackpage-f.md#hideAlertBeforeBackPage) |
| [push](arkts-arkui-router-push-f.md#push) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md#pushNamedRoute) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md#pushNamedRoute) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md#pushNamedRoute) |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md#pushNamedRoute) |
| [pushUrl](arkts-arkui-router-pushurl-f.md#pushUrl) |
| [pushUrl](arkts-arkui-router-pushurl-f.md#pushUrl) |
| [pushUrl](arkts-arkui-router-pushurl-f.md#pushUrl) |
| [pushUrl](arkts-arkui-router-pushurl-f.md#pushUrl) |
| [replace](arkts-arkui-router-replace-f.md#replace) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md#replaceNamedRoute) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md#replaceNamedRoute) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md#replaceNamedRoute) |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md#replaceNamedRoute) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md#replaceUrl) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md#replaceUrl) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md#replaceUrl) |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md#replaceUrl) |
| [showAlertBeforeBackPage](arkts-arkui-router-showalertbeforebackpage-f.md#showAlertBeforeBackPage) |

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
