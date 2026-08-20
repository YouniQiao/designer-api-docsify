# InvocationHandler

用于处理代理对象上方法调用的接口。 定义用于管理属性访问、赋值和方法调用的方法。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-reflect-interface InvocationHandler--><!--Device-reflect-interface InvocationHandler-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## get

```TypeScript
get(proxy: Proxy, method: InstanceMethod): Any
```

拦截代理对象上每个属性的getter操作。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvocationHandler-get(proxy: Proxy, method: InstanceMethod): Any--><!--Device-InvocationHandler-get(proxy: Proxy, method: InstanceMethod): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 | 被访问的代理对象。 |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | 被拦截的方法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 属性的值。 |

## invoke

```TypeScript
invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any
```

使用给定参数拦截代理对象上的方法调用。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvocationHandler-invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any--><!--Device-InvocationHandler-invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 | 调用该方法的代理对象。 |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | 被拦截的方法。 |
| args | FixedArray&lt;Any&gt; | 是 | 传入该方法的参数数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 方法调用的结果。 |

## set

```TypeScript
set(proxy: Proxy, method: InstanceMethod, value: Any): void
```

拦截代理对象上方法的setter操作。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvocationHandler-set(proxy: Proxy, method: InstanceMethod, value: Any): void--><!--Device-InvocationHandler-set(proxy: Proxy, method: InstanceMethod, value: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 | 被修改的代理对象。 |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 | 被拦截的方法。 |
| value | Any | 是 | 通过setter传入用于赋值的值。 |

