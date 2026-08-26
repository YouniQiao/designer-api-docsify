# @ohos.atomicservice.AtomicServiceWeb(Defines the atomicService web component)

###### Required Permissions
 **ohos.permission.INTERNET**, required for accessing online web pages. For details about how to apply for a
 permission, see [Declaring Permissions](../../../security/AccessToken/declare-permissions.md).
 ###### Child Components
 Not supported
 ###### Attributes
 The universal attributes are not supported.
 ###### Events
 The universal events are not supported.


## Modules to Import

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnErrorReceiveEvent, OnHttpErrorReceiveEvent, OnPageBeginEvent, OnPageEndEvent, AtomicServiceWebController, OnLoadInterceptEvent, OnProgressChangeEvent, OnLoadInterceptCallback, WebHeader } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AtomicServiceWebController(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-atomicservicewebcontroller-c.md) | Implements an **AtomicServiceWebController** object for controlling the behavior of the **AtomicServiceWeb** component. An **AtomicServiceWebController** can control only one **AtomicServiceWeb** component, and the APIs on the **AtomicServiceWebController** can be called only after it has been bound to the target **AtomicServiceWeb** component. |

### Structs

| Name | Description |
| --- | --- |
| [AtomicServiceWeb(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-atomicserviceweb-s.md) | **AtomicServiceWeb** is an advanced web component offering customization to meet specific demands. It shields irrelevant APIs from the native **Web** component and extends functionality through JavaScript capabilities. |

### Interfaces

| Name | Description |
| --- | --- |
| [OnErrorReceiveEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onerrorreceiveevent-i.md) | Represents the callback invoked when an error occurs during web page loading. |
| [OnHttpErrorReceiveEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onhttperrorreceiveevent-i.md) | Represents the callback invoked when an HTTP error occurs during web page resource loading. |
| [OnLoadInterceptEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onloadinterceptevent-i.md) | Represents the event triggered when resource loading is intercepted. |
| [OnMessageEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onmessageevent-i.md) | Represents the callback invoked when the page is navigated back or destroyed. |
| [OnPageBeginEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onpagebeginevent-i.md) | Represents the callback invoked when the web page loading begins. |
| [OnPageEndEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onpageendevent-i.md) | Represents the callback invoked when the web page loading ends. |
| [OnProgressChangeEvent(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-onprogresschangeevent-i.md) | Represents the callback invoked when the web page loading progress changes. |
| [WebHeader(Defines the atomicService web component)](arkts-arkui-atomicservice-atomicserviceweb-webheader-i.md) | Describes the request/response header returned by the **AtomicServiceWeb** component. |

### Types

| Name | Description |
| --- | --- |
| [OnLoadInterceptCallback(Defines the atomicService web component)](arkts-arkui-onloadinterceptcallback-t.md) | Represents the callback invoked when resource loading is intercepted. |
