# disableFormsUpdate（系统接口）

## 导入模块

```TypeScript
```

## disableFormsUpdate

```TypeScript
function disableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void
```

向卡片框架发送通知以使指定的卡片不可以更新。该方法调用成功后，卡片刷新状态设置为去使能，卡片不可以接收来自卡片提供方的更新。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableformsupdate系统接口)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function disableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void--><!--Device-formHost-function disableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## disableFormsUpdate

```TypeScript
function disableFormsUpdate(formIds: Array<string>): Promise<void>
```

向卡片框架发送通知以使指定的卡片不可以更新。该方法调用成功后，卡片刷新状态设置为去使能，卡片不可以接收来自卡片提供方的更新。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableformsupdate系统接口)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function disableFormsUpdate(formIds: Array<string>): Promise<void>--><!--Device-formHost-function disableFormsUpdate(formIds: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
