# PublishFormCrossBundleControlCallback（系统接口）

```TypeScript
type PublishFormCrossBundleControlCallback = (info: PublishFormCrossBundleInfo) => boolean
```

publish form cross bundle control callback.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formInfo-type PublishFormCrossBundleControlCallback = (info: PublishFormCrossBundleInfo) => boolean--><!--Device-formInfo-type PublishFormCrossBundleControlCallback = (info: PublishFormCrossBundleInfo) => boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [PublishFormCrossBundleInfo](arkts-form-forminfo-publishformcrossbundleinfo-i-sys.md) | 是 | Publish form cross bundle info. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Publish form cross bundle control result, true indicates success, false indicates failure. |

