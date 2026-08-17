# ArkWeb_CookieManagerAPI

```c
typedef struct ArkWeb_CookieManagerAPI {...} ArkWeb_CookieManagerAPI
```

## Overview

ArkWeb_CookieManagerAPI is a Native API struct for cookie management. This struct provides capabilities suchas reading, setting, clearing, and synchronizing cookies. It is applicable to scenarios where user sessions need tobe managed and user preferences need to be tracked in the Web component, helping developers conveniently implementdata persistence and state synchronization.<br>CookieManager APIs must be obtained by calling theOH_ArkWeb_GetNativeAPI method in the UI thread. Before calling, you are advised to use [ARKWEB_MEMBER_MISSING](capi-arkweb-type-h.md#arkweb_member_missing)to check the availability of function pointers, so as to avoid crashes caused by mismatch between the SDK and thedevice ROM.

**Since**: 12

**Related module**: [Web](capi-web.md)

**Header file**: [arkweb_type.h](capi-arkweb-type-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| size_t size | Size of the struct. |


### Member functions

| Name | Description |
| -- | -- |
| [ArkWeb_ErrorCode (\*fetchCookieSync)(const char* url, bool incognito, bool includeHttpOnly, char** cookieValue)](#fetchcookiesync) | Obtains the cookie value of a specified URL. This method is used in scenarios such as user login statemaintenance, session management, and personalized configuration reading. This method must be called in the UIthread. Before calling, you are advised to check the availability of the function pointer. |
| [ArkWeb_ErrorCode (\*configCookieSync)(const char* url,const char* cookieValue, bool incognito, bool includeHttpOnly)](#configcookiesync) | Sets the cookie value of a specified URL. This method is used in scenarios such as saving user preferencesettings, maintaining login state, and saving session information. This method must be called in the UI thread.Before calling, you are advised to check the availability of the function pointer. |
| [bool (\*existCookies)(bool incognito)](#existcookies) | Check whether cookies exist. |
| [void (\*clearAllCookiesSync)(bool incognito)](#clearallcookiessync) | Clears all cookies (including persistent cookies and session cookies). This method is used in scenariossuch as user logout, clearing privacy data, and resetting user state. If you only need to clear session cookies,you are advised to use [clearSessionCookiesSync](capi-web-arkweb-cookiemanagerapi.md#clearsessioncookiessync). This method must be called in the UI thread. Beforecalling, you are advised to check the availability of the function pointer. |
| [void (\*clearSessionCookiesSync)()](#clearsessioncookiessync) | Clears all session cookies. This method is used in scenarios such as clearing temporary session data,closing all sessions, and cleaning up session timeouts. This method must be called in the UI thread. Beforecalling, you are advised to check the availability of the function pointer. |

## Member function description

### fetchCookieSync()

```c
ArkWeb_ErrorCode (*fetchCookieSync)(const char* url, bool incognito, bool includeHttpOnly, char** cookieValue)
```

**Description**

Obtains the cookie value of a specified URL. This method is used in scenarios such as user login statemaintenance, session management, and personalized configuration reading. This method must be called in the UIthread. Before calling, you are advised to check the availability of the function pointer.

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* url | URL of the cookie to obtain. A complete URL is recommended. |
|  bool incognito | Whether to obtain the in-memory cookies of the Web component in privacy mode. The value truemeans to obtain cookies in privacy mode (automatically cleared after app exit), and false means to obtaincookies in non-privacy mode (persistent storage). |
|  bool includeHttpOnly | Whether to include cookies marked with the HTTP-Only attribute in cookieValue. The valuetrue means to include them, and false means not to include them.**Note:** Reading HTTP-Only cookies must comply with security and compliance requirements. |
|  char** cookieValue | Output parameter, which is a pointer to the cookie value corresponding to the URL. The memoryis allocated internally by the function, and the caller must release it after use. The return value is astring that contains all matching cookie items in the format of name=value, where name and value are thename and value of the cookie, respectively. |

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWeb_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | Result code.<br>         <br>[ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): success.<br>         <br>[ARKWEB_INVALID_URL](capi-arkweb-error-code-h.md#arkweb_errorcode): invalid URL. Possible causes: incorrect URL format, empty URL, or non-<br>         compliant URL.<br>         <br>[ARKWEB_INVALID_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode): invalid cookieValue parameter. |

### configCookieSync()

```c
ArkWeb_ErrorCode (*configCookieSync)(const char* url,const char* cookieValue, bool incognito, bool includeHttpOnly)
```

**Description**

Sets the cookie value of a specified URL. This method is used in scenarios such as saving user preferencesettings, maintaining login state, and saving session information. This method must be called in the UI thread.Before calling, you are advised to check the availability of the function pointer.

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char* url | URL of the specified cookie. It must be a complete URL. |
| const char* cookieValue | Value of the cookie to set, in the format of name=value, where name and value are the nameand value of the cookie, respectively. |
|  bool incognito | Whether to set the cookie for the corresponding URL in privacy mode. The value true means thecookie is set in privacy mode (automatically cleared after the app exits), and false means the cookie is setin non-privacy mode (persistent storage). |
|  bool includeHttpOnly | Whether to include or overwrite cookies marked with the HTTP-Only attribute. The valuetrue means cookies marked with the HTTP-Only attribute can also be included in the result or overwritten,and false means only non-HTTP-Only cookies are processed.**Note:** Overwriting HTTP-Only cookies may affect security. Ensure that this meets your service securityrequirements. |

**Returns**:

| Type | Description |
| -- | -- |
| [ArkWeb_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | Result code.<br>         <br>[ARKWEB_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode): the cookie is set successfully.<br>         <br>[ARKWEB_INVALID_URL](capi-arkweb-error-code-h.md#arkweb_errorcode): invalid URL. Possible causes: incorrect URL format, empty URL, or non-<br>         compliant URL.<br>         <br>[ARKWEB_INVALID_COOKIE_VALUE](capi-arkweb-error-code-h.md#arkweb_errorcode): invalid cookieValue parameter. |

### existCookies()

```c
bool (*existCookies)(bool incognito)
```

**Description**

Check whether cookies exist.

**Parameters**:

| Parameter | Description |
| -- | -- |
| bool incognito | True indicates whether cookies exist in privacy mode,and false indicates whether cookies exist in non-privacy mode. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | True indicates that the cookie exists, and false indicates that the cookie does not exist. |

### clearAllCookiesSync()

```c
void (*clearAllCookiesSync)(bool incognito)
```

**Description**

Clears all cookies (including persistent cookies and session cookies). This method is used in scenariossuch as user logout, clearing privacy data, and resetting user state. If you only need to clear session cookies,you are advised to use [clearSessionCookiesSync](capi-web-arkweb-cookiemanagerapi.md#clearsessioncookiessync). This method must be called in the UI thread. Beforecalling, you are advised to check the availability of the function pointer.

### clearSessionCookiesSync()

```c
void (*clearSessionCookiesSync)()
```

**Description**

Clears all session cookies. This method is used in scenarios such as clearing temporary session data,closing all sessions, and cleaning up session timeouts. This method must be called in the UI thread. Beforecalling, you are advised to check the availability of the function pointer.


