# Proxy

用于创建代理对象的基类，这些代理对象将方法调用和属性访问委托给 `InvocationHandler`。提供用于在运行时动态生成代理类和 实例化代理对象的静态方法。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## create

```TypeScript
static create(linker: RuntimeLinker, interfaces: FixedArray<Class>, handler: InvocationHandler): Proxy
```

创建一个实现指定接口并使用给定处理器的新代理实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| linker | RuntimeLinker | 是 |
| interfaces | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 是 |
| handler | [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Proxy](arkts-arkts-reflect-proxy-c.md) |

## getHandler

```TypeScript
getHandler(): InvocationHandler
```

获取与该代理关联的调用处理器。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) |
