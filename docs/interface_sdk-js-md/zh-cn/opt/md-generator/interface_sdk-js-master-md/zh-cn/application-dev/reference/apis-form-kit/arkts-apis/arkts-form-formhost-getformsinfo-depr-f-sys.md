# getFormsInfo（系统接口）

## 导入模块

```TypeScript
```

## getFormsInfo

```TypeScript
function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void
```

获取设备上指定应用程序提供的卡片信息。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo系统接口)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void--><!--Device-formHost-function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | 是 |


## getFormsInfo

```TypeScript
function getFormsInfo(
    bundleName: string,
    moduleName: string,
    callback: AsyncCallback<Array<formInfo.FormInfo>>
  ): void
```

获取设备上指定应用程序提供的卡片信息。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo系统接口)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(    bundleName: string,    moduleName: string,    callback: AsyncCallback<Array<formInfo.FormInfo>>  ): void--><!--Device-formHost-function getFormsInfo(    bundleName: string,    moduleName: string,    callback: AsyncCallback<Array<formInfo.FormInfo>>  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | 是 |


## getFormsInfo

```TypeScript
function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>
```

获取设备上指定应用程序提供的卡片信息。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getformsinfo系统接口)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>--><!--Device-formHost-function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |
