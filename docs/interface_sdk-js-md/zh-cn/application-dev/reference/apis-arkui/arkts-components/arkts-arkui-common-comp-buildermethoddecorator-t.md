# BuilderMethodDecorator

```TypeScript
declare type BuilderMethodDecorator = (value: BuilderDecoratorConfig) => MethodDecorator
```

定义带配置的Builder装饰器类型。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-unnamed-declare type BuilderMethodDecorator = (value: BuilderDecoratorConfig) => MethodDecorator--><!--Device-unnamed-declare type BuilderMethodDecorator = (value: BuilderDecoratorConfig) => MethodDecorator-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BuilderDecoratorConfig](arkts-arkui-common-comp-builderdecoratorconfig-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MethodDecorator | 方法装饰器。 |
