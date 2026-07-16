# PermissionRequest

Implements the **PermissionRequest** object.For details about the sample code,see [onPermissionRequest](./arkts-basic-components-web-events.md#onpermissionrequest9).

> **NOTE**  
>  
> - The initial APIs of this component are supported since API version 8.  
> Updates will be marked with a superscript to indicate their earliest API version.  
>  
> - The initial APIs of this class are supported since API version 9.  
>  
> - The sample effect is subject to the actual device.

**Since:** 9

<!--Device-unnamed-declare class PermissionRequest--><!--Device-unnamed-declare class PermissionRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructs a **PermissionRequest** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-constructor()--><!--Device-PermissionRequest-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deny

```TypeScript
deny(): void
```

Denies the permission requested by the web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-deny(): void--><!--Device-PermissionRequest-deny(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getAccessibleResource

```TypeScript
getAccessibleResource(): Array<string>
```

Obtains the list of accessible resources requested for the web page. For details about the resource types, see [ProtectedResourceType](arkts-arkweb-protectedresourcetype-e.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-getAccessibleResource(): Array<string>--><!--Device-PermissionRequest-getAccessibleResource(): Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Array](../../apis-na/arkts-apis/arkts-na-array-i.md)<string> | @syscap SystemCapability.Web.Webview.Core@crossplatform |

## getOrigin

```TypeScript
getOrigin(): string
```

Obtains the origin of this web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-getOrigin(): string--><!--Device-PermissionRequest-getOrigin(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | @syscap SystemCapability.Web.Webview.Core@crossplatform |

## grant

```TypeScript
grant(resources: Array<string>): void
```

Grants the permission for resources requested by the web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-grant(resources: Array<string>): void--><!--Device-PermissionRequest-grant(resources: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resources | [Array](../../apis-na/arkts-apis/arkts-na-array-i.md)<string> | Yes | List of resources that can be requested by the web page with the permission to |

