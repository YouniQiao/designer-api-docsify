# FormEditExtensionContext

**FormEditExtensionContext**, inherited from   
[UIExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiextensioncontext-c.md/arkts-ability-uiextensioncontext-c.md), is the context of   
[FormEditExtensionAbility](arkts-form-app-form-formeditextensionability-formeditextensionability-c.md).

> **NOTE：**

> - The APIs of this module can be used only in the stage model.

**继承/实现关系：** FormEditExtensionContext extends [UIExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiextensioncontext-c.md/arkts-ability-uiextensioncontext-c.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class FormEditExtensionContext extends UIExtensionContext--><!--Device-unnamed-declare class FormEditExtensionContext extends UIExtensionContext-End-->

**系统能力：** SystemCapability.Ability.Form

## startSecondPage

```TypeScript
startSecondPage(want: Want): Promise<AbilityResult>
```

Starts the widget provider page to be edited. This API uses a promise to return the result.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormEditExtensionContext-startSecondPage(want: Want): Promise<AbilityResult>--><!--Device-FormEditExtensionContext-startSecondPage(want: Want): Promise<AbilityResult>-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Information about the editing page that needs to be started by the home screen of a third-party application. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AbilityResult](../../apis-ability-kit/arkts-apis/arkts-ability-abilityresult-abilityresult-i.md)&gt; | Promise used to return the ability result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |
| 16500050 | An IPC connection error happened. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |

## startUIAbility

```TypeScript
startUIAbility(want: Want): Promise<void>
```

Starts UIAbility of the application to which a widget belongs. This API uses a promise to return the result.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormEditExtensionContext-startUIAbility(want: Want): Promise<void>--><!--Device-FormEditExtensionContext-startUIAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Want information of the UIAbility of the application. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000130 | The target UIAbility does not belong to the caller. |
| 16500050 | An IPC connection error happened. |
| 16501014 | The form edit page is not in the foreground. The current operation is not supported. |
| 16000121 | The target component type is not a UIAbility. |
| 16500100 | Failed to obtain the configuration information. |

