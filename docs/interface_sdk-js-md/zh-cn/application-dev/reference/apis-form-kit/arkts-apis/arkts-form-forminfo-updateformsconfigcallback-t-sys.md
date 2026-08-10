# UpdateFormsConfigCallback（系统接口）

```TypeScript
type UpdateFormsConfigCallback = (configInfo: Array<FormCustomConfig>) => void
```

Callback for updating the forms.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formInfo-type UpdateFormsConfigCallback = (configInfo: Array<FormCustomConfig>) => void--><!--Device-formInfo-type UpdateFormsConfigCallback = (configInfo: Array<FormCustomConfig>) => void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configInfo | Array&lt;FormCustomConfig&gt; | 是 | the config info list of the forms. |

