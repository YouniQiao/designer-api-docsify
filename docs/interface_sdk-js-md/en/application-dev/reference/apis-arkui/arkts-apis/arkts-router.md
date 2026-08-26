# @ohos.router

The **Router** module provides APIs to access pages through URLs. You can use the APIs to navigate to a specified page in an application, replace the current page with another one in the same application, and return to the previous page or a specified page.For routing management, it is recommended that you use the [Navigation](../../../ui/arkts-navigation-architecture.md) component instead as your application routing framework.

> **NOTE：**
> 
> - Page routing APIs can be invoked only after page rendering is complete. Do not call these APIs in **onInit** and
> **onReady** when the page is still in the rendering phase.
> 
> - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
> where [the UI context is ambiguous](../../../ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md).
> 
> - When using
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)
> or
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)
> with a callback to return the result, be aware that the stack information obtained through the callback using APIs
> such as [getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength) represents an intermediate state during the
> navigation operation. This temporary state might differ from the final stack information available after the stack
> operation is complete.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import router from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [back](arkts-arkui-router-back-f.md) | Returns to the previous page or a specified page, which deletes all pages between the current page and the target page. |
| [back](arkts-arkui-router-back-f.md) | Returns to the specified page, which deletes all pages between the current page and the target page. |
| [clear](arkts-arkui-router-clear-f.md) | Clears all historical pages in the stack and retains only the current page at the top of the stack. |
| [disableAlertBeforeBackPage](arkts-arkui-router-disablealertbeforebackpage-f.md) | Disables the display of a confirm dialog box before returning to the previous page. |
| [enableAlertBeforeBackPage](arkts-arkui-router-enablealertbeforebackpage-f.md) | Enables the display of a confirm dialog box before returning to the previous page. |
| [getLength](arkts-arkui-router-getlength-f.md) | Obtains the number of pages in the current stack. |
| [getParams](arkts-arkui-router-getparams-f.md) | Obtains the parameters passed from the page that initiates redirection to the current page. |
| [getState](arkts-arkui-router-getstate-f.md) | Obtains state information about the page at the top of the navigation stack. |
| [getStateByIndex](arkts-arkui-router-getstatebyindex-f.md) | Obtains the status information about a page by its index. |
| [getStateByUrl](arkts-arkui-router-getstatebyurl-f.md) | Obtains the status information about a page by its URL. |
| [hideAlertBeforeBackPage](arkts-arkui-router-hidealertbeforebackpage-f.md) | Disables the display of a confirm dialog box before returning to the previous page. |
| [push](arkts-arkui-router-push-f.md) | Navigates to a specified page in the application. |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) | Navigates to a page using the named route. This API uses a promise to return the result. |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) | Navigates to a page using the named route. This API uses a promise to return the result. |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) | Navigates to a page using the named route. This API uses a promise to return the result. |
| [pushNamedRoute](arkts-arkui-router-pushnamedroute-f.md) | Navigates to a page using the named route. This API uses a promise to return the result. |
| [pushUrl](arkts-arkui-router-pushurl-f.md) | Navigates to a specified page in the application. |
| [pushUrl](arkts-arkui-router-pushurl-f.md) | Navigates to a specified page in the application. |
| [pushUrl](arkts-arkui-router-pushurl-f.md) | Navigates to a specified page in the application. |
| [pushUrl](arkts-arkui-router-pushurl-f.md) | Navigates to a specified page in the application. |
| [replace](arkts-arkui-router-replace-f.md) | Replaces the current page with another one in the application and destroys the current page. |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) | Replaces the current page with another one using the named route and destroys the current page. |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) | Replaces the current page with another one using the named route and destroys the current page. |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) | Replaces the current page with another one using the named route and destroys the current page. |
| [replaceNamedRoute](arkts-arkui-router-replacenamedroute-f.md) | Replaces the current page with another one using the named route and destroys the current page. |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) | Replaces the current page with another one in the application and destroys the current page. |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) | Replaces the current page with another one in the application and destroys the current page. This API cannot be used to configure page transition effects. To configure page transition effects, use the [Navigation](../../../ui/arkts-navigation-architecture.md) component. |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) | Replaces the current page with another one in the application and destroys the current page. |
| [replaceUrl](arkts-arkui-router-replaceurl-f.md) | Replaces the current page with another one in the application and destroys the current page. |
| [showAlertBeforeBackPage](arkts-arkui-router-showalertbeforebackpage-f.md) | Enables the display of a confirm dialog box before returning to the previous page. |

### Interfaces

| Name | Description |
| --- | --- |
| [EnableAlertOptions](arkts-arkui-router-enablealertoptions-i.md) | Describes the page routing state. |
| [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Describes the named route options. |
| [RouterOptions](arkts-arkui-router-routeroptions-i.md) | Describes the page routing options. |
| [RouterState](arkts-arkui-router-routerstate-i.md) | Describes the page routing state. |

### Enums

| Name | Description |
| --- | --- |
| [RouterMode](arkts-arkui-router-routermode-e.md) | Enumerates the routing modes. |
