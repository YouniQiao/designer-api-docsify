# GeolocationPermissions

GeolocationPermissions is the geolocation permission management object for the Web component. It provides management capabilities such as querying, authorizing, and deleting saved geolocation permission statuses in the Web component. With GeolocationPermissions, an app can pre-authorize access for a specific origin before a web page initiates a geolocation request, and can also proactively query or clear saved permission records without relying on the pop-up authorization flow when a web page requests permission.GeolocationPermissions is suitable for scenarios where proactive management of Web component geolocation permissions is required. For example, an app may want to pre-authorize trusted websites to access geolocation, avoiding authorization prompts on each visit; or an app may need to clear geolocation permission records that are no longer needed by the user. The following permissions are required for accessing geolocation: ohos.permission.LOCATION, ohos.permission.APPROXIMATELY_LOCATION, and ohos.permission.LOCATION_IN_BACKGROUND. For details about the permissions, see [Development Guide for Location Permission Application](../../../device/location/location-permission-guidelines.md).

> **NOTE：**&gt;
> - You must load the **Web** component before calling the APIs in **GeolocationPermissions**.

**Since:** 9

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## allowGeolocation

```TypeScript
static allowGeolocation(origin: string, incognito?: boolean): void
```

Allows the specified origin to use the geolocation APIs. It is used to pre-authorize geolocation permission for trusted websites to avoid repeated pop-ups, or to allow an app to proactively manage the geolocation authorization of a specific origin.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## deleteAllGeolocation

```TypeScript
static deleteAllGeolocation(incognito?: boolean): void
```

Clears the geolocation permission status of all origins. It is used to revoke geolocation authorization in batches in scenarios such as user logout or one-click clearing.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

## deleteGeolocation

```TypeScript
static deleteGeolocation(origin: string, incognito?: boolean): void
```

Clears the geolocation permission status of the specified origin. It is used to revoke the geolocation authorization of a specified website, or to provide an app with the ability to manage permissions by origin.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getAccessibleGeolocation

```TypeScript
static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>
```

Obtains the geolocation permission status of the specified origin. This API uses a promise to return the result. It is used to query the geolocation authorization result of a specified website, such as displaying the permission status on a settings page or verifying authorization before access.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| incognito | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getAccessibleGeolocation

```TypeScript
static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void
```

Obtains the geolocation permission status of the specified origin. This API uses an asynchronous callback to return the result. It is used to query the geolocation authorization result of a specified website, such as displaying the permission status on a settings page or verifying authorization before access.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getStoredGeolocation

```TypeScript
static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>
```

Obtains the geolocation permission status of all origins. This API uses a promise to return the result. It is used to obtain a list of websites that have been granted geolocation permission, such as displaying on a privacy settings page or batch management on a permission management page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getStoredGeolocation

```TypeScript
static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void
```

Obtains the geolocation permission status of all origins. This API uses an asynchronous callback to return the result. It is used to obtain a list of websites that have been granted geolocation permission, such as displaying on a privacy settings page or batch management on a permission management page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
