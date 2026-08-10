# LifecycleForm

interface of form lifecycle.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

<!--Device-unnamed-export declare interface LifecycleForm--><!--Device-unnamed-export declare interface LifecycleForm-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

## onShare

```TypeScript
onShare?(formId: string): { [key: string]: any }
```

Called when the system shares the form.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-LifecycleForm-onShare?(formId: string): { [key: string]: any }--><!--Device-LifecycleForm-onShare?(formId: string): { [key: string]: any }-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Indicates the ID of the deleted form. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| { [key: string]: any } | Returns the wantParams object. |

## onShareForm

```TypeScript
onShareForm?(formId: string): Record<string, Object>
```

Called when the system shares the form.The ability of this function is same as onShare. If both are set, this function will be called.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-LifecycleForm-onShareForm?(formId: string): Record<string, Object>--><!--Device-LifecycleForm-onShareForm?(formId: string): Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Indicates the ID of the deleted form. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Returns the wantParams object. |

