# Proxy

A base class for creating proxy objects that delegate method calls and property access  to an `InvocationHandler`. Provides static methods for generating proxy classes and  instantiating proxy objects dynamically at runtime.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-reflect-class Proxy--><!--Device-reflect-class Proxy-End-->

**系统能力：** SystemCapability.Utils.Lang

## create

```TypeScript
static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy
```

Creates a new proxy instance that implements the specified interfaces and uses the provided handler.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Proxy-static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy--><!--Device-Proxy-static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| linker | RuntimeLinker | 是 | The `RuntimeLinker` used to generate the proxy class at runtime. |
| interfaces | FixedArray&lt;Class&gt; | 是 | An array of `Class` objects representing the interfaces to implement. |
| handler | [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | 是 | The `InvocationHandler` to handle method and property operations. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Proxy](arkts-arkts-reflect-proxy-c.md) | A new proxy instance as an `Proxy`. |

## getHandler

```TypeScript
getHandler(): InvocationHandler
```

Retrieves the invocation handler associated with this proxy.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Proxy-getHandler(): InvocationHandler--><!--Device-Proxy-getHandler(): InvocationHandler-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | The `InvocationHandler` used by this proxy. |

