# Proxy

A base class for creating proxy objects that delegate method calls and property access to an `InvocationHandler`. Provides static methods for generating proxy classes and instantiating proxy objects dynamically at runtime.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| linker | RuntimeLinker | Yes |
| interfaces | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | Yes |
| handler | [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Proxy](arkts-arkts-reflect-proxy-c.md) |

## getHandler

```TypeScript
getHandler(): InvocationHandler
```

Retrieves the invocation handler associated with this proxy.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) |
