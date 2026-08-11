# WebStorage

Implements a **WebStorage** object to manage the Web SQL database and HTML5 Web Storage APIs. All **Web**components in an application share a **WebStorage** object.

> **NOTE：**
> 
> - The sample effect is subject to the actual device.
> 
> - You must load the **Web** component before calling the APIs in **WebStorage**.
> 
> - After the ArkWeb kernel is upgraded to M132, the Web SQL database management becomes invalid because the kernel
> discards Web SQL. For details about the ArkWeb kernel version, see
> [Constraints](../../../web/web-component-overview.md#constraints).

**Since:** 9

<!--Device-webview-class WebStorage--><!--Device-webview-class WebStorage-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## deleteAllData

```TypeScript
static deleteAllData(incognito?: boolean): void
```

Deletes all storage data used by JavaScript storage APIs, including the Web SQL Database and HTML5-supported Web storage APIs.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static deleteAllData(incognito?: boolean): void--><!--Device-WebStorage-static deleteAllData(incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

## deleteOrigin

```TypeScript
static deleteOrigin(origin: string): void
```

Deletes all data in the specified origin.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static deleteOrigin(origin: string): void--><!--Device-WebStorage-static deleteOrigin(origin: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getOriginQuota

```TypeScript
static getOriginQuota(origin: string): Promise<number>
```

Obtains the storage quota of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes.This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static getOriginQuota(origin: string): Promise<number>--><!--Device-WebStorage-static getOriginQuota(origin: string): Promise<number>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getOriginQuota

```TypeScript
static getOriginQuota(origin: string, callback: AsyncCallback<number>): void
```

Obtains the storage quota of an origin in Web SQL Database and HTML5-supported Web Storage APIs, in bytes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static getOriginQuota(origin: string, callback: AsyncCallback<number>): void--><!--Device-WebStorage-static getOriginQuota(origin: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getOriginUsage

```TypeScript
static getOriginUsage(origin: string): Promise<number>
```

Obtains the storage usage of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes.This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static getOriginUsage(origin: string): Promise<number>--><!--Device-WebStorage-static getOriginUsage(origin: string): Promise<number>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getOriginUsage

```TypeScript
static getOriginUsage(origin: string, callback: AsyncCallback<number>): void
```

Obtains the storage usage of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes.This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static getOriginUsage(origin: string, callback: AsyncCallback<number>): void--><!--Device-WebStorage-static getOriginUsage(origin: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100011](../errorcode-webview.md#17100011-invalid-origin) |

## getOrigins

```TypeScript
static getOrigins(): Promise<Array<WebStorageOrigin>>
```

Obtains information about origins that are currently using the Web SQL Database and HTML5-supported Web Storage APIs. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static getOrigins(): Promise<Array<WebStorageOrigin>>--><!--Device-WebStorage-static getOrigins(): Promise<Array<WebStorageOrigin>>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;WebStorageOrigin&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100012](../errorcode-webview.md#17100012-no-web-storage-origin) |

## getOrigins

```TypeScript
static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void
```

Obtains information about origins that are currently using the Web SQL Database and HTML5-supported Web Storage APIs. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebStorage-static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void--><!--Device-WebStorage-static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;WebStorageOrigin&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17100012](../errorcode-webview.md#17100012-no-web-storage-origin) |
