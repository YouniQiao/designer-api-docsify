# with_theme(Defines WithTheme component.)

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [WithThemeAttribute](arkts-arkui-withthemeattribute-c.md) | 不支持通用属性。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [WithThemeOptions](arkts-arkui-withthemeoptions-i.md) | 设置WithTheme作用域内组件默认配色及深浅色模式。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [CustomTheme](arkts-arkui-customtheme-t.md) | 用于自定义WithTheme作用域内组件的配色方案，具体配色项通过CustomColors接口配置。 |
| [WithThemeInterface](arkts-arkui-withthemeinterface-t.md) | Define the function of WithThemeInterface. |

### 常量

| 名称 | 说明 |
| --- | --- |
| [WithTheme](arkts-arkui-withtheme-con.md) | Defines WithTheme Logic Component. |
| [WithThemeInstance](arkts-arkui-withtheme-con.md#withthemeinstance) | Defines WithTheme Logic Component Instance. |

## 示例

```TypeScript
设置局部深浅色模式时，需要添加dark.json资源文件，深浅色模式才会生效。



dark.json数据示例：
```

```TypeScript
### 示例1（指定局部深浅色模式）


```

```TypeScript
### 示例2（自定义WithTheme作用域内组件默认配色）
```
