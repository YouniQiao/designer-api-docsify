# castTempForm（系统接口）

## 导入模块

```TypeScript
```

## castTempForm

```TypeScript
function castTempForm(formId: string, callback: AsyncCallback<void>): void
```

将指定的临时卡片转换为普通卡片。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** castTempForm

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## castTempForm

```TypeScript
function castTempForm(formId: string): Promise<void>
```

将指定的临时卡片转换为普通卡片。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** castTempForm

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
