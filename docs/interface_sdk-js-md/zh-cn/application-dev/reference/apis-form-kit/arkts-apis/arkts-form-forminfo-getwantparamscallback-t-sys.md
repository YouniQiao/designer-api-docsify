# GetWantParamsCallback（系统接口）

```TypeScript
type GetWantParamsCallback = (formInfo: Array<formInfo.FormInfo>) => Array<Record<string, Object>>
```

Get want parameters callback.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formInfo-type GetWantParamsCallback = (formInfo: Array<formInfo.FormInfo>) => Array<Record<string, Object>>--><!--Device-formInfo-type GetWantParamsCallback = (formInfo: Array<formInfo.FormInfo>) => Array<Record<string, Object>>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formInfo | Array&lt;formInfo.FormInfo&gt; | 是 | The list of the form information. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;Record&lt;string, Object&gt;&gt; | The want parameters list of the forms. |

