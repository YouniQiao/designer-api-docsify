# InvocationHandler

用于处理代理对象上方法调用的接口。 定义用于管理属性访问、赋值和方法调用的方法。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Any |

## invoke

```TypeScript
invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any
```

使用给定参数拦截代理对象上的方法调用。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Any |

## set

```TypeScript
set(proxy: Proxy, method: InstanceMethod, value: Any): void
```

拦截代理对象上方法的setter操作。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | 是 |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | 是 |
| value | Any | 是 |
