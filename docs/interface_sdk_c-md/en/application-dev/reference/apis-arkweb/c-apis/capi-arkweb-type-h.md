# arkweb_type.h

## Overview

Defines the native common types of ArkWeb.

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Related module**: [Web](capi-web.md)

## Summary

### Struct

| Name | typedef keyword | Description |
| -- | -- | -- |
| [ArkWeb_JavaScriptBridgeData](capi-web-arkweb-javascriptbridgedata.md) | ArkWeb_JavaScriptBridgeData | ArkWeb_JavaScriptBridgeData is a struct that defines JavaScript bridge data, used to transfer JavaScriptbridge-related data between native code and web pages. This struct encapsulates the parameter data in bridge callsand serves as the basic data unit in the JavaScript bridge subsystem, working in conjunction with the JavaScriptProxy registration APIs in ArkWeb_ControllerAPI. |
| [ArkWeb_JavaScriptObject](capi-web-arkweb-javascriptobject.md) | ArkWeb_JavaScriptObject | The **ArkWeb_JavaScriptObject** struct is used to inject JavaScript code into a web page and obtain theexecution result. It is suitable for scenarios where a native app needs to actively call JavaScript functions in aweb page, read the web page state, or call web page APIs, simplifying the data interaction flow between the web andnative app. Developers can use this struct to specify the JavaScript script content and length to be injected,register an execution completion callback, and pass custom context data through userData, thereby enabling datainteraction between the web and native app. |
| [ArkWeb_ProxyMethod](capi-web-arkweb-proxymethod.md) | ArkWeb_ProxyMethod | ArkWeb_ProxyMethod is a struct that defines a JavaScript proxy method. It supports secure communicationbetween JavaScript and native code, and is suitable for scenarios where native capabilities need to be called from aweb page. This struct specifies the basic information of a native method that can be called from JavaScript,consisting of three fields: the method name, the corresponding native callback pointer, and the custom data to carry.Multiple ArkWeb_ProxyMethod instances can be combined into an ArkWeb_ProxyObject, which is injected into a web pageas an object, allowing web apps to conveniently access native device capabilities. |
| [ArkWeb_ProxyMethodWithResult](capi-web-arkweb-proxymethodwithresult.md) | ArkWeb_ProxyMethodWithResult | ArkWeb_ProxyMethodWithResult is a JavaScript proxy method struct with a return value. It extends thecapabilities of ArkWeb_ProxyMethod and supports obtaining a return value after JavaScript calls a native method.Based on the method name and callback function, this struct adds the return value processing capability, making itsuitable for scenarios where execution results need to be returned to the web frontend. |
| [ArkWeb_ProxyObject](capi-web-arkweb-proxyobject.md) | ArkWeb_ProxyObject | ArkWeb_ProxyObject is a JavaScript proxy object struct injected into a web page. It organizes a group ofrelated ArkWeb_ProxyMethod methods into an object and exposes them to the web frontend as a whole. This structspecifies the object name in JavaScript (objName), the method array (methodList), and the method count (size),enabling a Native app to expose a structured API set to the web page. The proxy object associates ArkWeb_ProxyMethodon the native side with method calls on the JavaScript side through a method mapping mechanism, supporting automaticconversion of method parameters and return values. |
| [ArkWeb_ProxyObjectWithResult](capi-web-arkweb-proxyobjectwithresult.md) | ArkWeb_ProxyObjectWithResult | ArkWeb_ProxyObjectWithResult is a JavaScript proxy object struct with a return value, extending thecapabilities of ArkWeb_ProxyObject. This struct organizes multiple ArkWeb_ProxyMethodWithResult instances into anobject and injects it into a web page, allowing JavaScript to obtain a return value after calling Native methods. Itresolves the issue that ArkWeb_ProxyObject cannot return execution results, simplifying the development process andimproving development efficiency. It is suitable for API scenarios that require returning structured executionresults to the web frontend. |
| [ArkWeb_ControllerAPI](capi-web-arkweb-controllerapi.md) | ArkWeb_ControllerAPI | ArkWeb_ControllerAPI is a native API struct related to the controller. This struct provides features such asJavaScript injection, synchronous and asynchronous JavaScript proxy registration, proxy deletion, page refresh, WebMessage Port creation and management, and Frame URL query. It supports the coexistence of synchronous andasynchronous proxies and unified management and control of WebView behavior. It is suitable for scenarios whereJavaScript needs to be injected and called from native code and bidirectional communication between native and pagesis required. It resolves JSBridge intercommunication and secure injection issues, improving development efficiencyand controllability. This is the primary interface for controlling WebView behavior from native code.<br>Controller-related APIs must be called on the UI thread by calling the OH_ArkWeb_GetNativeAPI method. Before calling, you areadvised to use {@link ARKWEB_MEMBER_MISSING} to check the availability of the function pointer to avoid crashescaused by mismatches between the SDK and the device ROM. |
| [ArkWeb_ComponentAPI](capi-web-arkweb-componentapi.md) | ArkWeb_ComponentAPI | ArkWeb_ComponentAPI is an API struct provided by ArkWeb on the native side for listening to Web componentlifecycle events. It inherits from the base native API type {@link ArkWeb_AnyNativeAPI}. Developers obtain thisstruct by calling {@link OH_ArkWeb_GetNativeAPI} with the `ARKWEB_NATIVE_COMPONENT` type, and then register eventcallbacks for Web component Controller attached, page load begin, page load end, and component destruction. Thisstruct is suitable for scenarios where you need to perceive key state changes of the Web component in native code (C/C++), such as initializing native resources, synchronizing page load status, collecting analytics data, or releasingassociated resources upon component destruction. The related APIs must be called in the UI thread. Before calling aspecific member function, it is recommended to use the {@link ARKWEB_MEMBER_MISSING} macro to check whether thefunction pointer exists. |
| [ArkWeb_WebMessagePortAPI](capi-web-arkweb-webmessageportapi.md) | ArkWeb_WebMessagePortAPI | ArkWeb_WebMessagePortAPI is a native API struct for web message ports. This struct provides functions such asmessage port creation, closing, message sending, and message receiving callback registration. This API is a corecomponent of the postMessage bridge, supporting the establishment of persistent bidirectional communication channelsbetween native code and web pages. It is suitable for scenarios where data interaction between native apps and webpages is required, solving cross-language communication challenges and improving app extensibility and developmentefficiency.<br>Web message port related APIs must be called on the UI thread by using the OH_ArkWeb_GetNativeAPImethod. Before calling, you are advised to use {@link ARKWEB_MEMBER_MISSING} to check the availability of functionpointers, preventing crashes caused by mismatches between the SDK and the device ROM. |
| [ArkWeb_WebMessageAPI](capi-web-arkweb-webmessageapi.md) | ArkWeb_WebMessageAPI | ArkWeb_WebMessageAPI is a native API struct for Web messages. This struct provides functions for creating anddestroying messages, setting and obtaining message types, and managing message data buffers. This API is part of thepostMessage bridge, supporting bidirectional communication between Native code and HTML pages.<br>Web message APIsmust be called on the UI thread by calling the OH_ArkWeb_GetNativeAPI method. Before calling, you are advised to use{@link ARKWEB_MEMBER_MISSING} to check the availability of function pointers, preventing crashes caused by amismatch between the SDK and device ROM. |
| [ArkWeb_CookieManagerAPI](capi-web-arkweb-cookiemanagerapi.md) | ArkWeb_CookieManagerAPI | ArkWeb_CookieManagerAPI is a Native API struct for cookie management. This struct provides capabilities suchas reading, setting, clearing, and synchronizing cookies. It is applicable to scenarios where user sessions need tobe managed and user preferences need to be tracked in the Web component, helping developers conveniently implementdata persistence and state synchronization.<br>CookieManager APIs must be obtained by calling theOH_ArkWeb_GetNativeAPI method in the UI thread. Before calling, you are advised to use {@link ARKWEB_MEMBER_MISSING}to check the availability of function pointers, so as to avoid crashes caused by mismatch between the SDK and thedevice ROM. |
| [ArkWeb_JavaScriptValueAPI](capi-web-arkweb-javascriptvalueapi.md) | - | ArkWeb_JavaScriptValueAPI is a JavaScript-related Native API struct. This struct provides functions forcreating JavaScript values, supporting the conversion of Native data into a JavaScript-recognizable format andreturning it to HTML. This conversion mechanism parses and encapsulates the Native data buffer based on thespecified JavaScript value type to generate the corresponding JavaScript value object. It is applicable toscenarios where data needs to be passed from the Native layer to the Web layer, enabling bidirectional datainteraction between Native and Web and improving app development flexibility.<br>Call the OH_ArkWeb_GetNativeAPI method on the UI thread to obtain JavaScript-related APIs. Before calling,you are advised to use {@link ARKWEB_MEMBER_MISSING} to check the availability of the function pointer,to prevent crashes caused by mismatch between the SDK and device ROM. |
| [ArkWeb_WebMessage*](capi-web-arkweb-webmessage8h.md) | ArkWeb_WebMessagePtr | ArkWeb_WebMessage is a web message struct used for cross-context message communication. It defines the basicformat and data carrying capability of messages. This struct serves as the fundamental data unit for web messagecommunication, supporting the transfer of strings and binary data between native code and web pages. |
| [ArkWeb_JavaScriptValue*](capi-web-arkweb-javascriptvalue8h.md) | ArkWeb_JavaScriptValuePtr | ArkWeb_JavaScriptValue is a struct used to encapsulate JavaScript values in native code. It provides basiccreation and manipulation capabilities for JavaScript values. This struct supports converting native data into aJavaScript-recognizable format, addressing type safety and format compatibility issues in bidirectional datatransfer between native and JavaScript. As the fundamental data transfer type in JavaScript bridge communication, ithelps reduce manual conversion costs, improve bridge communication efficiency, and enhance maintainability. |
| [ArkWeb_WebMessagePort*](capi-web-arkweb-webmessageport8h.md) | ArkWeb_WebMessagePortPtr | ArkWeb_WebMessagePort is a web message port struct that represents one of the two ports of a MessageChannel,used to send and receive messages. This struct supports bidirectional message communication between native code andweb pages. |

### Enum

| Name | typedef keyword | Description |
| -- | -- | -- |
| [ArkWeb_WebMessageType](#arkweb_webmessagetype) | ArkWeb_WebMessageType | Enumerates the data types of post message. |
| [ArkWeb_JavaScriptValueType](#arkweb_javascriptvaluetype) | ArkWeb_JavaScriptValueType | Enumerates the JavaScript data types. |

### Macro

| Name | Description |
| -- | -- |
| ARKWEB_MEMBER_EXISTS(s, f)<br>((intptr_t) & ((s)->f) - (intptr_t)(s) + sizeof((s)->f) <= *(size_t *)(s)) | Check whether the member variables of the current struct exist.<br>**Since**: 12 |
| ARKWEB_MEMBER_MISSING(s, f) (!ARKWEB_MEMBER_EXISTS(s, f) \|\| !((s)->f)) | Return false if the struct member does not exist, otherwise true.<br>**Since**: 12 |

### Function

| Name | typedef keyword | Description |
| -- | -- | -- |
| [typedef void (\*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData)](#arkweb_onjavascriptcallback) | ArkWeb_OnJavaScriptCallback | Callback invoked when the injected JavaScript execution is complete. It is used to obtain the executionresult of JavaScript code in the Web component, for example, in scenarios where the native UI needs to be updated orsubsequent logic needs to be executed based on the data returned by JavaScript. |
| [typedef void (\*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)](#arkweb_onjavascriptproxycallback) | ArkWeb_OnJavaScriptProxyCallback | Callback invoked when a Proxy method is executed. Proxy methods are used for object interaction and customoperations between the native side and the JavaScript side. |
| [typedef ArkWeb_JavaScriptValuePtr (\*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)](#arkweb_onjavascriptproxycallbackwithresult) | ArkWeb_OnJavaScriptProxyCallbackWithResult | Callback invoked when a Proxy method is executed (with a return value). It is used to receive a notificationand return the execution result when JavaScript calls an injected Proxy method. This is suitable for implementingbridge communication between JavaScript and native code, for example, intercepting JavaScript calls, executingnative logic, computing results, and returning the results to JavaScript. |
| [typedef void (\*ArkWeb_OnComponentCallback)(const char* webTag, void* userData)](#arkweb_oncomponentcallback) | ArkWeb_OnComponentCallback | Callback for receiving Web component event notifications. It is used to receive lifecycle event notificationsof the Web component, such as status change notifications in scenarios like page loading completion, pagedestruction, and component visibility changes. |
| [typedef void (\*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y)](#arkweb_onscrollcallback) | ArkWeb_OnScrollCallback | Callback invoked when the Web component scrolls. |
| [typedef void (\*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData)](#arkweb_onmessageeventhandler) | ArkWeb_OnMessageEventHandler | Called when a post message is sent from the HTML page. |

## Enum type description

### ArkWeb_WebMessageType

```c
enum ArkWeb_WebMessageType
```

**Description**

Enumerates the data types of post message.

**Since**: 12

| Enum item | Description |
| -- | -- |
| ARKWEB_NONE = 0 | Error data. |
| ARKWEB_STRING | String data. |
| ARKWEB_BUFFER | Byte stream data. |

### ArkWeb_JavaScriptValueType

```c
enum ArkWeb_JavaScriptValueType
```

**Description**

Enumerates the JavaScript data types.

**Since**: 18

| Enum item | Description |
| -- | -- |
| ARKWEB_JAVASCRIPT_NONE = 0 | Error data. |
| ARKWEB_JAVASCRIPT_STRING | String data. |
| ARKWEB_JAVASCRIPT_BOOL | Boolean data type. |


## Function description

### ArkWeb_OnJavaScriptCallback()

```c
typedef void (*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData)
```

**Description**

Callback invoked when the injected JavaScript execution is complete. It is used to obtain the executionresult of JavaScript code in the Web component, for example, in scenarios where the native UI needs to be updated orsubsequent logic needs to be executed based on the data returned by JavaScript.

**Since**: 12

### ArkWeb_OnJavaScriptProxyCallback()

```c
typedef void (*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

**Description**

Callback invoked when a Proxy method is executed. Proxy methods are used for object interaction and customoperations between the native side and the JavaScript side.

**Since**: 12

### ArkWeb_OnJavaScriptProxyCallbackWithResult()

```c
typedef ArkWeb_JavaScriptValuePtr (*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

**Description**

Callback invoked when a Proxy method is executed (with a return value). It is used to receive a notificationand return the execution result when JavaScript calls an injected Proxy method. This is suitable for implementingbridge communication between JavaScript and native code, for example, intercepting JavaScript calls, executingnative logic, computing results, and returning the results to JavaScript.

**Since**: 18

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char\* webTag | Name of the **Web** component. |
| [const ArkWeb_JavaScriptBridgeData](capi-web-arkweb-javascriptbridgedata.md)\* dataArray | Pointer to data array. |
| size_t arraySize | Array size. |
| void\* userData | Pointer to user-defined data. |

### ArkWeb_OnComponentCallback()

```c
typedef void (*ArkWeb_OnComponentCallback)(const char* webTag, void* userData)
```

**Description**

Callback for receiving Web component event notifications. It is used to receive lifecycle event notificationsof the Web component, such as status change notifications in scenarios like page loading completion, pagedestruction, and component visibility changes.

**Since**: 12

### ArkWeb_OnScrollCallback()

```c
typedef void (*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y)
```

**Description**

Callback invoked when the Web component scrolls.

**Since**: 18

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char\* webTag | Name of the **Web** component. |
| void\* userData | Pointer to user-defined data. |
| double x | X-axis scroll offset. Unit: vp. |
| double y | Y-axis scroll offset. Unit: vp. |

### ArkWeb_OnMessageEventHandler()

```c
typedef void (*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData)
```

**Description**

Called when a post message is sent from the HTML page.

**Since**: 12

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char\* webTag | Name of the **Web** component. |
| [const ArkWeb_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) port | Post message port. |
| [const ArkWeb_WebMessagePtr](capi-web-arkweb-webmessage8h.md) message | Post message data. |
| void\* userData | User-defined data. |


