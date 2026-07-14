# CustomTheme

自定义主题风格对象。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors?: CustomColors
```

自定义浅色主题颜色资源。</br>

**类型：** CustomColors

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本12开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## darkColors

```TypeScript
darkColors?: CustomDarkColors
```

自定义深色主题颜色资源。

**说明**：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。</br>

**类型：** CustomDarkColors

**默认值：** If not set darkColors, color value will same as colors under light mode and will not change with color
mode, unless the color is setted by resource in dark directory.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本20开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

