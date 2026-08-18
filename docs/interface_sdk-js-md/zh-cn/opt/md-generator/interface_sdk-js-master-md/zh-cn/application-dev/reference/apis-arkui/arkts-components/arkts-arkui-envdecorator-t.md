# EnvDecorator

```TypeScript
declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator
```

定义EnvDecorator属性装饰器类型。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator--><!--Device-unnamed-declare type EnvDecorator = (value: SystemProperties) => PropertyDecorator-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SystemProperties](arkts-arkui-systemproperties-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| PropertyDecorator |
