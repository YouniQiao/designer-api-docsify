# GeolocationPermissions

Provides a method for managing web geographic location permissions.

**起始版本：** 9

<!--Device-webview-class GeolocationPermissions--><!--Device-webview-class GeolocationPermissions-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## allowGeolocation

```TypeScript
static allowGeolocation(origin: string, incognito?: boolean): void
```

Allow geolocation permissions for specifies source.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static allowGeolocation(origin: string, incognito?: boolean): void--><!--Device-GeolocationPermissions-static allowGeolocation(origin: string, incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| origin | string | 是 |
| incognito | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17100011](../errorcode-webview.md#17100011-输入参数origin错误) |

## deleteAllGeolocation

```TypeScript
static deleteAllGeolocation(incognito?: boolean): void
```

Delete all geolocation permissions.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static deleteAllGeolocation(incognito?: boolean): void--><!--Device-GeolocationPermissions-static deleteAllGeolocation(incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| incognito | boolean | 否 |

## deleteGeolocation

```TypeScript
static deleteGeolocation(origin: string, incognito?: boolean): void
```

Delete geolocation permissions for specifies source.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static deleteGeolocation(origin: string, incognito?: boolean): void--><!--Device-GeolocationPermissions-static deleteGeolocation(origin: string, incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| origin | string | 是 |
| incognito | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17100011](../errorcode-webview.md#17100011-输入参数origin错误) |

## getAccessibleGeolocation

```TypeScript
static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>
```

Gets the geolocation permission status of the specified source.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>--><!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| origin | string | 是 |
| incognito | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17100011](../errorcode-webview.md#17100011-输入参数origin错误) |

## getAccessibleGeolocation

```TypeScript
static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void
```

Gets the geolocation permission status of the specified source.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void--><!--Device-GeolocationPermissions-static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| origin | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |
| incognito | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17100011](../errorcode-webview.md#17100011-输入参数origin错误) |

## getStoredGeolocation

```TypeScript
static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>
```

Get all stored geolocation permission url source.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>--><!--Device-GeolocationPermissions-static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| incognito | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## getStoredGeolocation

```TypeScript
static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void
```

Get all stored geolocation permission url source.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-GeolocationPermissions-static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void--><!--Device-GeolocationPermissions-static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |
| incognito | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
