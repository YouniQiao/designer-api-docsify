# updateForm

## 导入模块

```TypeScript
```

## updateForm

```TypeScript
function updateForm(
    formId: string,
    formBindingData: formBindingData.FormBindingData,
    callback: AsyncCallback<void>
  ): void
```

更新指定的卡片，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [updateForm](arkts-form-formprovider-updateform-f.md)

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| [formBindingData](arkts-application-formbindingdata.md) | formBindingData.FormBindingData | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## updateForm

```TypeScript
function updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>
```

更新指定的卡片，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [updateForm](arkts-form-formprovider-updateform-f.md)

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| [formBindingData](arkts-application-formbindingdata.md) | formBindingData.FormBindingData | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
