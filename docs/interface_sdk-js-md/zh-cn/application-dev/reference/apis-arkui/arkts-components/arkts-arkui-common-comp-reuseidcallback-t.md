# ReuseIdCallback

```TypeScript
declare type ReuseIdCallback = () => string
```

获取复用标识ID的回调方法。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-declare type ReuseIdCallback = () => string--><!--Device-unnamed-declare type ReuseIdCallback = () => string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 复用标识ID，由开发者指定。<br>未指定或使用空字符串`''`作为复用标识ID时，将默认使用自定义组件名。<br>在API版本26.0.0之前，当该回调不是显式返回字符串字面量时，实际复用标识ID将为自定义组件名，回调返回值不生效；在API版本26.0.0及以后，回调的实际返回结果将作为复用标识ID。 |
