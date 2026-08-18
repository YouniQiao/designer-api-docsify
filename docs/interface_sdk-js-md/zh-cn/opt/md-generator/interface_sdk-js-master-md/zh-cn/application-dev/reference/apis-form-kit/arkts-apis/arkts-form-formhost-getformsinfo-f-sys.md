# getFormsInfo（系统接口）

## 导入模块

```TypeScript
```

## getFormsInfo

```TypeScript
function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void
```

获取设备上指定应用程序提供的卡片信息（不包含模板卡片）。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void--><!--Device-formHost-function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |


## getFormsInfo

```TypeScript
function getFormsInfo(
    bundleName: string,
    moduleName: string,
    callback: AsyncCallback<Array<formInfo.FormInfo>>
  ): void
```

获取设备上指定应用程序提供的卡片信息（不包含模板卡片）。使用callback异步回调。

**起始版本：** 23

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |


## getFormsInfo

```TypeScript
function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>
```

获取设备上指定应用程序提供的卡片信息（不包含模板卡片）。使用Promise异步回调。

**起始版本：** 23

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |


## getFormsInfo

```TypeScript
function getFormsInfo(filter: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>
```

获取设备上指定应用程序提供的卡片信息（不包含模板卡片）。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(filter: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>--><!--Device-formHost-function getFormsInfo(filter: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | formInfo.FormInfoFilter | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
