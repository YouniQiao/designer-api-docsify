# Proxy

A base class for creating proxy objects that delegate method calls and property access to an `InvocationHandler`. Provides static methods for generating proxy classes and instantiating proxy objects dynamically at runtime.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-reflect-class Proxy--><!--Device-reflect-class Proxy-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## create

```TypeScript
static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy
```

Creates a new proxy instance that implements the specified interfaces and uses the provided handler.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Proxy-static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy--><!--Device-Proxy-static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| linker | RuntimeLinker | Yes | The `RuntimeLinker` used to generate the proxy class at runtime. |
| interfaces | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | Yes | An array of `Class` objects representing the interfaces to implement. |
| handler | [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | Yes | The `InvocationHandler` to handle method and property operations. |

**Return value:**

| Type | Description |
| --- | --- |
| [Proxy](arkts-arkts-reflect-proxy-c.md) | A new proxy instance as an `Proxy`. |

## getHandler

```TypeScript
getHandler(): InvocationHandler
```

Retrieves the invocation handler associated with this proxy.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Proxy-getHandler(): InvocationHandler--><!--Device-Proxy-getHandler(): InvocationHandler-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | The `InvocationHandler` used by this proxy. |

