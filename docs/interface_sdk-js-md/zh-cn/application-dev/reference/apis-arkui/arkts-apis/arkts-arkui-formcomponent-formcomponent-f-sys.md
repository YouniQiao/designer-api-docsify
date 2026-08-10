# FormComponent（系统接口）

## FormComponent

```TypeScript
export declare function FormComponent(
    formInfo: FormInfo, 
    content_?: CustomBuilder,
): FormComponentAttribute
```

Defines FormComponent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function FormComponent(    formInfo: FormInfo,     content_?: CustomBuilder,): FormComponentAttribute--><!--Device-unnamed-export declare function FormComponent(    formInfo: FormInfo,     content_?: CustomBuilder,): FormComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formInfo | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i-sys.md) | 是 | The formInfo |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FormComponentAttribute](../arkts-components/arkts-arkui-formcomponent-attribute.md) |  |

