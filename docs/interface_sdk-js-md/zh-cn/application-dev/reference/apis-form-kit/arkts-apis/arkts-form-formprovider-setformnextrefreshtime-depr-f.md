# setFormNextRefreshTime

## 导入模块

```TypeScript
```

## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void
```

设置指定卡片的下一次刷新时间，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setFormNextRefreshTime](arkts-form-formprovider-setformnextrefreshtime-f.md)

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| minute | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: number): Promise<void>
```

设置指定卡片的下一次刷新时间，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setFormNextRefreshTime](arkts-form-formprovider-setformnextrefreshtime-f.md)

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| minute | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
