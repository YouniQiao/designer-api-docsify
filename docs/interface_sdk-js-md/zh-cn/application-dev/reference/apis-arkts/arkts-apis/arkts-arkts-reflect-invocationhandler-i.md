# InvocationHandler

Interface for handling method invocations on a proxy object.Defines methods to manage property access, assignment, and method invocation.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-reflect-interface InvocationHandler--><!--Device-reflect-interface InvocationHandler-End-->

**系统能力：** SystemCapability.Utils.Lang

## get

```TypeScript
get(proxy: Proxy, method: InstanceMethod): Any
```

Intercepts the getter operation for the each property on the proxy object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvocationHandler-get(proxy: Proxy, method: InstanceMethod): Any--><!--Device-InvocationHandler-get(proxy: Proxy, method: InstanceMethod): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 | The proxy object being accessed. |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | Intercepted method. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | The value of the attribute. |

## invoke

```TypeScript
invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any
```

Intercepts invocation of a method on the proxy object with the provided arguments.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvocationHandler-invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any--><!--Device-InvocationHandler-invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 | The proxy object on which the method is invoked. |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | Intercepted method. |
| args | FixedArray&lt;Any&gt; | 是 | An array of arguments that has been passed to the method. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | The result of the method call. |

## set

```TypeScript
set(proxy: Proxy, method: InstanceMethod, value: Any): void
```

Intercepts the setter operation of a method on the proxy object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvocationHandler-set(proxy: Proxy, method: InstanceMethod, value: Any): void--><!--Device-InvocationHandler-set(proxy: Proxy, method: InstanceMethod, value: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 | The proxy object being modified. |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | Intercepted method. |
| value | Any | 是 | The value that has been passed to assign through the setter. |

