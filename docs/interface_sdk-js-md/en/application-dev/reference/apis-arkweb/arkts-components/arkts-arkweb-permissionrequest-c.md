# PermissionRequest

权限请求。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare class PermissionRequest--><!--Device-unnamed-declare class PermissionRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

PermissionRequest的构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-constructor()--><!--Device-PermissionRequest-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deny

```TypeScript
deny(): void
```

Reject the request.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-deny(): void--><!--Device-PermissionRequest-deny(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getAccessibleResource

```TypeScript
getAccessibleResource(): Array<string>
```

Gets the resource that the webpage is trying to access.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-getAccessibleResource(): Array<string>--><!--Device-PermissionRequest-getAccessibleResource(): Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; |  |

## getOrigin

```TypeScript
getOrigin(): string
```

Gets the source if the webpage that attempted to access the restricted resource.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-getOrigin(): string--><!--Device-PermissionRequest-getOrigin(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## grant

```TypeScript
grant(resources: Array<string>): void
```

Grant origin access to a given resource.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PermissionRequest-grant(resources: Array<string>): void--><!--Device-PermissionRequest-grant(resources: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resources | Array&lt;string&gt; | Yes | List of resources that can be requested by the web page with the permission to grant. |

