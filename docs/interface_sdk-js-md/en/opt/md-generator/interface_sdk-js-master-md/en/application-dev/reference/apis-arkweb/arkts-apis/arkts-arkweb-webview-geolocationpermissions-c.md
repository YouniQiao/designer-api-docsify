# GeolocationPermissions

Implements a **GeolocationPermissions** object.

> **NOTE：**
> 
> - The sample effect is subject to the actual device.
> 
> - You must load the **Web** component before calling the APIs in **GeolocationPermissions**.
> 
> - Required Permissions
> **ohos.permission.LOCATION**, **ohos.permission.APPROXIMATELY_LOCATION**, and
> **ohos.permission.LOCATION_IN_BACKGROUND**, which are required for accessing the location information. For details
> about the permissions, see
> [@ohos.geolocation (Geolocation)](../../../reference/apis-location-kit/js-apis-geolocation.md).

**Since:** 9

<!--Device-webview-class GeolocationPermissions--><!--Device-webview-class GeolocationPermissions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## allowGeolocation

```TypeScript
static allowGeolocation(origin: string, incognito?: boolean): void
```

Allows the specified origin to use the geolocation information.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static allowGeolocation(origin: string, incognito?: boolean): void--><!--Device-GeolocationPermissions-static allowGeolocation(origin: string, incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## deleteAllGeolocation

```TypeScript
static deleteAllGeolocation(incognito?: boolean): void
```

Clears the geolocation permission status of all sources.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static deleteAllGeolocation(incognito?: boolean): void--><!--Device-GeolocationPermissions-static deleteAllGeolocation(incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

## deleteGeolocation

```TypeScript
static deleteGeolocation(origin: string, incognito?: boolean): void
```

Clears the geolocation permission status of a specified origin.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static deleteGeolocation(origin: string, incognito?: boolean): void--><!--Device-GeolocationPermissions-static deleteGeolocation(origin: string, incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getAccessibleGeolocation

```TypeScript
static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>
```

Obtains the geolocation permission status of the specified origin. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>--><!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| incognito | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getAccessibleGeolocation

```TypeScript
static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void
```

Obtains the geolocation permission status of the specified origin. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void--><!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getStoredGeolocation

```TypeScript
static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>
```

Obtains the geolocation permission status of all origins. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>--><!--Device-GeolocationPermissions-static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getStoredGeolocation

```TypeScript
static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void
```

Obtains the geolocation permission status of all origins. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GeolocationPermissions-static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void--><!--Device-GeolocationPermissions-static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
