# notifyFormsEnableUpdate（系统接口）

## 导入模块

```TypeScript
```

## notifyFormsEnableUpdate

```TypeScript
function notifyFormsEnableUpdate(
    formIds: Array<string>,
    isEnableUpdate: boolean,
    callback: AsyncCallback<void>
  ): void
```

通知卡片是否启用更新状态。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyformsenableupdate系统接口)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsEnableUpdate(    formIds: Array<string>,    isEnableUpdate: boolean,    callback: AsyncCallback<void>  ): void--><!--Device-formHost-function notifyFormsEnableUpdate(    formIds: Array<string>,    isEnableUpdate: boolean,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| isEnableUpdate | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## notifyFormsEnableUpdate

```TypeScript
function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>
```

通知卡片是否启用更新状态。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyformsenableupdate系统接口)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>--><!--Device-formHost-function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| isEnableUpdate | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
