# WithEnv(定义WithEnv组件，允许为子组件设置环境属性。)

WithEnv组件用于为子组件树设置局部环境变量作用域。开发者可以通过该组件为后代组件提供自定义环境变量，或设置系统环境变量。

> **说明：**

> - 此接口仅可在Stage模型下使用。 > > - 可通过[customEnv](arkts-arkui-withenv-comp-attribute.md#customenv)设置自定义环境变量。 > > - 支持通过[env](arkts-arkui-withenv-comp-attribute.md#env)设置的系统环境变量键，系统环境变量键存于[WritableEnvKey](arkts-arkui-common-comp-writableenvkey-c.md)。 > > - WithEnv嵌套时，同名环境变量按最近作用域生效。

## 子组件

支持单个子组件。

## 汇总

## 示例

```TypeScript
### 示例1（设置局部字体缩放）

该示例通过为作用域内组件设置局部字体缩放比例。

从API版本26.0.0开始，新增env属性和键值WritableEnvKey.FONT_SCALE。


```

```TypeScript
### 示例2（设置局部布局方向）

该示例通过为作用域内组件设置局部布局方向。

从API版本26.0.0开始，新增env属性和键值WritableEnvKey.DIRECTION。
```
