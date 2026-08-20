# ReflectProxy

提供反射与代理功能的命名空间。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-namespace reflect--><!--Device-unnamed-namespace reflect-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [Proxy](arkts-arkts-reflect-proxy-c.md) | 用于创建代理对象的基类，这些代理对象将方法调用和属性访问委托给 `InvocationHandler`。提供用于在运行时动态生成代理类和 实例化代理对象的静态方法。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [InvocationHandler](arkts-arkts-reflect-invocationhandler-i.md) | 用于处理代理对象上方法调用的接口。 定义用于管理属性访问、赋值和方法调用的方法。 |

