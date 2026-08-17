# native_interface_arkweb.h

## Overview

native_interface_arkweb.h is the core entry header file of ArkWeb Native API. It defines the enums, structs,and NDK function interfaces required for interaction between apps and the ArkWeb engine, covering features such asJavaScript execution and proxy injection, cookie management, blankless loading control, and kernel version selection.This module is suitable for scenarios that require deep interaction with the **Web** component through nativemethods. It addresses the technical challenge that complex capabilities of the ArkWeb component (such as JavaScriptbidirectional communication, cookie persistence, and kernel version switching) cannot be directly called at theArkTS layer, providing developers with complete low-level control to implement high-performance, customizable **Webcomponent features.

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Related module**: [Web](capi-web.md)

## Summary

### Struct

| Name | typedef keyword | Description |
| -- | -- | -- |
| [ArkWeb_BlanklessInfo](capi-web-arkweb-blanklessinfo.md) | ArkWeb_BlanklessInfo | Describes the first-screen loading prediction information, including the predicted first-screen similarityvalue, predicted first-screen loading time, and error code. The app uses this information to decide whether toenable the blankless loading frame insertion solution, which reduces the blank screen time by inserting pre-renderedframes during page loading. |

### Enum

| Name | typedef keyword | Description |
| -- | -- | -- |
| [ArkWebEngineVersion](#arkwebengineversion) | ArkWebEngineVersion | For ArkWeb kernel versions, see {@link Adaptation Guide for the M114 Kernel on OpenHarmony 6.0} and{@link Adaptation Guide for the M132 Kernel on OpenHarmony 7.0}. |

### Function

| Name | typedef keyword | Description |
| -- | -- | -- |
| [typedef void (\*NativeArkWeb_OnJavaScriptCallback)(const char*)](#nativearkweb_onjavascriptcallback) | NativeArkWeb_OnJavaScriptCallback | Called to return the result after the JavaScript code is executed. |
| [typedef char* (\*NativeArkWeb_OnJavaScriptProxyCallback)(const char** argv, int32_t argc)](#nativearkweb_onjavascriptproxycallback) | NativeArkWeb_OnJavaScriptProxyCallback | Called when a JavaScript proxy is registered. |
| [typedef void (\*NativeArkWeb_OnValidCallback)(const char*)](#nativearkweb_onvalidcallback) | NativeArkWeb_OnValidCallback | Called when a **Web** component is valid. |
| [typedef void (\*NativeArkWeb_OnDestroyCallback)(const char*)](#nativearkweb_ondestroycallback) | NativeArkWeb_OnDestroyCallback | Called when a **Web** component is destroyed. |
| [typedef void (\*OH_ArkWeb_OnCookieSaveCallback)(ArkWeb_ErrorCode errorCode)](#oh_arkweb_oncookiesavecallback) | OH_ArkWeb_OnCookieSaveCallback | Called when a cookie is saved. |
| [typedef void (\*OH_ArkWeb_OnCookieFetchCallback)(ArkWeb_ErrorCode errorCode, char* cookieValue)](#oh_arkweb_oncookiefetchcallback) | OH_ArkWeb_OnCookieFetchCallback | Defines a pointer to the callback invoked when the cookie fetch operation is complete. |
| [void OH_NativeArkWeb_RunJavaScript(const char* webTag, const char* jsCode, NativeArkWeb_OnJavaScriptCallback callback)](#oh_nativearkweb_runjavascript) | - | Loads and asynchronously executes a piece of JavaScript code in the context of the current page. Thisfunction must be called in the main thread. **Use case**: Used when you need to dynamically modify page content,obtain page runtime information, or interact with page JavaScript at the native layer, for example, obtaining formdata or executing custom scripts. |
| [void OH_NativeArkWeb_RegisterJavaScriptProxy(const char* webTag, const char* objName, const char** methodList, NativeArkWeb_OnJavaScriptProxyCallback* callback, int32_t size, bool needRefresh)](#oh_nativearkweb_registerjavascriptproxy) | - | Registers a list of object and function names, used to inject native objects into web pages and implementbidirectional communication between the app side and the frontend page. This is used in scenarios such as web pagescalling native functions, native code controlling web page behavior, and cross-layer interaction in hybrid apps. |
| [void OH_NativeArkWeb_UnregisterJavaScriptProxy(const char* webTag, const char* objName)](#oh_nativearkweb_unregisterjavascriptproxy) | - | Deletes a registered object and its callback functions, used to clean up JavaScript injection objects thatare no longer needed. Typical use cases: cleaning up injected objects when a page is destroyed, removingcorresponding native interfaces when a function module is unloaded, and preventing memory leaks. |
| [void OH_NativeArkWeb_SetJavaScriptProxyValidCallback(const char* webTag, NativeArkWeb_OnValidCallback callback)](#oh_nativearkweb_setjavascriptproxyvalidcallback) | - | Sets the callback invoked when an object can be registered. Used when specific logic needs to be executedafter a JavaScript proxy object is successfully registered, for example, notifying the page or logging aftersuccessful registration. |
| [NativeArkWeb_OnValidCallback OH_NativeArkWeb_GetJavaScriptProxyValidCallback(const char* webTag)](#oh_nativearkweb_getjavascriptproxyvalidcallback) | - | Obtains the callback used when a registered object is valid. |
| [void OH_NativeArkWeb_SetDestroyCallback(const char* webTag, NativeArkWeb_OnDestroyCallback callback)](#oh_nativearkweb_setdestroycallback) | - | Sets the callback invoked when the **Web** component is destroyed. Typical use cases: releasing resources,cleaning up states, or performing finalization operations when the **Web** component is destroyed, for example,releasing JavaScript proxy objects, canceling network requests, or closing file handles. |
| [NativeArkWeb_OnDestroyCallback OH_NativeArkWeb_GetDestroyCallback(const char* webTag)](#oh_nativearkweb_getdestroycallback) | - | Obtains the registered callback invoked when the **Web** component is destroyed. |
| [ArkWeb_ErrorCode OH_NativeArkWeb_LoadData(const char* webTag, const char* data, const char* mimeType, const char* encoding, const char* baseUrl, const char* historyUrl)](#oh_nativearkweb_loaddata) | - | Loads data or a URL. This function must be called in the main thread. Typical use cases: loading page contentfrom the network or local files, dynamically generating and displaying HTML content, implementing offline pagedisplay, and custom page rendering. |
| [void OH_NativeArkWeb_RegisterAsyncThreadJavaScriptProxy(const char* webTag, const ArkWeb_ProxyObjectWithResult* proxyObject, const char* permission)](#oh_nativearkweb_registerasyncthreadjavascriptproxy) | - | Registers a JavaScript object that contains callback methods with return values. The object is injected intoall frames of the current page, including all iframes, and can be accessed by the name specified inArkWeb_ProxyObjectWithResult. The object takes effect in JavaScript only after the next page load or reload. Thesemethods are executed in the worker thread of ArkWeb. Typical use cases: processing JavaScript calls and returningresults in the worker thread, for example, performing time-consuming computations, asynchronous task processing, andcomplex business logic processing, to avoid blocking the main thread. |
| [ArkWeb_BlanklessErrorCode OH_NativeArkWeb_SetBlanklessLoadingWithKey(const char* webTag, const char* key, bool isStarted)](#oh_nativearkweb_setblanklessloadingwithkey) | - | Sets whether blankless loading is enabled. This API must be used together withOH_NativeArkWeb_GetBlanklessInfoWithKey.> **NOTE>> - This API must be called after the page loading API is triggered. Other constraints are the same as those of> [OH_NativeArkWeb_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey).> - The page must be loaded in the component that calls this set of APIs.> - When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail. |
| [void OH_NativeArkWeb_ClearBlanklessLoadingCache(const char* key[], uint32_t size)](#oh_nativearkweb_clearblanklessloadingcache) | - | Clears the blankless loading cache of the page with a specified key value.<br>In an applet or web application, when the content changes significantly during page loading, an obvious scenechange may occur. If you are concerned about this change, you can use this API to clear the page cache. |
| [ArkWeb_BlanklessInfo OH_NativeArkWeb_GetBlanklessInfoWithKey(const char* webTag, const char* key)](#oh_nativearkweb_getblanklessinfowithkey) | - | Obtains the first screen loading prediction information, and starts to generate the loading transition frame.The application determines whether to enable blankless loading based on the information. For details, see [ArkWeb_BlanklessInfo](capi-web-arkweb-blanklessinfo.md). This API must be used together with the [OH_NativeArkWeb_SetBlanklessLoadingWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingwithkey) API and must be calledbefore the page loading API is triggered and after **WebViewController** is bound to the **Web** component.> **NOTE>> - The default size of the persistent cache capacity is 30 MB (about 30 pages). You can set the cache capacity by> calling [OH_NativeArkWeb_SetBlanklessLoadingCacheCapacity](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingcachecapacity). For details, see the description of this API.> When the maximum capacity is exceeded, the cache is updated based on the Least Recently Used (LRU) mechanism. The> persistent cache data that has been stored for more than seven days is automatically cleared. After the cache is> cleared, the optimization effect appears when the page is loaded for the third time.> - If the value of **similarity** in [ArkWeb_BlanklessInfo](capi-web-arkweb-blanklessinfo.md) is extremely low, check whether the key value is> correctly passed.> - After this API is called, page loading snapshot detection and transition frame generation calculation are enabled> , which generates certain resource overhead.> - Blankless loading consumes resources, which depends on the resolution of the **Web** component. It is assumed> that a width and a height of the resolution are respectively **w** and **h**. When a page is opened, the peak> memory usage increases by about **12×w×h** B. After the page is opened, the memory is reclaimed, which does not> affect the stable memory usage. When the size of the solid-state application cache is increased, the increased> cache of each page is about **w×h/10** B and the cache is located in the application cache. |
| [uint32_t OH_NativeArkWeb_SetBlanklessLoadingCacheCapacity(uint32_t capacity)](#oh_nativearkweb_setblanklessloadingcachecapacity) | - | Sets the persistent cache capacity for the blankless loading solution and returns the actual effective value.The default cache capacity is 30 MB, and the maximum value is 100 MB. When the actual cache exceeds the capacity,infrequently used transition frames are evicted for cleanup. Typical use cases: adjusting the cache size based onthe app memory usage, optimizing storage space usage, and balancing the blankless effect with system resourceconsumption. |
| [ArkWeb_ErrorCode OH_ArkWebCookieManager_SaveCookieSync()](#oh_arkwebcookiemanager_savecookiesync) | - | Persists all cookies currently accessible through the CookieManager API to the disk. If this API is used in anon-UI thread, you need to initialize the CookieManager API using {@link OH_ArkWeb_GetNativeAPI} first. Typical usecases: saving cookie states when the app exits or at specific times, for example, saving user login states, appconfiguration information, and session data, to ensure that the previous state can be restored after the apprestarts. |
| [void OH_ArkWebCookieManager_SaveCookieAsync(OH_ArkWeb_OnCookieSaveCallback callback)](#oh_arkwebcookiemanager_savecookieasync) | - | Persists all cookies currently accessible through the CookieManager API to the disk. If this API is used in anon-UI thread, you need to initialize the CookieManager API using {@link OH_ArkWeb_GetNativeAPI} first. Withoutinitializing the CookieManager API, this API is automatically executed on the UI thread. Typical use cases:asynchronously saving cookie states, for example, saving cookies asynchronously after page loading is complete orafter a user operation, to avoid blocking the main thread. |
| [void OH_NativeArkWeb_SetActiveWebEngineVersion(ArkWebEngineVersion webEngineVersion)](#oh_nativearkweb_setactivewebengineversion) | - |  |
| [ArkWebEngineVersion OH_NativeArkWeb_GetActiveWebEngineVersion()](#oh_nativearkweb_getactivewebengineversion) | - |  |
| [void OH_NativeArkWeb_LazyInitializeWebEngineInCookieManager(bool lazy)](#oh_nativearkweb_lazyinitializewebengineincookiemanager) | - |  |
| [bool OH_NativeArkWeb_IsActiveWebEngineEvergreen()](#oh_nativearkweb_isactivewebengineevergreen) | - |  |
| [ArkWeb_ErrorCode OH_ArkWebCookieManager_FetchCookieSync(const char* url, bool incognito, bool includeHttpOnly, bool includePartitionedCookies, char** cookieValue)](#oh_arkwebcookiemanager_fetchcookiesync) | - | Obtains the cookies corresponding to the specified URL. If this API is used in a non-UI thread, you need toinitialize the CookieManager API using {@link OH_ArkWeb_GetNativeAPI} first. |
| [void OH_ArkWebCookieManager_FetchCookieAsync(const char* url, bool incognito, bool includeHttpOnly, bool includePartitionedCookies, OH_ArkWeb_OnCookieFetchCallback callback)](#oh_arkwebcookiemanager_fetchcookieasync) | - | Asynchronously obtains the cookies corresponding to the specified URL. Without initializing the CookieManagerAPI, this API is automatically executed on the UI thread. |

## Enum type description

### ArkWebEngineVersion

```c
enum ArkWebEngineVersion
```

**Description**

For ArkWeb kernel versions, see {@link Adaptation Guide for the M114 Kernel on OpenHarmony 6.0} and{@link Adaptation Guide for the M132 Kernel on OpenHarmony 7.0}.

**Since**: 20

| Enum item | Description |
| -- | -- |
| SYSTEM_DEFAULT = 0 | System default kernel (see {@link Constraints}). The default kernel is M132 for OpenHarmony 6.0 and M144for OpenHarmony 7.0.<br>**Since**: 20 |
| ARKWEB_M114 = 1 | Legacy kernel of OpenHarmony 6.0. Developers can select this legacy kernel. If this kernel does not existon the system version, the setting does not take effect and the system default kernel is used.<br>**Since**: 20 |
| ARKWEB_M132 = 2 | Evergreen kernel of OpenHarmony 6.0 (legacy kernel of OpenHarmony 7.0). M132 is the default kernel ofOpenHarmony 6.0. If this kernel does not exist on the system version, the setting does not take effect and thesystem default kernel is used.<br>**Since**: 20 |
| ARKWEB_M144 = 3 | Evergreen kernel of OpenHarmony 7.0. M144 is the default kernel of OpenHarmony 7.0. If this kernel doesnot exist on the system version, the setting does not take effect and the system default kernel is used.<br>**Since**: 26.0.0 |
| ARKWEB_EVERGREEN = 99999 | Latest kernel of the system (evergreen kernel). Developers can select to use the latest kernel on eachsystem version.<br>**Since**: 23 |


## Function description

### NativeArkWeb_OnJavaScriptCallback()

```c
typedef void (*NativeArkWeb_OnJavaScriptCallback)(const char*)
```

**Description**

Called to return the result after the JavaScript code is executed.

**Since**: 11

### NativeArkWeb_OnJavaScriptProxyCallback()

```c
typedef char* (*NativeArkWeb_OnJavaScriptProxyCallback)(const char** argv, int32_t argc)
```

**Description**

Called when a JavaScript proxy is registered.

**Since**: 11

### NativeArkWeb_OnValidCallback()

```c
typedef void (*NativeArkWeb_OnValidCallback)(const char*)
```

**Description**

Called when a **Web** component is valid.

**Since**: 11

### NativeArkWeb_OnDestroyCallback()

```c
typedef void (*NativeArkWeb_OnDestroyCallback)(const char*)
```

**Description**

Called when a **Web** component is destroyed.

**Since**: 11

### OH_ArkWeb_OnCookieSaveCallback()

```c
typedef void (*OH_ArkWeb_OnCookieSaveCallback)(ArkWeb_ErrorCode errorCode)
```

**Description**

Called when a cookie is saved.

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| (ArkWeb_ErrorCode errorCode | [ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): The cookie is successfully saved.<br>[ARKWEB_COOKIE_SAVE_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode): Failed to save the cookie.<br>[ARKWEB_COOKIE_MANAGER_INITIALIZE_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode): The **CookieManager** initialization failed. |

### OH_ArkWeb_OnCookieFetchCallback()

```c
typedef void (*OH_ArkWeb_OnCookieFetchCallback)(ArkWeb_ErrorCode errorCode, char* cookieValue)
```

**Description**

Defines a pointer to the callback invoked when the cookie fetch operation is complete.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (ArkWeb_ErrorCode errorCode | Error code for the cookie fetch callback.<br>[ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): The cookie is fetched successfully.<br>[ARKWEB_INVALID_URL](capi-arkweb-error-code-h.md#arkweb_errorcode): Invalid URL.<br>[ARKWEB_LIBRARY_OPEN_FAILURE](capi-arkweb-error-code-h.md#arkweb_errorcode): Failed to open the dynamic link library.<br>[ARKWEB_LIBRARY_SYMBOL_NOT_FOUND](capi-arkweb-error-code-h.md#arkweb_errorcode): The required symbol is not found in the dynamic link library. |
| char\* cookieValue | Cookies corresponding to the URL. The function allocates memory for cookieValue, and thedeveloper must release the string using {@link OH_ArkWeb_ReleaseString}. |

### OH_NativeArkWeb_RunJavaScript()

```c
void OH_NativeArkWeb_RunJavaScript(const char* webTag, const char* jsCode, NativeArkWeb_OnJavaScriptCallback callback)
```

**Description**

Loads and asynchronously executes a piece of JavaScript code in the context of the current page. Thisfunction must be called in the main thread. **Use case**: Used when you need to dynamically modify page content,obtain page runtime information, or interact with page JavaScript at the native layer, for example, obtaining formdata or executing custom scripts.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| const char* jsCode | A piece of JavaScript code script. |
| [NativeArkWeb_OnJavaScriptCallback](capi-native-interface-arkweb-h.md#nativearkweb_onjavascriptcallback) callback | Callback for notifying the code execution result. |

### OH_NativeArkWeb_RegisterJavaScriptProxy()

```c
void OH_NativeArkWeb_RegisterJavaScriptProxy(const char* webTag, const char* objName, const char** methodList, NativeArkWeb_OnJavaScriptProxyCallback* callback, int32_t size, bool needRefresh)
```

**Description**

Registers a list of object and function names, used to inject native objects into web pages and implementbidirectional communication between the app side and the frontend page. This is used in scenarios such as web pagescalling native functions, native code controlling web page behavior, and cross-layer interaction in hybrid apps.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| const char* objName | Name of the registered object. |
| const char** methodList | Name of the registered method list. |
| [NativeArkWeb_OnJavaScriptProxyCallback](capi-native-interface-arkweb-h.md#nativearkweb_onjavascriptproxycallback)* callback | Registered callback. |
| int32_t size | Number of registered callbacks. |
| bool needRefresh | Whether a page need to be refreshed. The value **true** indicates that the page needs to berefreshed, and **false** indicates the opposite. |

### OH_NativeArkWeb_UnregisterJavaScriptProxy()

```c
void OH_NativeArkWeb_UnregisterJavaScriptProxy(const char* webTag, const char* objName)
```

**Description**

Deletes a registered object and its callback functions, used to clean up JavaScript injection objects thatare no longer needed. Typical use cases: cleaning up injected objects when a page is destroyed, removingcorresponding native interfaces when a function module is unloaded, and preventing memory leaks.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| const char* objName | Name of the registered object. |

### OH_NativeArkWeb_SetJavaScriptProxyValidCallback()

```c
void OH_NativeArkWeb_SetJavaScriptProxyValidCallback(const char* webTag, NativeArkWeb_OnValidCallback callback)
```

**Description**

Sets the callback invoked when an object can be registered. Used when specific logic needs to be executedafter a JavaScript proxy object is successfully registered, for example, notifying the page or logging aftersuccessful registration.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| [NativeArkWeb_OnValidCallback](capi-native-interface-arkweb-h.md#nativearkweb_onvalidcallback) callback | Callback used when an object is valid. |

### OH_NativeArkWeb_GetJavaScriptProxyValidCallback()

```c
NativeArkWeb_OnValidCallback OH_NativeArkWeb_GetJavaScriptProxyValidCallback(const char* webTag)
```

**Description**

Obtains the callback used when a registered object is valid.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |

**Returns**:

| Type | Description |
| -- | -- |
| [NativeArkWeb_OnValidCallback](capi-native-interface-arkweb-h.md#nativearkweb_onvalidcallback) | Callback used when a registered object is valid. If no valid callback function is set for the webTag<br>     parameter, a null pointer is returned. |

### OH_NativeArkWeb_SetDestroyCallback()

```c
void OH_NativeArkWeb_SetDestroyCallback(const char* webTag, NativeArkWeb_OnDestroyCallback callback)
```

**Description**

Sets the callback invoked when the **Web** component is destroyed. Typical use cases: releasing resources,cleaning up states, or performing finalization operations when the **Web** component is destroyed, for example,releasing JavaScript proxy objects, canceling network requests, or closing file handles.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| [NativeArkWeb_OnDestroyCallback](capi-native-interface-arkweb-h.md#nativearkweb_ondestroycallback) callback | Callback invoked when the Web component is destroyed. |

### OH_NativeArkWeb_GetDestroyCallback()

```c
NativeArkWeb_OnDestroyCallback OH_NativeArkWeb_GetDestroyCallback(const char* webTag)
```

**Description**

Obtains the registered callback invoked when the **Web** component is destroyed.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 11

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |

**Returns**:

| Type | Description |
| -- | -- |
| [NativeArkWeb_OnDestroyCallback](capi-native-interface-arkweb-h.md#nativearkweb_ondestroycallback) | Returns the registered callback for when the Web component is destroyed. If the destroy callback specified<br>     by the webTag parameter is not set, a null pointer is returned. |

### OH_NativeArkWeb_LoadData()

```c
ArkWeb_ErrorCode OH_NativeArkWeb_LoadData(const char* webTag, const char* data, const char* mimeType, const char* encoding, const char* baseUrl, const char* historyUrl)
```

**Description**

Loads data or a URL. This function must be called in the main thread. Typical use cases: loading page contentfrom the network or local files, dynamically generating and displaying HTML content, implementing offline pagedisplay, and custom page rendering.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 15

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| const char* data | String being base64 or URL encoded, which cannot be empty. |
| const char* mimeType | Media type, such as **text/html**, which cannot be empty. |
| const char* encoding | Encoding type, such as **UTF-8**, which cannot be empty. |
| const char* baseUrl | Specified URL path (using the "http", "https", or "data" protocol), assigned to window.origin by theWeb component. |
| const char* historyUrl | Historical URL. If this parameter is not empty, it can be managed in historical records toimplement backward and forward navigation. |

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWeb_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | Error codes of OH_NativeArkWeb_LoadData.<br>     <br>[ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): data loaded successfully.<br>     <br>[ARKWEB_INVALID_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode): a required parameter is not specified, the parameter type is incorrect, or<br>     parameter verification fails.<br>     <br>[ARKWEB_INIT_ERROR](capi-arkweb-error-code-h.md#arkweb_errorcode): initialization fails. No valid Web component is found based on the passed "webTag"<br>     .<br>     <br>[ARKWEB_LIBRARY_OPEN_FAILURE](capi-arkweb-error-code-h.md#arkweb_errorcode): failed to open the dynamic link library. Check whether the library file<br>     path is correct, whether the library file is corrupted, and whether you have sufficient access permissions.<br>     <br>[ARKWEB_LIBRARY_SYMBOL_NOT_FOUND](capi-arkweb-error-code-h.md#arkweb_errorcode): the required symbol is not found in the dynamic link library. |

### OH_NativeArkWeb_RegisterAsyncThreadJavaScriptProxy()

```c
void OH_NativeArkWeb_RegisterAsyncThreadJavaScriptProxy(const char* webTag, const ArkWeb_ProxyObjectWithResult* proxyObject, const char* permission)
```

**Description**

Registers a JavaScript object that contains callback methods with return values. The object is injected intoall frames of the current page, including all iframes, and can be accessed by the name specified inArkWeb_ProxyObjectWithResult. The object takes effect in JavaScript only after the next page load or reload. Thesemethods are executed in the worker thread of ArkWeb. Typical use cases: processing JavaScript calls and returningresults in the worker thread, for example, performing time-consuming computations, asynchronous task processing, andcomplex business logic processing, to avoid blocking the main thread.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| [const ArkWeb_ProxyObjectWithResult](capi-web-arkweb-proxyobjectwithresult.md)* proxyObject | Object to be registered. |
| const char* permission | A JSON string used to configure the object and method levels of the JSBridge permission. Thisvalue is empty by default. |

### OH_NativeArkWeb_SetBlanklessLoadingWithKey()

```c
ArkWeb_BlanklessErrorCode OH_NativeArkWeb_SetBlanklessLoadingWithKey(const char* webTag, const char* key, bool isStarted)
```

**Description**

Sets whether blankless loading is enabled. This API must be used together withOH_NativeArkWeb_GetBlanklessInfoWithKey.> **NOTE>> - This API must be called after the page loading API is triggered. Other constraints are the same as those of> [OH_NativeArkWeb_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey).> - The page must be loaded in the component that calls this set of APIs.> - When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail.

**Required permission**: ohos.permission.INTERNET and ohos.permission.GET_NETWORK_INFO

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| const char* key | Unique key that identifies this page. It must be the same as the key value of the[OH_NativeArkWeb_GetBlanklessInfoWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_getblanklessinfowithkey) API.<br>Valid value range: non-empty, with a maximum length of 2048 characters.<br>Behavior for invalid values: returns the error code {@link ArkWeb_BlanklessErrorCode}, and frame insertiondoes not take effect. |
| bool isStarted | Whether to enable frame insertion. The value **true** means to enable frame insertion. Select thisoption when the first screen of the page has high similarity and the blank screen time needs to be reduced toimprove the loading experience. The value **false** means to disable frame insertion. Select this option whenthe page transition is too large, resulting in low similarity, or when the loading experience does not need tobe optimized.<br>Default value: **false**. |

**Returns**:

| Type | Description |
| -- | -- |
| ArkWeb_BlanklessErrorCode | Enumerates the error codes. For details, see {@link ArkWeb_BlanklessErrorCode}. |

### OH_NativeArkWeb_ClearBlanklessLoadingCache()

```c
void OH_NativeArkWeb_ClearBlanklessLoadingCache(const char* key[], uint32_t size)
```

**Description**

Clears the blankless loading cache of the page with a specified key value.<br>In an applet or web application, when the content changes significantly during page loading, an obvious scenechange may occur. If you are concerned about this change, you can use this API to clear the page cache.

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* key[] | The list of key values of pages cached in the blankless loading solution. These key values arespecified in OH_NativeArkWeb_GetBlanklessInfoWithKey.The default value is the list of key values of all pages cached in the blankless loading solution.The key length cannot exceed 2048 characters, and the number of keys must be less than or equal to 100. TheURL is the same as that input to the Web component during page loading.When the key length exceeds 2048 characters, the key does not take effect. When the number of keys exceeds100, the first 100 keys are used. If this parameter is set to NULL, the default value is used. |
| uint32_t size | Size of the keys array.<br>Valid value range: 0 to 100. If the value exceeds 100, the first 100 keys in the array are used.<br>Behavior for invalid values: if the value is greater than 100, the first 100 keys are used. |

### OH_NativeArkWeb_GetBlanklessInfoWithKey()

```c
ArkWeb_BlanklessInfo OH_NativeArkWeb_GetBlanklessInfoWithKey(const char* webTag, const char* key)
```

**Description**

Obtains the first screen loading prediction information, and starts to generate the loading transition frame.The application determines whether to enable blankless loading based on the information. For details, see [ArkWeb_BlanklessInfo](capi-web-arkweb-blanklessinfo.md). This API must be used together with the [OH_NativeArkWeb_SetBlanklessLoadingWithKey](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingwithkey) API and must be calledbefore the page loading API is triggered and after **WebViewController** is bound to the **Web** component.> **NOTE>> - The default size of the persistent cache capacity is 30 MB (about 30 pages). You can set the cache capacity by> calling [OH_NativeArkWeb_SetBlanklessLoadingCacheCapacity](capi-native-interface-arkweb-h.md#oh_nativearkweb_setblanklessloadingcachecapacity). For details, see the description of this API.> When the maximum capacity is exceeded, the cache is updated based on the Least Recently Used (LRU) mechanism. The> persistent cache data that has been stored for more than seven days is automatically cleared. After the cache is> cleared, the optimization effect appears when the page is loaded for the third time.> - If the value of **similarity** in [ArkWeb_BlanklessInfo](capi-web-arkweb-blanklessinfo.md) is extremely low, check whether the key value is> correctly passed.> - After this API is called, page loading snapshot detection and transition frame generation calculation are enabled> , which generates certain resource overhead.> - Blankless loading consumes resources, which depends on the resolution of the **Web** component. It is assumed> that a width and a height of the resolution are respectively **w** and **h**. When a page is opened, the peak> memory usage increases by about **12×w×h** B. After the page is opened, the memory is reclaimed, which does not> affect the stable memory usage. When the size of the solid-state application cache is increased, the increased> cache of each page is about **w×h/10** B and the cache is located in the application cache.

**Required permission**: ohos.permission.INTERNET and ohos.permission.GET_NETWORK_INFO

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* webTag | Name of the **Web** component. |
| const char* key | Key value that uniquely identifies the page.The value cannot be empty and can contain a maximum of 2048 characters.Invalid values do not take effect. |

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWeb_BlanklessInfo](capi-web-arkweb-blanklessinfo.md) | Prediction information about blankless loading, including the first screen similarity and first screen<br> loading duration. The application determines whether to enable blankless loading based on the prediction information. |

### OH_NativeArkWeb_SetBlanklessLoadingCacheCapacity()

```c
uint32_t OH_NativeArkWeb_SetBlanklessLoadingCacheCapacity(uint32_t capacity)
```

**Description**

Sets the persistent cache capacity for the blankless loading solution and returns the actual effective value.The default cache capacity is 30 MB, and the maximum value is 100 MB. When the actual cache exceeds the capacity,infrequently used transition frames are evicted for cleanup. Typical use cases: adjusting the cache size based onthe app memory usage, optimizing storage space usage, and balancing the blankless effect with system resourceconsumption.

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| uint32_t capacity | Sets the persistent cache capacity, in MB. The maximum value cannot exceed 100 MB.<br>Default value: 30 MB.<br>Valid range: 0 to 100. When set to 0, there is no cache space and the feature is globally disabled.<br>Invalid value handling: When the value is greater than 100, the effective value is 100. |

**Returns**:

| Type | Description |
| -- | -- |
| uint32_t | Effective capacity value, in MB, ranging from 0 to 100.<br>     <br>If the value is greater than 100, the effective value is 100. |

### OH_ArkWebCookieManager_SaveCookieSync()

```c
ArkWeb_ErrorCode OH_ArkWebCookieManager_SaveCookieSync()
```

**Description**

Persists all cookies currently accessible through the CookieManager API to the disk. If this API is used in anon-UI thread, you need to initialize the CookieManager API using {@link OH_ArkWeb_GetNativeAPI} first. Typical usecases: saving cookie states when the app exits or at specific times, for example, saving user login states, appconfiguration information, and session data, to ensure that the previous state can be restored after the apprestarts.

**Since**: 20

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWeb_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | Error codes of OH_ArkWebCookieManager_SaveCookieSync. Check whether the disk space is sufficient, whether<br>     write permission is available, and whether the cookie data format is correct.<br>     <br>[ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): the cookie is saved successfully.<br>     <br>[ARKWEB_COOKIE_SAVE_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode): failed to save the cookie.<br>     <br>[ARKWEB_COOKIE_MANAGER_INITIALIZE_FAILED](capi-arkweb-error-code-h.md#arkweb_errorcode): failed to initialize CookieManager.<br>     <br>[ARKWEB_COOKIE_MANAGER_NOT_INITIALIZED](capi-arkweb-error-code-h.md#arkweb_errorcode): on a non-UI thread, calling this API without initializing the<br>     CookieManager API is not allowed. Use {@link OH_ArkWeb_GetNativeAPI} to initialize the CookieManager API first. |

### OH_ArkWebCookieManager_SaveCookieAsync()

```c
void OH_ArkWebCookieManager_SaveCookieAsync(OH_ArkWeb_OnCookieSaveCallback callback)
```

**Description**

Persists all cookies currently accessible through the CookieManager API to the disk. If this API is used in anon-UI thread, you need to initialize the CookieManager API using {@link OH_ArkWeb_GetNativeAPI} first. Withoutinitializing the CookieManager API, this API is automatically executed on the UI thread. Typical use cases:asynchronously saving cookie states, for example, saving cookies asynchronously after page loading is complete orafter a user operation, to avoid blocking the main thread.

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_ArkWeb_OnCookieSaveCallback](capi-native-interface-arkweb-h.md#oh_arkweb_oncookiesavecallback) callback | Callback invoked after the cookie is saved successfully or fails. When a callback is passed in, theoperation result is received asynchronously using the callback, which is suitable for scenarios requiringasynchronous notification of the save result. When no callback is passed in, the behavior may vary depending onthe specific implementation. |

### OH_NativeArkWeb_SetActiveWebEngineVersion()

```c
void OH_NativeArkWeb_SetActiveWebEngineVersion(ArkWebEngineVersion webEngineVersion)
```

**Description**

**Since**: 20

**Parameters**:

| Parameter | Description |
| -- | -- |
| { | ArkWebEngineVersion } webEngineVersion - ArkWeb kernel version.For details, see [ArkWebEngineVersion](capi-native-interface-arkweb-h.md#arkwebengineversion). |

### OH_NativeArkWeb_GetActiveWebEngineVersion()

```c
ArkWebEngineVersion OH_NativeArkWeb_GetActiveWebEngineVersion()
```

**Description**

**Since**: 20

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWebEngineVersion](capi-native-interface-arkweb-h.md#arkwebengineversion) | The current ArkWeb kernel version defined by [ArkWebEngineVersion](capi-native-interface-arkweb-h.md#arkwebengineversion). |

### OH_NativeArkWeb_LazyInitializeWebEngineInCookieManager()

```c
void OH_NativeArkWeb_LazyInitializeWebEngineInCookieManager(bool lazy)
```

**Description**

**Since**: 22

**Parameters**:

| Parameter | Description |
| -- | -- |
| { | bool } lazy - Controls whether to delay the initialization of the web engine. |

### OH_NativeArkWeb_IsActiveWebEngineEvergreen()

```c
bool OH_NativeArkWeb_IsActiveWebEngineEvergreen()
```

**Description**

**Since**: 23

**Returns**:

| Type | Description |
| -- | -- |
| bool | Whether the kernel used by the current app is the Evergreen kernel. The value true indicates it is the<br>     Evergreen kernel, and false indicates it is not. |

### OH_ArkWebCookieManager_FetchCookieSync()

```c
ArkWeb_ErrorCode OH_ArkWebCookieManager_FetchCookieSync(const char* url, bool incognito, bool includeHttpOnly, bool includePartitionedCookies, char** cookieValue)
```

**Description**

Obtains the cookies corresponding to the specified URL. If this API is used in a non-UI thread, you need toinitialize the CookieManager API using {@link OH_ArkWeb_GetNativeAPI} first.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* url | URL to which the cookies belong. It is recommended to provide the complete URL. |
| bool incognito | Whether to obtain the in-memory cookies of the webview in incognito mode. The value **trueindicates obtaining cookies in incognito mode, and **false** indicates obtaining cookies in non-incognito mode. |
| bool includeHttpOnly | Whether to include cookies marked with the HTTP-Only attribute in cookieValue. The value**true** indicates that they are included, and **false** indicates that they are not. |
| bool includePartitionedCookies | Whether to include first-party partitioned cookies in cookieValue. The value**true** indicates that they are included, and **false** indicates that they are not. |
| char** cookieValue | Cookie value corresponding to the URL. The function allocates memory for cookieValue, and thedeveloper must release the string using {@link OH_ArkWeb_ReleaseString}. |

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWeb_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | Result code.<br>     <br>[ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): The cookie is obtained successfully.<br>     <br>[ARKWEB_INVALID_URL](capi-arkweb-error-code-h.md#arkweb_errorcode): Invalid URL.<br>     <br>[ARKWEB_INVALID_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode): Invalid parameter.<br>     <br>[ARKWEB_COOKIE_MANAGER_NOT_INITIALIZED](capi-arkweb-error-code-h.md#arkweb_errorcode): In a non-UI thread, calling this API without initializing the<br>     CookieManager API is not allowed. Initialize the CookieManager API using OH_ArkWeb_GetNativeAPI first.<br>     <br>[ARKWEB_LIBRARY_OPEN_FAILURE](capi-arkweb-error-code-h.md#arkweb_errorcode): Failed to open the dynamic link library.<br>     <br>[ARKWEB_LIBRARY_SYMBOL_NOT_FOUND](capi-arkweb-error-code-h.md#arkweb_errorcode): The required symbol is not found in the dynamic link library. |

### OH_ArkWebCookieManager_FetchCookieAsync()

```c
void OH_ArkWebCookieManager_FetchCookieAsync(const char* url, bool incognito, bool includeHttpOnly, bool includePartitionedCookies, OH_ArkWeb_OnCookieFetchCallback callback)
```

**Description**

Asynchronously obtains the cookies corresponding to the specified URL. Without initializing the CookieManagerAPI, this API is automatically executed on the UI thread.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* url | URL to which the cookies belong. It is recommended to provide the complete URL. |
| bool incognito | Whether to obtain the in-memory cookies of the webview in incognito mode. The value **trueindicates obtaining cookies in incognito mode, and **false** indicates obtaining cookies in non-incognito mode. |
| bool includeHttpOnly | Whether to include cookies marked with the HTTP-Only attribute in cookieValue. The value**true** indicates that they are included, and **false** indicates that they are not. |
| bool includePartitionedCookies | Whether to include first-party partitioned cookies in cookieValue. The value**true** indicates that they are included, and **false** indicates that they are not. |
| [OH_ArkWeb_OnCookieFetchCallback](capi-native-interface-arkweb-h.md#oh_arkweb_oncookiefetchcallback) callback | Callback invoked after the cookies are obtained. |


