# InvocationHandler

Interface for handling method invocations on a proxy object. Defines methods to manage property access, assignment, and method invocation.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-reflect-interface InvocationHandler--><!--Device-reflect-interface InvocationHandler-End-->

**System capability:** SystemCapability.Utils.Lang

## get

```TypeScript
get(proxy: Proxy, method: InstanceMethod): Any
```

Intercepts the getter operation for the each property on the proxy object.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InvocationHandler-get(proxy: Proxy, method: InstanceMethod): Any--><!--Device-InvocationHandler-get(proxy: Proxy, method: InstanceMethod): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-na-reflect-proxy-c.md) | Yes | The proxy object being accessed. |
| method | [InstanceMethod](arkts-na-reflect-instancemethod-c.md) | Yes | Intercepted method. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | The value of the attribute. |

## invoke

```TypeScript
invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any
```

Intercepts invocation of a method on the proxy object with the provided arguments.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InvocationHandler-invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any--><!--Device-InvocationHandler-invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-na-reflect-proxy-c.md) | Yes | The proxy object on which the method is invoked. |
| method | [InstanceMethod](arkts-na-reflect-instancemethod-c.md) | Yes | Intercepted method. |
| args | FixedArray&lt;Any&gt; | Yes | An array of arguments that has been passed to the method. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | The result of the method call. |

## set

```TypeScript
set(proxy: Proxy, method: InstanceMethod, value: Any): void
```

Intercepts the setter operation of a method on the proxy object.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InvocationHandler-set(proxy: Proxy, method: InstanceMethod, value: Any): void--><!--Device-InvocationHandler-set(proxy: Proxy, method: InstanceMethod, value: Any): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-na-reflect-proxy-c.md) | Yes | The proxy object being modified. |
| method | [InstanceMethod](arkts-na-reflect-instancemethod-c.md) | Yes | Intercepted method. |
| value | Any | Yes | The value that has been passed to assign through the setter. |

