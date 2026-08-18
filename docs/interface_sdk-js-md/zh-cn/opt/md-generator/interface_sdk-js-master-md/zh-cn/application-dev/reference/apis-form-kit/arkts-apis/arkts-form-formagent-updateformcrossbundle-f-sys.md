# updateFormCrossBundle（系统接口）

## 导入模块

```TypeScript
```

## updateFormCrossBundle

```TypeScript
function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>
```

跨应用更新卡片，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.UPDATE_FORM_CROSS_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formAgent-function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>--><!--Device-formAgent-function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| [formBindingData](arkts-app-form-formbindingdata.md) | formBindingData.FormBindingData | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501007](../errorcode-form.md#16501007-卡片不可信) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
