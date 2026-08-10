# ReflectProxy

A namespace that provides reflection and proxy functionality.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-namespace reflect--><!--Device-unnamed-namespace reflect-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [Proxy](arkts-arkts-reflect-proxy-c.md) | A base class for creating proxy objects that delegate method calls and property access to an `InvocationHandler`. Provides static methods for generating proxy classes and instantiating proxy objects dynamically at runtime. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | Interface for handling method invocations on a proxy object.Defines methods to manage property access, assignment, and method invocation. |

