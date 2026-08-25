# PermissionRequest

PermissionRequest 是 Web 组件用于授权或拒绝权限请求的对象。当网页尝试访问受保护的系统资源（如摄像头、麦克风、地理位置等）时，ArkWeb 内核会通过 [onPermissionRequest](arkts-arkweb-web-attribute.md#onpermissionrequest)事件回调向应用发送权限请求，应用通过 PermissionRequest 对象来决定是否授权这些请求。该对象适用 于需要在应用中管理网页对敏感资源的访问权限、保护用户隐私、确保资源访问安全可控等场景，帮助开发者灵活处理网页权限请求。

> **说明：**&gt;
> - [grant](#grant)()与 [deny](#deny)() 方法互斥，对于同一个 PermissionRequest 对象，
> 只能调用其中一个方法。&gt;
> - 调用 grant() 或 deny() 后，该 PermissionRequest 对象已完成响应，不允许重复调用。&gt;
> - 未调用任何方法响应的 PermissionRequest 对象会导致权限请求超时。&gt;
> - grant() 方法的 resources 参数通常使用 getAccessibleResource() 方法的返回值。&gt;
> - 典型使用流程：调用 getAccessibleResource() 获取请求的资源列表，选择需要授权的资源后调用 grant() 进行授权。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

PermissionRequest的构造函数。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## deny

```TypeScript
deny(): void
```

拒绝网页所请求的权限。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## getAccessibleResource

```TypeScript
getAccessibleResource(): Array<string>
```

获取网页所请求的权限资源列表，类型参考[ProtectedResourceType](arkts-arkweb-protectedresourcetype-e.md)。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getOrigin

```TypeScript
getOrigin(): string
```

获取网页来源。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## grant

```TypeScript
grant(resources: Array<string>): void
```

对网页所请求的权限进行授权。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resources | Array & lt;string & gt; | 是 |
