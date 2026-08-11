# PermissionRequest

Defines the onPermissionRequest callback, related to {@link onPermissionRequest} method.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PermissionRequest--><!--Device-unnamed-export declare class PermissionRequest-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PermissionRequest-constructor()--><!--Device-PermissionRequest-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deny

```TypeScript
deny(): void
```

Reject the request.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PermissionRequest-deny(): void--><!--Device-PermissionRequest-deny(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getAccessibleResource

```TypeScript
getAccessibleResource(): Array<string>
```

Gets the resource that the webpage is trying to access.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PermissionRequest-grant(resources: Array<string>): void--><!--Device-PermissionRequest-grant(resources: Array<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resources | Array&lt;string&gt; | Yes |  |

